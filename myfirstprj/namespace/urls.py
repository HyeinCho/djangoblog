from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from namespace import views

app_name = "namespace"

urlpatterns = [
    path('main', views.index, name='index'),
    path('lotto', views.lotto, name='lotto'),
    path('naver', views.naver, name='naver'),
    path('daum', views.daum, name='daum'),
    path('lotto_mv',views.lotto_mv, name="lotto_mv")
]