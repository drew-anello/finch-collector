from django.urls import path
from . import views

urlpatterns = [  # we will define all app-level urls in this list
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finch, name='index'),
    # NEW ROUTE BELOW!!!
    path('finch/<int:finch_id>/', views.finch_detail, name='detail'),

    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
    path('birdhouse/', views.BirdhouseList.as_view(), name='birdhouse_index'),
    path('birdhouse/<int:pk>/', views.BirdhouseDetail.as_view(),
         name='birdhouse_detail'),
    path('birdhouse/create/', views.BirdhouseCreate.as_view(),
         name='birdhouse_create'),
    path('birdhouse/<int:pk>/update/', views.BirdhouseUpdate.as_view(),
         name='birdhouse_update'),
    path('birdhouse/<int:pk>/delete/', views.BirdhouseDelete.as_view(),
         name='birdhouse_delete'),
    path('finch/<int:finch_id>/assoc_birdhouse/<int:birdhouse_id>/',
         views.assoc_birdhouse, name='assoc_birdhouse'),
]
