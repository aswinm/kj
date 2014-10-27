from django.contrib import admin
from products.models import Company,Product,ItemType

class CompanyAdmin(admin.ModelAdmin):
    pass

class ProdAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product,ProdAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(ItemType,ItemAdmin)

# Register your models here.
