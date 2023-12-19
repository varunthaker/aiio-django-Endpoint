from django.contrib import admin
from .models import Product
from .models import Subcatergory
from .models import Subproduct

admin.site.register(Product)
admin.site.register(Subcatergory)
admin.site.register(Subproduct)