from django.contrib import admin

# Register your models here.

from farm.models import Owner, Farm


class Owners(admin.ModelAdmin):
    list_display = ('id','name', 'document', 'document_type', 'creation_date', 'last_modification_date', 'is_active')
    list_display_links = ('id','name', 'document', 'document_type', 'last_modification_date', 'is_active')
    search_fields = ('name', 'document', 'is_active',)
    list_per_page = 25
    
admin.site.register(Owner, Owners)


class Farms(admin.ModelAdmin):
    list_display = ('id','name', 'geometry', 'area', 'centro_id', 'creation_date', 'last_modification_date', 'is_active', 'municipio', 'estado', 'owner')
    list_display_links = ('id','name', 'geometry', 'area', 'centro_id', 'last_modification_date', 'is_active', 'municipio', 'estado', 'owner')
    search_fields = ('name',  'area', 'centro_id', 'is_active', 'municipio', 'estado',)
    list_per_page = 25
    
admin.site.register(Farm, Farms)