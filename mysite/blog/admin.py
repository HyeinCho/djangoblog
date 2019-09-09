from django.contrib import admin
from blog.models import Post

admin.site.register(Post)

'''
*admin 계정 생성
1. cmd
    D:\hidjango\workspace\mysite> dir        #manage.py 있는지 확인
    D:\hidjango\workspace\mysite> python manage.py createsuperuser
2. 입력
    Username (leave blank to user 'kg'): admin
    Email address: admin@admin.com
    Password: python01
'''
