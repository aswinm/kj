from django.contrib import admin
from products.models import Company,Product

class CompanyAdmin(admin.ModelAdmin):
    pass

class ProdAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product,ProdAdmin)
admin.site.register(Company,CompanyAdmin)

# Register your models here.
