from django.urls import path

from message import views


app_name='comment'
urlpatterns = [
    path('comment', views.ComentarioListView.as_view(), name='comment-list'),
    path('comment/create/', views.ComentarioCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/detail', views.ComentarioDetailView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/update', views.ComentarioUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', views.ComentarioDeleteView.as_view(), name='comment-delete'),
]
