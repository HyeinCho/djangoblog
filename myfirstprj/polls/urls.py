from django.urls import path
from . import views

# app_name 변수는 주소에 라벨링을 합니다.
app_name = "polls"

urlpatterns = [
        path('main', views.index, name='index'),    # name: 별명 (main의 절대경로를 index라고 부르자!)
        path('test', views.test, name='test'),
        path('getform',views.getform, name='getform'),
        path('get', views.get, name='get'),
        path('nameform', views.nameform, name='nameform'),
        path('name',views.get_name, name='name'),
        path('<int:c>/ctof', views.ctof),
        path('<int:cm>/<int:kg>/bmi', views.BMI),
        path('<int:number>/content', views.get_number),  #가변(우아한) url. number: 가변, content: 고정
        path('<int:age>/check', views.get_adult_result),
        path('<int:num1>/<int:num2>/two', views.get_two),
        path('<str:name>/name', views.get_name2),   
        #실수(float)입력은 바로 안되기 때문에 문자열(str)로 받아서 형변환하기
        
        #<str:변수명>을 이용하면 문자열을 입력받을 수 있는데 문자열에는 반드시 문자만 들어가는게 아니라 .를  포함한 숫자도 넣을 수 있음
        #따라서 .를 포함한 숫자가 들어왔을 때 float()을 이용해 강제 형변환을 하면 실수 입력이 가능함.

        path('<str:won>/<str:rate>/exchange', views.exchange_won),
        path('qtest', views.qtest),
        path('<int:age>/bus', views.buscost),
        path('<int:id>', views.detail, name='detail'),
        path('<int:question_id>/results/', views.results, name='results'),
        path('<int:question_id>/vote/',views.vote, name='vote'),    #~~/polls/1/vote/?choice=2
    ]