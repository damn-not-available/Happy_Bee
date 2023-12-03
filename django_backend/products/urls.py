from django.urls import path
from products import views


urlpatterns = [
    path('save_products/', views.save_products),
    path('deposits/', views.deposits),
    path('savings/', views.savings),
    path('deposit_options_all/', views.deposit_options_all),
    path('deposit_options/<deposit_pk>/', views.deposit_options),
    path('saving_options_all/', views.saving_options_all),
    # path('saving_options/<deposit_pk>/', views.saving_options),
    path('deposits/<deposit_pk>/', views.deposit_detail),
    path('savings/<saving_pk>/', views.saving_detail),
    path('deposit_general_recommendation/', views.deposit_general_recommendation),
    path('random_deposit/', views.random_deposit),
    path('saving_general_recommendation/', views.saving_general_recommendation),
    path('random_saving/', views.random_saving),
    path('deposit_get_classified/', views.deposit_get_classified),
    path('saving_get_classified/', views.saving_get_classified),
    path('personal_recommend/', views.personal_recommend),
    path('test/<str:fin_prdt_cd>/', views.test),
]
