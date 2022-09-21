from rest_framework import serializers
from .models import *



# Serializer
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


#Model Serializer
class ProductInventry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Inventry
        fields = '__all__'

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

#Hyper Link Model Serializer
class Category_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url','name']