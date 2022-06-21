from django.urls import path

from message import views


app_name='message'
urlpatterns = [
    path('message', views.MessageListView.as_view(), name='message-list'),
    path('message/send/', views.MessageCreateView.as_view(), name='message-add'),
    path('message/<int:pk>/detail', views.MessageDetailView.as_view(), name='message-detail'),
]
