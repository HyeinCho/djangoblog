"""myfirstprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  #polls.urls 상대경로 (파이썬은 /,\ 대신 .을 사용)
    path('namespace/', include('namespace.urls')),
]

'''
myfirstprj -> polls
1차 url        2차 url

http://127.0.0.1:8000/polls        /main
                    (어플리케이션)    (기능)
'''