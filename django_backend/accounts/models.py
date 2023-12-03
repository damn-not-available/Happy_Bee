from django.db import models
from django.contrib.auth.models import AbstractUser

from allauth.account.adapter import DefaultAccountAdapter

# class Photo(models.Model):
#     user_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

# Create your models here.
class User(AbstractUser):
    # 아이디
    username = models.CharField(max_length=30, unique=True)
    # 이용 금융상품
    financial_products = models.TextField(blank=True, null=True)
    # financial_products = models.ManyToManyField(DepositOptions)
    # financial_products = models.ManyToManyField(SavingOptions)
    # 나이
    age = models.IntegerField(blank=True, null=True)
    # 소지금
    money = models.IntegerField(blank=True, null=True)
    # 연봉
    salary = models.IntegerField(blank=True, null=True)
    # 닉네임
    nickname = models.CharField(max_length=30, blank=True, null=True)
    # 주소
    address = models.TextField(blank=True, null=True)
    # 위험회피성향
    # 1 averse, 2 neutral, 3 favor
    risk_aversion = models.IntegerField(blank=True, null=True)
    # 프로필 이미지
    # profile_image = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='profile_image', blank=True)
    profile_image = models.ImageField(blank=True, null=True)
    
    email = models.EmailField(blank=True, null=True)
    REQUIRED_FIELDS = []

from allauth.account.utils import user_email, user_field, user_username
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = form.data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        financial_product = data.get("financial_products")
        address = data.get("address")
        risk_aversion = data.get("risk_aversion")
        profile_image = data.get("profile.img")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if address:
            address = user.address
        if risk_aversion:
            risk_aversion = user.risk_aversion
        if profile_image:
            profile_image = user.profile_image
        if financial_product:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_product)
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
            self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()

        return user