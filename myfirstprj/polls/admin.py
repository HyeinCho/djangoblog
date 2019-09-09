from django.contrib import admin

from .models import Question    #Question에만 접근이 됨.Choice에는 접근 불가
from polls.models import Choice

admin.site.register(Question)

admin.site.register(Choice)