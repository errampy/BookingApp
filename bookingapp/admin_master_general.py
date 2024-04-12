from django.contrib import admin
from .models_master_general import *

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Define ModelResource classes for each model
class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        import_id_fields = ['code']  # Specifies the field to use as the identifier during import

class CountyOrStateResource(resources.ModelResource):
    class Meta:
        model = CountyOrState
        import_id_fields = ['code']  # Specifies the field to use as the identifier during import

class CityResource(resources.ModelResource):
    class Meta:
        model = City
        import_id_fields = ['code']  # Specifies the field to use as the identifier during import

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'created_at', 'updated_at')
    resource_class = CountryResource

@admin.register(CountyOrState)
class CountyOrStateAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'county', 'created_at', 'updated_at')
    resource_class = CountyOrStateResource

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'country', 'county_or_state', 'created_at', 'updated_at')
    resource_class = CityResource
