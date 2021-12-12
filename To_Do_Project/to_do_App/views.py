from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from to_do_App.forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from to_do_App.models import Tasks
from to_do_App.forms import TaskForm


# Create your views here.


def homepage_view(request):
    return render(request, 'to_do_App/homepage.html')

def sign_up_view(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/') 

    return render(request, 'registration/sign_up.html', context={'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request.session['username'] = username
#             return render(request, 'to_do_App/tasks_template.html', context={'username':username})
#         else:
#             return HttpResponse('Invalid user !!!')
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request, 'registration/login.html', context={'form':form})

@login_required
def ongoing_tasks_view(request):
    username = request.user.username
    #print(username)
    try:
        tasks = Tasks.objects.filter(username=username)
    except Tasks.DoesNotExist:
        tasks = None
    return render(request, 'to_do_App/ongoing_tasks.html', {'tasks':tasks})

@login_required
def upcoming_tasks_view(request):
    #username = request.session.get('username')
    return render(request, 'to_do_App/upcoming_tasks.html')

@login_required
def completed_tasks_view(request):
    #username = request.session.get('username')
    form = TaskForm()
    return render(request, 'to_do_App/completed_tasks.html', context={'form':form})

@login_required
def tasks_history_view(request):
    #username = request.session.get('username')
    form = TaskForm()
    return render(request, 'to_do_App/tasks_history.html', context={'form':form})

@login_required
def new_tasks_view(request):
    #username = request.session.get('username')
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save(commit=False)
            #form.username = request.user.username
            #print(request.user.username)
            form.save(commit=True)
            return render(request, 'to_do_App/new_tasks.html', context={'title': request.POST['title'],'added': True})
    return render(request, 'to_do_App/new_tasks.html', {'added': False})

