from django.urls import path, include
from .views import (
    UserModelListCreateView,
    ComeChechingModelListCreateView,
    GoneChechingModelListCreateView
)

urlpatterns = [
    path('users/', UserModelListCreateView.as_view(), name='user-list-create'),
    path('come/', ComeChechingModelListCreateView.as_view(), name='come-keldi'),
    path('gone/', GoneChechingModelListCreateView.as_view(), name='gone-ketdi'),
]