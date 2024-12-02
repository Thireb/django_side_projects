from django.contrib import admin
from .models import PagesModel
# Register your models here.


class PageAdminUpdate(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name','date',)
    search_fields = ('name',)
admin.site.register(PagesModel,PageAdminUpdate)
