from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
users = ['user1','user2']
def user_valid(**kwargs):
    err = []
    if kwargs['username'] in users:
        err.append('Пользователь уже существует')
    if kwargs['password']!=kwargs['repeat_password']:
        err.append('Пароли не совпадают')
    if int(kwargs['age']) < 18:
        err.append('Вы должны быть старше 18')
    return err

def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        # print('html post')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        age = request.POST.get('age')
        err = user_valid(username=username,repeat_password=repeat_password,password=password,age=age)
        info['len_error'] = len(err)
        if len(err) == 0:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}!')
        else:
            info['error'] = err
            return HttpResponse(err)
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
            err = user_valid(username=username, repeat_password=repeat_password, password=password, age=age)
            if len(err) == 0:
                users.append(username)
                return HttpResponse(f'Приветствуем {username}!')
            else:
                info['error'] = err
                return HttpResponse(err)
    else:
        # print('django non post')
        form = UserRegister()

    info['form'] = form
    info['formtype'] = 'django'
    info['len_error'] = len(err)
    return render(request,'registration_page.html', context=info)

def main(request):
    context = {'pagename': 'Главная страница'}
    return render(request,"mainpage.html", context)
def price(request):
    context = {'games': ['Atomic Heart', "Cyberpunk 2077",'Monopolya'], 'pagename': 'Игры'}
    return render(request,"price.html", context)
def card(request):
    context = {'pagename': 'Корзина'}
    return render(request,"card.html", context)

# Create your views here.
