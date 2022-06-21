from django.urls import path

from rate import views


app_name='rate'
urlpatterns = [
    path('rate', views.BookToRateListView.as_view(), name='rate-list'),
    path('rate/add/', views.BookToRateCreateView.as_view(), name='rate-add'),
    path('rate/<int:pk>/detail', views.BookToRateDetailView.as_view(), name='rate-detail'),
    path('rate/<int:pk>/update', views.BookToRateUpdateView.as_view(), name='rate-update'),
    path('rate/<int:pk>/delete', views.BookToRateDeleteView.as_view(), name='rate-delete'),
]
