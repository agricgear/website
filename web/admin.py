
from django.contrib import admin
from models import Contact

class ContactAdmin(admin.ModelAdmin): 
    list_filter = ('date')
    list_display = ('date', 'name', 'email', 'phone')

admin.site.register(Work, WorkAdmin)
