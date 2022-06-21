from django.urls import path
from about.views import *


app_name='about'
urlpatterns = [
    path('', AboutListView.as_view(), name='about_list'),    
    path('add', AboutCreateView.as_view(), name='about_add'),    
    path('<int:pk>/update', AboutUpdateView.as_view(), name='about_edit'),    
    path('<int:pk>/delete', AboutDeleteView.as_view(), name='about_delete'),    
]
