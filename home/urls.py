from django.urls import path

from home import views


app_name='home'
urlpatterns = [
    path('', views.CatalogueBookListView.as_view(), name='home-list'),
    path('add/', views.CatalogueBookCreateView.as_view(), name='home-add'),
    path('<int:pk>/detail', views.CatalogueBookDetailView.as_view(), name='home-detail'),
    path('<int:pk>/update', views.CatalogueBookUpdateView.as_view(), name='home-update'),
    path('<int:pk>/delete', views.CatalogueBookDeleteView.as_view(), name='home-delete'),
    path('search', views.search, name='search'),
    
]
