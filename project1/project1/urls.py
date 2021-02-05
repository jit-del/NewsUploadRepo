from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('news_upload/', views.news_upload, name="news_upload"),
    path('news_show/', views.news_show, name="news_show"),
]
