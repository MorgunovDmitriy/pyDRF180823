from django_filters import rest_framework as filters
import django_filters
from .models import Game, Studio

class GameFilter(filters.FilterSet):
    class Meta:
        model = Game
        fields = ['name']

# class StudioFilter(filters.FilterSet):
#     class Meta:
#         model = Studio
#         fields = ['=name']

class StudioFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Studio
        fields = ['name']