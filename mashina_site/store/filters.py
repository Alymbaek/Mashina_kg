from django_filters.rest_framework import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'marka': ['exact'],
            'model': ['exact'],
            'year_of_release': ['gt', 'lt'],
            'price_dollars': ['gt', 'lt']
        }

