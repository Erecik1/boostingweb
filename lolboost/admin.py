from lolboost.models import Order
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from lolboost.models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display =  ('user','time_created','booster','status')
    search_fields = ('user','booster', 'status')
    readonly_fields = ('user','booster', 'status')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Order, OrderAdmin)
admin.site.register(WinBoosting)
admin.site.register(PlacementBoosting)
admin.site.register(DivisionBoosting)
