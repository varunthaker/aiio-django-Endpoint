from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)

class Subcatergory(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    subCategoryName = models.CharField(max_length = 200)

class Subproduct(models.Model):
    subCategoryId = models.ForeignKey(Subcatergory, on_delete=models.CASCADE)
    subProductName = models.CharField(max_length = 200)
