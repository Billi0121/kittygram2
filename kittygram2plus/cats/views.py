from rest_framework import viewsets
from .models import Achievement, Cat, User
from .serializers import AchievementSerializer, CatSerializer, UserSerializer, CatListSerializer
from .permissions import *
from rest_framework.permissions import *
from .throttling import *
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.pagination import LimitOffsetPagination
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,) 
    throttle_classes = (LowRequestRateThrottle, ScopedRateThrottle)
    throttle_scope = 'low_request'
    pagination_class = CatsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('name', 'color')
    # Определим, что значение параметра search должно быть началом искомой строки
    search_fields = ('^name', 'color', 'achievements__name',)
    ordering = ('birth_year')

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CatListSerializer
    #     else:
    #         return super().get_serializer_class()
        
    def get_permissions(self):
    # Если в GET-запросе требуется получить информацию об объекте
        if self.action == 'retrieve':
        # Вернем обновленный перечень используемых пермишенов
            return (ReadOnly(),)
    # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
        return super().get_permissions() 

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = LimitOffsetPagination