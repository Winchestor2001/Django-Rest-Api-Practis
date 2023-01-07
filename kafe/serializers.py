from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class FoodCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'

# OLD
# class FoodCategoriesSerializer(serializers.Serializer):
#     food_name = serializers.CharField(max_length=150)
#
#     def create(self, validated_data):
#         return FoodCategory.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.food_name = validated_data.get('food_name', instance.food_name)
#         instance.save()
#         return instance
