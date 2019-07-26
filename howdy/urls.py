from django.urls import path
from django.conf.urls import url
from howdy import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view()),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.ProfilePageView.as_view(), name='profile'),
    path('signup/', views.signup, name='signup'),
    path('import/', views.simple_upload),
    path('list/', views.list),
    path('books/<int:book_id>/', views.detail, name='detail'),
    url(r'^displaybooks/$', views.displaybooks, name='displaybooks'),
]
