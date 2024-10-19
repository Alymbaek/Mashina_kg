from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(UserProfile)
admin.site.register(Marka)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(CarPhotos)
admin.site.register(Cart)
admin.site.register(Review)
