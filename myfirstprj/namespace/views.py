from django.shortcuts import render
import random
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

def index(request):
    print(reverse('namespace:lotto'))   #namespace의 lotto 패턴 주소를 콘솔창에 찍은 것
    print(reverse('polls:test'))    #/polls/test
    print(reverse('polls:results', args=(10,)))     #우아한 url.    /polls/10/results/
    return render(request, 'namespace/index.html')

def lotto(request):
    lottonum = []
    while len(lottonum) != 6:
        number = random.randint(1,45)
        if number not in lottonum:
            lottonum.append(number)
    lottonum.sort()  
    while number in lottonum:
        number = random.randint(1,45)
    return render(request, 'namespace/lotto.html',{"lottonum":lottonum, "number":number})    

def naver(request):
    print("네이버 페이지로 강제 링크됩니다.")
    return HttpResponseRedirect('https://www.naver.com')

def lotto_mv(request):
    print("로또 사이트로 이동하셨습니다")
    return HttpResponseRedirect('/namespace/lotto')

def daum(request):
    print("다음 사이트로 이동하셨습니다")
    return HttpResponseRedirect('https://www.daum.net')