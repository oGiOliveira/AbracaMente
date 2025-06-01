from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.connect, name='connect'),
    path('login/', views.login_view, name='login'),
] 