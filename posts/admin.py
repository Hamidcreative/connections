
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from posts.models import Post
from accounts.resources import UpdateResource

# Register your models here.

@admin.register(Post)
class edxUserAdmin(ImportExportModelAdmin):
    resource_class = UpdateResource

