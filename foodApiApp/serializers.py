from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from foodApiApp.models import Administator, Menu, Food, SpecialItem, Customer, Order, OrderItem, Payment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



# class FoodSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Food
#         fields = ['url', 'name', 'price', 'description', 'catagory']

# ModelSerializer


# class CustomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Administator
#         fields = ['name', 'catagory']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name']

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['catagory']

class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialItem
        fields = ['food']