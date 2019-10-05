from rest_framework import serializers
from .models import Product, PhoneUser, Transactions

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ["p_id", "title", "description", "price", "image", "stock"]

class PhoneUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = PhoneUser
		fields = ["phone_number", "otp"]

class TransactionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transactions
		fields = ["trans_id", "fk_p_id", "created_at", "quantity", "fk_phone"]