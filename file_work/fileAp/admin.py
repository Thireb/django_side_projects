from django.contrib import admin
from .models import QuoteModel
# Register your models here.

class MyQuoteAdmin(admin.ModelAdmin):
    '''Admin View for Quote'''

    list_display = ('name','jawab','money','submitted',)
    list_filter = ('submitted','jawab',)
    
    readonly_fields = ('submitted',)
    search_fields = ('name','username',)
    fieldsets = (
        (None, {
            'fields': (
                'name','email','description',
            ),
        }),
        (
            'Response', {
                'classes':('collapse',),
                'fields': (
                    'jawab','money',
                )
            }),
        (
            'Remaining Data', {
                'classes' : ('collapse',),
                'fields' : (
                    'submitted', 'jobfile','username',
                )
            }),   
    )

admin.site.register(QuoteModel, MyQuoteAdmin)