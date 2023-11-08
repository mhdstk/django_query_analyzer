from django.urls import path
from . import views

urlpatterns = [
    path('query-analyzer/', views.query_analyzer_list, name='query_analyzer_list'),
]
