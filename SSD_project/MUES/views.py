from django.shortcuts import render
from MUES.models import Tasks,Users,Videos

# Create your views here.

def index(request):
    return render(request,"MUES/index.html")

def dashboard(request):
    tasks = Tasks.objects.values()
    users = Users.objects.all()
    data = {"tasks":tasks, "users":users}

    if request.method == 'GET':
        return render(request,"MUES/dashboard.html",data)
    else:
        name = request.POST.get('username','default')
        age = request.POST.get('userage','default')
        gender = request.POST.get('gender','default')
        tasks = request.POST.getlist('tasks','default')
        # tasksdb = Tasks.objects.filter(id__in=tasks)
        user = Users(name=name,age=age,gender=gender)
        user.save()
        user.tasks.add(*tasks)
        return render(request,"MUES/dashboard.html",data)

def recording(request):
    tasks = Tasks.objects.values()
    users = Users.objects.all()
    data = {"tasks":tasks, "users":users}

    if request.method == 'GET':
        return render(request,"MUES/testing.html",data)
    else:
        # name = request.POST.get('username','default')
        # age = request.POST.get('userage','default')
        # gender = request.POST.get('gender','default')
        # tasks = request.POST.getlist('tasks','default')
        # # tasksdb = Tasks.objects.filter(id__in=tasks)
        # user = Users(name=name,age=age,gender=gender)
        # user.save()
        # user.tasks.add(*tasks)
        return render(request,"MUES/dashboard.html",data)

def testing(request):
    tasks = Tasks.objects.values()
    users = Users.objects.all()
    data = {"tasks":tasks, "users":users}

    if request.method == 'GET':
        return render(request,"MUES/testing.html",data)
    else:
        # name = request.POST.get('username','default')
        # age = request.POST.get('userage','default')
        # gender = request.POST.get('gender','default')
        # tasks = request.POST.getlist('tasks','default')
        # # tasksdb = Tasks.objects.filter(id__in=tasks)
        # user = Users(name=name,age=age,gender=gender)
        # user.save()
        # user.tasks.add(*tasks)
        return render(request,"MUES/dashboard.html",data)
