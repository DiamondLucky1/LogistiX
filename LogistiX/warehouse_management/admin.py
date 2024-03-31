from django.contrib import admin

from .models import *


admin.site.register(Warehouse)
admin.site.register(Category)
admin.site.register(InventoryItem)
admin.site.register(Production)
admin.site.register(StockMovement)


