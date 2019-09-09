from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse    #브라우저상에 연결
from polls.models import Question
from django.template.context_processors import request
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

#request는 요청을 받는 변수이기 때문에 무조건 써야함

def index(request):     #장고 쓸 때 함수 내부에 request 반드시 써야함
    latest_question_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html',{"latest_question_list":latest_question_list})

def test(request):
    return render(request, 'polls/test.html')   #render: polls/templates/polls 안에 test.html를 연결해줌(현위치 templates)

def getform(request):
    return render(request, 'polls/getform.html')

def get(request):
    """
    #http://127.0.0.1:8000/polls/get?str1=가나다라&str2=abcd
    '''
    print(request.GET['str1'])  #가나다라 콘솔창에 출력됨
    return HttpResponse("<h1>"+ request.GET['str2'] + "</h1>")  #abcd 브라우저 창에 출력됨
    '''
    #str2에 값을 안넣으면 에러뜸. 즉 요청한걸 안넣으면 에러뜸
    
    #요청한 걸 안넣었을 때 에러 안뜨게 설정하기
    print(request.GET.get('str1'))
    return HttpResponse("<h1>"+ str(request.GET.get('str2')) + "</h1>")
    #http://127.0.0.1:8000/polls/get?str1=장고
    #str2에 안넣었지만 브라우저에는 None으로 나옴
    """
    str1 = request.POST.get('str1')
    str2 = request.POST.get('str2')
    return render(request, 'polls/get.html', {"str1":str1, "str2":str2})  #중요!!!!!!!

def nameform(request):    
    return render(request, 'polls/nameform.html')
    
def get_name(request):
    """
    name = str(request.GET.get('name'))
    return HttpResponse("<h1>사용자의 이름은: " + name + "입니다.</h1>")
    #http://127.0.0.1:8000/polls/name?name=python
    #사용자의 이름은: python입니다.
    """
    name = request.POST.get('name')
    return render(request, 'polls/get_name.html', {'name':name})
    
'''
get방식으로 섭씨 온도를 입력받아 화씨온도로 바꿔주는 프로그램
섭씨=(화씨-32)/1.8
'''
def ctof(request, c):
    '''
    c = int(request.GET.get('cel'))
    f = c * 1.8 + 32
    return HttpResponse("<h1>섭씨온도: " + str(c) + " 화씨온도: " + str(f) + "</h1>")
    #HttpResponse는 문자열에만 응답하기 때문에 모두 문자열로 바꿔줘야함
    #print는 자동으로 문자열로 바꿔줌. 문자열로 바꿀 필요없음
    
    f = c * 1.8 + 32
    return HttpResponse("<h1>섭씨온도: " + str(c) + " 화씨온도: " + str(f) + "</h1>")
    '''
    f = c * 1.8 + 32
    return render(request, 'polls/ctof.html', {"c":c,"f":f})
    
    
'''s
get방식으로 키, 몸무게를 입력받아 BMI지수를 출력하는 프로그램을 만들어보세요
BMI지수 공식: 몸무게(kg) / (키(m) * 키(m))
키는 cm단위로 입력받되 계산시는 m단위로 사용합니다
'''
def BMI(request, cm, kg):
    '''
    h = float(request.GET.get('height')) / 100
    w = float(request.GET.get('weight'))
    bmi = w / (h * h)
    return HttpResponse("<h1>bmi 지수는 " + str(round(bmi, 2)) + "입니다.</h1>")
    
    m = float(cm) / 100
    bmi = kg / (m * m)
    return HttpResponse("<h1>키 : " + str(cm) + "cm, 몸무게: " + str(kg) + "kg일 때  bmi 지수는 " 
                        +  str(round(bmi, 2)) + "입니다.</h1>")
    '''
    m = cm / 100.0
    bmi = kg / (m * m)
    bmi = round(bmi, 2)
    return render(request, 'polls/get_bmi.html', {'cm':cm, 'kg':kg, 'bmi':bmi})

def get_number(request, number):    
    return HttpResponse('<h1>테스트 중입니다.' + str(number) + "</h1>")

def get_adult_result(request, age):
    """
    person = ""
    if age >= 20:
        person = "성인입니다."
    else:
        person = "미성년자입니다."
    return HttpResponse("<h1>" + person + "</h1>")
    """
    """
    if age >= 20:
        return render(request, 'polls/adult_ok.html', {'age':age})
    else:
        return render(request, 'polls/adult_fail.html', {'age':age})
    """
    return render(request, 'polls/adult_check.html', {'age':age})

def get_two(request, num1, num2):
    return HttpResponse("<h1>" + str(num1) + " || " + str(num2) + "</h1>")

def get_name2(request, name):
    return HttpResponse("<h1>당신의 이름은: " + name + "입니다.</h1>")

def exchange_won(request, won, rate):
    dol = float(won) / float(rate)
    return HttpResponse("<h1>원화: " + won + "원, 환율: " +rate +
                        "달러일 때 환전금액: " + str(round(dol,2)) + "달러 입니다.</h1>")

def qtest(request):
    #question_all = Question.objects.all()   #저장된 순서로 모두 꺼내옴
    question_all = Question.objects.order_by('-pk')  #컬럼의 순서대로 정렬되어 꺼내옴
    return render(request, 'polls/question_test.html', {'question_all':question_all})

def buscost(request, age):
    return render(request, 'polls/bus_cost.html', {'age':age})

def detail(request, id):
    # .get(조건)은 결과가 무조건 1개만 나올 때 쓸 수 있습니다.
    #question = Question.objects.get(pk=id)
    question = get_object_or_404(Question, pk=id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
