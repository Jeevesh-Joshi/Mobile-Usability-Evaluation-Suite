from django.shortcuts import render
from django.http import HttpResponse
from MUES.models import Tasks,Users,Videos

# Create your views here.


def index(request):
    # return HttpResponse("Hello inside app")
    return render(request,"MUES/index.html")

def dashboard(request):
    tasks = Tasks.objects.values()
    users = Users.objects.values()
    data = {"tasks":tasks, "users":users}
    print(data)
    if request.method == 'GET':
        return render(request,"MUES/dashboard.html",data)
    else:
        name = request.POST.get('username','default')
        age = request.POST.get('userage','default')
        gender = request.POST.get('gender','default')
        tasks = request.POST.getlist('tasks','default')
        
        tasksdb = Tasks.objects.filter(id__in=tasks)
        user = Users(name=name,age=age,gender=gender)
        user.save()
        user.tasks.add(*tasksdb)
        return render(request,"MUES/dashboard.html",data)
