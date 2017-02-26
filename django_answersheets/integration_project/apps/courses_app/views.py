from django.shortcuts import render, redirect
from .models import Course, Description
from ..lr_app.models import User
# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
        'descriptons': Description.objects.all(),
        'users': User.objects.all(),
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    descripton = Description.objects.create(content=request.POST['content'])
    Course.objects.create(name = request.POST['name'], descripton = descripton)
    return redirect('courses:index')

def add_users_to_courses(request):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    course.users.add(user)
    return redirect('courses:index')

def descripton_delete(request, descripton_id):
    Description.objects.filter(id = descripton_id).delete()
    return redirect('courses:index')
