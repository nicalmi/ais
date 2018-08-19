from django.contrib import admin
from .models import *


class CustomFieldInline(admin.TabularInline):
    model = CustomField


class CustomFieldAnswerInline(admin.TabularInline):
    model = CustomFieldAnswer


class CustomFieldArgumentInline(admin.TabularInline):
    model = CustomFieldArgument


class CustomFieldAdmin(admin.ModelAdmin):
    inlines = [CustomFieldArgumentInline]


class RoleApplicationInline(admin.TabularInline):
    model = RoleApplication


class RecruitmentApplicationAdmin(admin.ModelAdmin):
    inlines = [RoleApplicationInline]

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ['name', 'recruitment_period']
	list_filter = ['recruitment_period']

admin.site.register(RecruitmentPeriod)
admin.site.register(RecruitmentApplication, RecruitmentApplicationAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
admin.site.register(CustomFieldAnswer)
admin.site.register(CustomFieldArgument)
