from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Account, Booster

class AccountAdmin(UserAdmin):
    list_display =  ('email', 'username','date_joined','last_login','is_admin','is_staff', 'is_booster')
    search_fields = ('email','username')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class BoosterAdmin(admin.ModelAdmin):
    list_display =  ('account','rank','reviews','orders_done','languages')
    search_fields = ('account',)
    readonly_fields = ('orders_done','status')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Booster, BoosterAdmin)