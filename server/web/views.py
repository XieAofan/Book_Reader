from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'web/index.html')

def test(request):
    return render(request, 'web/test.html')
@login_required
def reader(request):
    content = request.GET.get('myid',default='1')
    url = request.GET.get('url',default='1')
    name = request.GET.get('n',default='1')
    context = {
        'content':content,
        'url':url,
        'name':name,
    }
    return render(request, 'web/reader.html', context)

def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            # Return an 'invalid login' error message.
            c ={
                'message':'账户或密码错误',
            }
            return render(request, 'web/login.html', c)
    else:
        return render(request, 'web/login.html')

def my_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")