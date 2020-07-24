from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('post/add/', views.new_post, name='new_post'),
    path('post/<slug:title>/', views.post_detail, name='post_detail'),
    path('post/<slug:title>/edit/', views.post_update, name='post_update'),
    path('post/<slug:title>/delete/', views.post_delete, name='post_delete'),

]
