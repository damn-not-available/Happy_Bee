from datetime import datetime
import requests, pprint
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *

# auth
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

# 직접 save 할 필요 없이, 요청에 따라 자동으로 판단하고 실행시킴
@api_view(['GET'])
def save_products(request):
    print('save_function')
    # 저장 프로세스
    def get_products():
        api_key = settings.FSS_API_KEY
        
        deposit_url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
        saving_url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
        params = {
            'auth' : api_key,
            'topFinGrpNo' : '020000',
            'pageNo':1
        }

        # 저장 시간 기록
        createdtime = CreatedTime()
        createdtime.save()

        # 기존 정보 삭제
        DepositProduct.objects.all().delete()
        DepositOptions.objects.all().delete()
        SavingProduct.objects.all().delete()
        SavingOptions.objects.all().delete()

        # 예금상품 정보 저장
        response = requests.get(deposit_url, params=params).json()
        baselist = response['result']['baseList']
        serializer = DepositProductSerializer(data=baselist, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # 예금옵션 정보 저장
        optionlist = response['result']['optionList']
        for option in optionlist:
            serializer = DepositOptionsSerializer(data=option)
            depositproduct = DepositProduct.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if serializer.is_valid(raise_exception=True):
                serializer.save(fin_prdt_cd=depositproduct)

        # 적금상품 정보 저장
        response = requests.get(saving_url, params=params).json()
        baselist = response['result']['baseList']
        serializer = SavingProductSerializer(data=baselist, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # 적금옵션 정보 저장
        optionlist = response['result']['optionList']
        for option in optionlist:
            serializer = SavingOptionsSerializer(data=option)
            savingproduct = SavingProduct.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if serializer.is_valid(raise_exception=True):
                serializer.save(fin_prdt_cd=savingproduct)

        print('saved')
        return Response(status=status.HTTP_201_CREATED)

    # 데이터 최신 여부 확인    # 데이터 최신 여부 확인 - 참고 : autonow와 datatime의 시간에 9시간의 오차 있음 - USE_TZ 해결 완료
    beforetime = CreatedTime.objects.last()
    # print(beforetime.created_at)
    if beforetime:
        nowtime = datetime.now()
        # print(nowtime)
        if beforetime.created_at.year == nowtime.year and beforetime.created_at.month == nowtime.month and beforetime.created_at.day == nowtime.day:
            # not save
            print('need_not_save')
            pass
        else:
            # have to save
            # print('case1')
            get_products()
    else:
        # have to save
        # print('case2')
        get_products()

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def deposits(request):
    depositproduct = get_list_or_404(DepositProduct)
    serializer = DepositProductDetailSerializer(depositproduct, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def savings(request):
    savingproduct = get_list_or_404(SavingProduct)
    serializer = SavingProductDetailSerializer(savingproduct, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_options_all(request):
    depositoptions = get_list_or_404(DepositOptions)
    serializer = DepositOptionsSerializer(depositoptions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def saving_options_all(request):
    savingoptions = get_list_or_404(SavingOptions)
    serializer = SavingOptionsSerializer(savingoptions, many=True)
    return Response(serializer.data)


# 상당수 안쓰이게됐지만 일단 놔둘까
@api_view(['GET'])
def deposit_detail(request, deposit_pk):
    depositproduct = get_list_or_404(DepositProduct, pk=deposit_pk)
    serializer = DepositProductDetailSerializer(depositproduct, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_options(request, deposit_pk):
    depositoptions = get_list_or_404(DepositOptions, fin_prdt_cd=deposit_pk)
    serializer = DepositOptionsSerializer(depositoptions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def saving_detail(request, saving_pk):
    savingproduct = get_list_or_404(SavingProduct)
    serializer = SavingProductDetailSerializer(savingproduct, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_general_recommendation(request):
    # 최고 우대 금리
    deposit_options_desc = DepositOptions.objects.order_by('-intr_rate2')
    deposit_highest_intr_rate2 = deposit_options_desc.first()
    deposit_product_highest_intr_rate2 = DepositProduct.objects.get(pk=deposit_highest_intr_rate2.fin_prdt_cd_id)
    
    # 신규 가입 필터링
    deposit_new_signup = DepositProduct.objects.filter(spcl_cnd__icontains="신규")
    
    # 인터넷 가입 필터링
    temp = DepositProduct.objects.filter(spcl_cnd__icontains="인터넷")
    deposit_internet_signup = temp.filter(spcl_cnd__icontains="가입")
    
    # 한도없는
    deposit_unlimited = DepositProduct.objects.filter(max_limit__isnull=True)
    
    # 랜덤 추천
    # deposit_random = DepositProduct.objects.order_by('?').first()

    # 전송하기 위한 시리얼라이즈, 딕셔너리 및 전송
    deposit_highest_intr_rate2 = DepositOptionsSerializer(deposit_highest_intr_rate2)
    deposit_product_highest_intr_rate2 = DepositProductSerializer(deposit_product_highest_intr_rate2)
    deposit_new_signup = DepositProductSerializer(deposit_new_signup, many=True)
    deposit_internet_signup = DepositProductSerializer(deposit_internet_signup, many=True)
    deposit_unlimited = DepositProductSerializer(deposit_unlimited, many=True)
    # deposit_random = DepositProductSerializer(deposit_random)

    data = {
        'deposit_highest_intr_rate2' : deposit_highest_intr_rate2.data,
        'deposit_product_highest_intr_rate2' : deposit_product_highest_intr_rate2.data,
        'deposit_new_signup' : deposit_new_signup.data,
        'deposit_internet_signup' : deposit_internet_signup.data,
        'deposit_unlimited' : deposit_unlimited.data,
        # 'deposit_random' : deposit_random.data,
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def random_deposit(request):
    product = DepositProduct.objects.order_by('?').first()
    data = DepositProductSerializer(product)
    return Response(data.data, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def saving_general_recommendation(request):
    # 최고 우대 금리
    saving_options_desc = SavingOptions.objects.order_by('-intr_rate2')
    saving_highest_intr_rate2 = saving_options_desc.first()
    saving_product_highest_intr_rate2 = SavingProduct.objects.get(pk=saving_highest_intr_rate2.fin_prdt_cd_id)
    
    # 신규 가입 필터링
    saving_new_signup = SavingProduct.objects.filter(spcl_cnd__icontains="신규")
    
    # 인터넷 가입 필터링
    temp = SavingProduct.objects.filter(spcl_cnd__icontains="인터넷")
    saving_internet_signup = temp.filter(spcl_cnd__icontains="가입")
    
    # 랜덤 추천
    # saving_random = SavingProduct.objects.order_by('?').first()
    
    # 한도없는
    saving_unlimited = SavingProduct.objects.filter(max_limit__isnull=True)

    # 전송하기 위한 시리얼라이즈, 딕셔너리 및 전송
    saving_highest_intr_rate2 = SavingOptionsSerializer(saving_highest_intr_rate2)
    saving_product_highest_intr_rate2 = SavingProductSerializer(saving_product_highest_intr_rate2)
    saving_new_signup = SavingProductSerializer(saving_new_signup, many=True)
    saving_internet_signup = SavingProductSerializer(saving_internet_signup, many=True)
    # saving_random = SavingProductSerializer(saving_random)
    saving_unlimited = SavingProductSerializer(saving_unlimited, many=True)

    data = {
        'saving_highest_intr_rate2' : saving_highest_intr_rate2.data,
        'saving_product_highest_intr_rate2' : saving_product_highest_intr_rate2.data,
        'saving_new_signup' : saving_new_signup.data,
        'saving_internet_signup' : saving_internet_signup.data,
        # 'saving_random' : saving_random.data,
        'saving_unlimited' : saving_unlimited.data,
        }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def random_saving(request):
    product = SavingProduct.objects.order_by('?').first()
    data = SavingProductSerializer(product)
    return Response(data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def deposit_get_classified(request):
    bank, period = request.data['bank'], request.data['period']

    if bank == 'null':
        depositproduct = DepositProduct.objects.all()
    else:
        depositproduct = DepositProduct.objects.filter(kor_co_nm=bank)
    if period == 'null':
        depositoptions = DepositOptions.objects.all()
    else:
        depositoptions =  DepositOptions.objects.filter(save_trm=int(period))

    fin_prdt_cds = depositproduct.values_list('id', flat=True)
    filtered_depositoptions = depositoptions.filter(fin_prdt_cd__in=fin_prdt_cds)

    serializer = DepositOptionsSerializer(filtered_depositoptions, many=True)  
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def saving_get_classified(request):
    bank, period = request.data['bank'], request.data['period']

    if bank == 'null':
        savingproduct = SavingProduct.objects.all()
    else:
        savingproduct = SavingProduct.objects.filter(kor_co_nm=bank)
    if period == 'null':
        savingoptions = SavingOptions.objects.all()
    else:
        savingoptions =  SavingOptions.objects.filter(save_trm=int(period))

    fin_prdt_cds = savingproduct.values_list('id', flat=True)
    filtered_savingoptions = savingoptions.filter(fin_prdt_cd__in=fin_prdt_cds)

    serializer = SavingOptionsSerializer(filtered_savingoptions, many=True)  
    return Response(data=serializer.data, status=status.HTTP_200_OK)


from accounts.models import User
@api_view(['POST'])
def personal_recommend(request):
    client = request.data['user']
    users_have_product = User.objects.exclude(financial_products__exact='').exclude(id=client['id'])
    
    client_salary = client['salary']
    recommend_salary = min(users_have_product, key=lambda user: abs(user.salary - client_salary))

    client_money = client['money']
    recommend_money = min(users_have_product, key=lambda user: abs(user.money - client_money))
    
    recommend_salary_product = recommend_salary.financial_products.split(',')
    recommend_money_product = recommend_money.financial_products.split(',')

    data = {
        'recommend_salary' : recommend_salary_product,
        'recommend_money' : recommend_money_product,
        }

    return Response(data, status=status.HTTP_200_OK)
    
    # print('유사 연봉 : ', recommend_salary_product)
    # print('유사 자산 : ', recommend_money_product[1])
    # return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def test(request, fin_prdt_cd):
    deposit = DepositProduct.objects.filter(fin_prdt_cd=fin_prdt_cd)

    if len(deposit) != 0:
        serializer = DepositProductDetailSerializer(deposit[0])
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    else:
        saving = SavingProduct.objects.filter(fin_prdt_cd=fin_prdt_cd)[0]
        serializer = SavingProductDetailSerializer(saving)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        