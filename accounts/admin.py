
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from accounts.models import Account
from .resources import AccountResource

# Register your models here.

@admin.register(Account)
class edxUserAdmin(ImportExportModelAdmin):
    resource_class = AccountResource
