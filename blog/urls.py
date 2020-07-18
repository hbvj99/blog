from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('post/<slug:title>/', views.post_detail, name='post_detail')
]
