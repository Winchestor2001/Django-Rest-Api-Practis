from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import FoodCategoriesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class FoodCategoriesViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategoriesSerializer

# OLD
# class FoodCategoriesAPIList(generics.ListCreateAPIView):
#     queryset = FoodCategory.objects.all()
#     serializer_class = FoodCategoriesSerializer
#
#
# class FoodCategoriesAPIUpdate(generics.UpdateAPIView):
#     queryset = FoodCategory.objects.all()
#     serializer_class = FoodCategoriesSerializer
#
#
# class FoodCategoriesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FoodCategory.objects.all()
#     serializer_class = FoodCategoriesSerializer

# OLD
# class FoodCategoriesAPI(APIView):
#     def get(self, request):
#         food_categories_list = FoodCategory.objects.all()
#         return Response({"food_category": FoodCategoriesSerializer(food_categories_list, many=True).data})
#
#     def post(self, request):
#         serializer = FoodCategoriesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"new_category": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = FoodCategory.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object dose not exists"})
#
#         serializer = FoodCategoriesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"update_category": serializer.data})
#
#     def delete(self, request, pk):
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             food_cat = FoodCategory.objects.get(pk=pk)
#             food_cat.delete()
#         except:
#             return Response({"error": "Object dose not exists"})
#
#         return Response({"delete_category": f"category deleted {pk}"})
