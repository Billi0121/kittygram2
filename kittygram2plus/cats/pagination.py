from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from .models import *
from rest_framework.response import Response

class CatsPagination(pagination.BasePagination):
    # page_size = 2
    def paginate_queryset(self, queryset, request, view=None):
        queryset = Cat.objects.all()
        return queryset
    
    def get_paginated_response(self, data):
        return Response({
            'result': data
        })