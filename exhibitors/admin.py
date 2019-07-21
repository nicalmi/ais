from django.contrib import admin
from django.http import HttpResponse

from orders.models import Order, Product
from .models import *


@admin.register(Exhibitor)
class ExhibitorAdmin(admin.ModelAdmin):
	search_fields = ['company__name']
	ordering = ['-fair__year', 'company']
	list_filter = ['fair']

@admin.register(CatalogueIndustry)
class CatalogueIndustryAdmin(admin.ModelAdmin):
	list_display = ('industry', 'include_in_form')
	list_filter = ['include_in_form']
	ordering = ['industry']

@admin.register(CatalogueValue)
class CatalogueValueAdmin(admin.ModelAdmin):
	list_display = ('value', 'include_in_form')
	list_filter = ['include_in_form']
	ordering = ['value']

@admin.register(CatalogueEmployment)
class CatalogueEmploymentAdmin(admin.ModelAdmin):
	list_display = ('employment', 'include_in_form')
	list_filter = ['include_in_form']
	ordering = ['employment']

@admin.register(CatalogueLocation)
class CatalogueLocationAdmin(admin.ModelAdmin):
	list_display = ('location', 'include_in_form')
	list_filter = ['include_in_form']
	ordering = ['location']

@admin.register(CatalogueBenefit)
class CatalogueBenefitAdmin(admin.ModelAdmin):
	list_display = ('benefit', 'include_in_form')
	list_filter = ['include_in_form']
	ordering = ['benefit']

admin.site.register(Location)
admin.site.register(Booth)
admin.site.register(ExhibitorInBooth)
