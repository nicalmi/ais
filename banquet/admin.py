from django.contrib import admin
from .models import Banquet, Participant, Invitation


admin.site.register(Banquet)
#admin.site.register(DietaryPreference)
admin.site.register(Participant)
admin.site.register(Invitation)
