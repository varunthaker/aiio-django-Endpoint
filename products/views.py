from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
    serializer = ProductSerializer(products, many =True)
    return JsonResponse({'products':serializer.data})

@api_view(['GET', 'POST'])
def subCatagory_list(request):
    if request.method == "GET":
        subCatagories = Subcatergory.objects.all()
        serializer = SubCatagorySerializer(subCatagories, many = True)
        return JsonResponse({'subcatagories':serializer.data})
    if request.method == "POST":
        serializer = SubCatagorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def subProduct_list(request):
    
    if request.method == "GET":
        subProducts = Subproduct.objects.all()
        serializer = SubProductSerializer(subProducts, many = True)
        return JsonResponse({'subproducts':serializer.data})
    
    if request.method == "POST":
        serializer = SubProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)