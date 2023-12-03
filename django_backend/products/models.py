from django.db import models


# Create your models here.
class CreatedTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class DepositProduct(models.Model):
    # 금융상품코드
    fin_prdt_cd = models.TextField(null=True)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융상품명
    fin_prdt_nm = models.TextField(null=True)
    # 가입제한
    join_deny = models.IntegerField(null=True)
    # 가입대상
    join_member = models.TextField(null=True)
    # 가입방법
    join_way = models.TextField(null=True)
    # 우대조건
    spcl_cnd = models.TextField(null=True)
    # 최고한도
    max_limit = models.IntegerField(null=True)


class SavingProduct(models.Model):
    # 금융상품코드
    fin_prdt_cd = models.TextField(null=True)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융상품명
    fin_prdt_nm = models.TextField(null=True)
    # 가입제한
    join_deny = models.IntegerField(null=True)
    # 가입대상
    join_member = models.TextField(null=True)
    # 가입방법
    join_way = models.TextField(null=True)
    # 우대조건
    spcl_cnd = models.TextField(null=True)
    # 최고한도
    max_limit = models.IntegerField(null=True)


class DepositOptions(models.Model):
    # 외래키... 필드명 잘못 만듬
    fin_prdt_cd = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    # 저축금리유형
    intr_rate_type = models.TextField(null=True)
    # 저축금리유형명
    intr_rate_type_nm = models.TextField(null=True)
    # 저축기간(개월)
    save_trm = models.IntegerField(null=True)
    # 저축금리
    intr_rate = models.FloatField(null=True)
    # 최고우대금리
    intr_rate2 = models.FloatField(null=True)


class SavingOptions(models.Model):
    # 외래키... 필드명 잘못 만듬
    fin_prdt_cd = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    # 저축금리유형
    intr_rate_type = models.TextField(null=True)
    # 저축금리유형명
    intr_rate_type_nm = models.TextField(null=True)
    # 적립유형
    rsrv_type = models.TextField(null=True)
    # 적립유형명
    rsrv_type_nm = models.TextField(null=True)
    # 저축기간(개월)
    save_trm = models.IntegerField(null=True)
    # 저축금리
    intr_rate = models.FloatField(null=True)
    # 최고우대금리
    intr_rate2 = models.FloatField(null=True)