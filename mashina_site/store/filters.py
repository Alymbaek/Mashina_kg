from django_filters import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'model': ['exact'],
            'marka': ['exact'],
            'year': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }
