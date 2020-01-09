from django.contrib import admin
from .models import Chem
from import_export.admin import ImportExportModelAdmin


@admin.register(Chem)
class ViewAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
