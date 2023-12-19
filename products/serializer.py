from rest_framework import serializers
from .models import Product
from .models import Subcatergory
from .models import Subproduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'productName']

class SubCatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcatergory
        fields = ['productId', 'subCategoryId', 'subCategoryName']

class SubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subproduct
        fields = ['subCategoryId', 'subProductId', 'subProductName']