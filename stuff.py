import numpy as np
from sklearn.neighbors import NearestNeighbors
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsertempSerializer
import json

class UserProfileAPIView(APIView):
    def get(self, request, username):
        user_profile_view = UserProfileAPIView()
        userdata = user_profile_view.recommend_products(username)
        serializer = UsertempSerializer(userdata)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def recommend_products(self, username):
        # Django User 모델 가져오기
        User = get_user_model()
        try:
            # 사용자 정보 가져오기
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print(f"사용자 '{username}'를 찾을 수 없습니다.")
            return []

        user_data = np.array([[user.age, user.money, user.salary]])
        user_data = user_data.reshape(1, -1)

        with open("../final-pjt-back/algo/user_data.json", "r", encoding='UTF8') as f:
            data = json.load(f)
        all_users = data
        all_users_data = np.array([[u['fields']['age'], u['fields']['money'], u['fields']['salary']] for u in all_users])

        # KNN 모델 훈련
        knn_model = NearestNeighbors(n_neighbors=3)
        knn_model.fit(all_users_data)

        # 가장 가까운 이웃 찾기
        _, indices = knn_model.kneighbors(user_data)
        nearest_neighbors_data = all_users_data[indices[0]]

        # 추천 상품 코드 수집
        recommended_products = []
        for neighbor_data in nearest_neighbors_data:
            # neighbor_data의 age, money, salary 값에 따라 financial_products 가져오기
            neighbor_age, neighbor_money, neighbor_salary = neighbor_data[0], neighbor_data[1], neighbor_data[2]
            for user_entry in all_users:
                if (
                    user_entry['fields']['age'] == neighbor_age
                    and user_entry['fields']['money'] == neighbor_money
                    and user_entry['fields']['salary'] == neighbor_salary
                ):
                    recommended_products.extend(user_entry['fields']['financial_products'].split(' '))

        # 중복 상품 제거
        recommended_products = list(set(recommended_products))

        return {
            "username": user.username,
            "age": user.age,
            "money": user.money,
            "salary": user.salary,
            "recommendations": recommended_products
        }