from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('region/<int:id>', views.region_detail , name = 'region_url'),
    path('region/', views.region, name='region'),
    path('arena/', views.arena, name='arena_url'),
    path('arena/<int:id>', views.arena_detail, name='arena_detail_url'),
    path('trener/', views.trener, name='trener_url'),
    path('trener/<int:id>', views.trener_detail, name='trener_detail_url'),
    path('sport/<int:id>', views.sport_trener, name="sport_trener_url"),
    path('sport/', views.sport_trener ,name="sport_trener")
]

# Slug