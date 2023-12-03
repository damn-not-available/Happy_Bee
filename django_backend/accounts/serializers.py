from django.contrib.auth import get_user_model
from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
# from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=30
    )
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    address = serializers.CharField(required=False)
    risk_aversion = serializers.IntegerField(required=False)
    profile_image = serializers.ImageField(required=False)    

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username'),
            'nickname': self.validated_data.get('nickname'),
            'password1': self.validated_data.get('password1'),
            'age': self.validated_data.get('age'),
            'money': self.validated_data.get('money'),
            'salary': self.validated_data.get('salary'),
            'financial_products': self.validated_data.get('financial_products'),
            'address': self.validated_data.get('address'),
            'risk_aversion': self.validated_data.get('risk_aversion'),
            'profile_image': self.validated_data.get('profile_image'),
        }
    

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    # profile = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        exclude = ('password', 'is_staff', 'is_active', )