from django.http import JsonResponse
from .models import Product
from .models import Subcatergory
from .models import Subproduct
from .serializer import ProductSerializer
from .serializer import SubCatagorySerializer
from .serializer import SubProductSerializer

def product_list(request):
    #get all proucts
    #serialize (frpm Python to JSON format)
    #return JSON

    products = Product.objects.all()
    serialiser = ProductSerializer(products, many =True)
    return JsonResponse(serialiser.data, safe = False)

def subCatagory_list(request):
    subCatagories = Subcatergory.objects.all()
    serialiser = SubCatagorySerializer(subCatagories, many = True)
    return JsonResponse(serialiser.data, safe = False)

def subProduct_list(request):
    subCatagories = Subproduct.objects.all()
    serialiser = SubProductSerializer(subCatagories, many = True)
    return JsonResponse(serialiser.data, safe = False)