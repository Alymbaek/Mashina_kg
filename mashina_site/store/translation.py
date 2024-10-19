from .models import Car, Model
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('the_body', 'colour', 'engine',
              'box_ru',     'drive_ru','rudder_ru', 'condition',
              'customs', 'exchange', 'region_city_of_ale',
              'accounting', 'other', 'text',)

