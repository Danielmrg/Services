from django_filters import CharFilter
import django_filters
from .models import *

class ReqFilter(django_filters.FilterSet):
    title=CharFilter(field_name='title',lookup_expr='icontains')
    class Meta:
        model = Request_srv
        fields= ['title']

class CatFilter(django_filters.FilterSet):
    hashtag=CharFilter(field_name='hashtag',lookup_expr='icontains')
    class Meta:
        model = Request_srv
        fields= ['hashtag']