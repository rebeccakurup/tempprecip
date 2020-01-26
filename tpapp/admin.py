# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from tpapp.models import AppData

@admin.register(AppData)
class TpAppAdmin(ImportExportModelAdmin):
    pass