from django.contrib import admin
from .models import Record
# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('Quantity','Date_of_Current')
    ordering = ('Date_of_Current',)
    fieldsets = (
        (None, {
            'fields': (
                'Quantity', 'Date_of_Current'
            ),
        }),
    )



admin.site.register(Record,RecordAdmin)