from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        # print('html post')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        age = request.POST.get('age')
        usr = Buyer.objects.filter(name = username)
        if usr:
            return HttpResponse("Пользователь с таким именем уже существует")
        else:
            Buyer.objects.create(name = username, age = age, balance = 0)
            return HttpResponse(f'Приветствуем {username}!')

    info['formtype'] = 'html'
    return render(request,'registration_page.html', context= info)
# Create your views here.
def sign_up_by_django(request):
    info = {}
    err = []
    if request.method == 'POST':
        form = UserRegister(request.POST)
        # print('django post')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            usr = Buyer.objects.filter(name=username)
            if usr:
                return HttpResponse("Пользователь с таким именем уже существует")
            else:
                Buyer.objects.create(name=username, age=age, balance=0)

    else:
        # print('django non post')
        form = UserRegister()

    info['form'] = form
    info['formtype'] = 'django'

    return render(request,'registration_page.html', context=info)

def main(request):
    context = {'pagename': 'Главная страница'}
    return render(request,"mainpage.html", context)
def price(request):
    games=Game.objects.all()
    context = {'games': games, 'pagename': 'Игры'}
    return render(request,"price.html", context)
def card(request):
    context = {'pagename': 'Корзина'}
    return render(request,"card.html", context)

# Create your views here.
