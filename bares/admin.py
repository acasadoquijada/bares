from django.contrib import admin
from bares.models import *

class AdminBar(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}
    
admin.site.register(Bar,AdminBar)
admin.site.register(Tapa)
