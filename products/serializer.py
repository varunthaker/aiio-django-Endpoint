from rest_framework import serializers
from .models import Product
from .models import Subcatergory
from .models import Subproduct

class ProductSerializer(serializers.ModelSerializer):
    productId = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Product
        fields = ['productId', 'productName']

class SubCatagorySerializer(serializers.ModelSerializer):
    subCategoryId = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Subcatergory
        fields = ['subCategoryId', 'productId', 'subCategoryName']

class SubProductSerializer(serializers.ModelSerializer):
    subProductId = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Subproduct
        fields = ['subProductId', 'subCategoryId', 'subProductName']