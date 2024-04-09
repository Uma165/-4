import django_filters
from .models import Cruise, Room


class CruiseFilter(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='rooms__price',
        label='Диапазон цен', distinct=True)
    room_category = django_filters.ChoiceFilter(field_name='rooms__category', distinct=True,
         label='Категория комнат', choices=Room.CATEGORIES)
    cities = django_filters.CharFilter(field_name='cities', lookup_expr='icontains', label='Город')

    class Meta:
        model = Cruise
        fields = ['price_range', 'room_category', 'time', 'cities']
