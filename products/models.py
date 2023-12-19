from django.db import models

class Product(models.Model):
    productId = models.IntegerField()
    productName = models.CharField(max_length=200)

class Subcatergory(models.Model):
    productId = models.IntegerField()
    subCategoryId = models.IntegerField()
    subCategoryName = models.CharField(max_length = 200)

class Subproduct(models.Model):
    subCategoryId = models.IntegerField()
    subProductId = models.IntegerField()
    subProductName = models.CharField(max_length = 200)
