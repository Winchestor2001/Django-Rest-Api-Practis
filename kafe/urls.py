from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'food_category', views.FoodCategoriesViewSet)

urlpatterns = [
    path('', include(router.urls))  # http://127.0.0.1:8000/api/v1/food_category/

    # OLD
    # path('food_category/', views.FoodCategoriesViewSet.as_view({"get": "list"})),
    # path('food_category/<int:pk>/', views.FoodCategoriesViewSet.as_view({'put': 'update'})),

    # OLD
    # path('food_category/', views.FoodCategoriesAPIList.as_view()),
    #     path('food_category/<int:pk>/', views.FoodCategoriesAPIUpdate.as_view()),
    #     path('food_category_detail/<int:pk>/', views.FoodCategoriesAPIDetailView.as_view())
]
