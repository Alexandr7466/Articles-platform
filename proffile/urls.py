from django.contrib import admin
from . import views
from django.urls import include, path

app_name = 'proffile'

urlpatterns = [
    path ('', views.profile_page, name='profile_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('log_in/', views.log_in, name='log_in'),
    path('profile_page_of_someone/<int:user_id>/', views.profile_page_of_someone, name='profile_page_of_someone'),
    path('menu/', views.menu, name='menu'),
]
