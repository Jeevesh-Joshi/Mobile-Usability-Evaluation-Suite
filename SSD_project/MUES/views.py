from django.shortcuts import render
from MUES.models import Tasks,Users,Videos,Projects

# Create your views here.

def index(request):
    return render(request,"MUES/index.html")

def user_register(request):
    tasks = Tasks.objects.values()
    projects = Projects.objects.values()
    users = Users.objects.all()
    data = {"tasks":tasks, "users":users, "projects":projects}

    if request.method == 'GET':
        return render(request,"MUES/user_register.html",data)
    else:
        name = request.POST.get('username','default')
        proj_id = request.POST.get('projid','default')
        age = request.POST.get('userage','default')
        gender = request.POST.get('gender','default')
        tasks = request.POST.getlist('tasks','default')
        # tasksdb = Tasks.objects.filter(id__in=tasks)
        projobj = Projects.objects.filter(id=proj_id)[0]
        user = Users(name=name,project=projobj,age=age,gender=gender)
        user.save()
        user.tasks.add(*tasks)
        user.save()
        return render(request,"MUES/user_register.html",data)

def load_ptasks(request):
    project_id = request.GET.get('project')
    proj = Projects.objects.filter(id=project_id)[0]
    data = {"proj":proj}
    return render(request, 'MUES/load_ptasks.html', data)

def project_register(request):
    if request.method == 'GET':
        return render(request,"MUES/project_register.html")
    else:
        name = request.POST.get('projectname','default')
        desc = request.POST.get('desc','default')
        ptasks = request.POST.get('projtasks','default')

        print(name,desc,ptasks)
        proj = Projects(name=name,description=desc)
        proj.save()

        proj = Projects.objects.filter(name=name)[0]

        tasks_lists = list(ptasks.split(","))
        print(tasks_lists)
        for task in tasks_lists:
            t = Tasks(project=proj,name=task)
            t.save()
        
        tasksdb = Tasks.objects.filter(project__id = proj.id)
        proj.tasks.add(*tasksdb)
        proj.save()
        return render(request,"MUES/project_register.html")

def recording(request):
    tasks = Tasks.objects.values()
    users = Users.objects.all()
    data = {"tasks":tasks, "users":users}

    if request.method == 'GET':
        return render(request,"MUES/recording.html",data)
    else:
        # name = request.POST.get('username','default')
        # age = request.POST.get('userage','default')
        # gender = request.POST.get('gender','default')
        # tasks = request.POST.getlist('tasks','default')
        # # tasksdb = Tasks.objects.filter(id__in=tasks)
        # user = Users(name=name,age=age,gender=gender)
        # user.save()
        # user.tasks.add(*tasks)
        return render(request,"MUES/recording.html",data)

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
        return render(request,"MUES/testing.html",data)
