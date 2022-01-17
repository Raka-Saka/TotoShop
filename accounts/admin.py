from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'company_name', 'personal_phone_number',
                    'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'company_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('company_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
