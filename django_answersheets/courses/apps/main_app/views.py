from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
        'descriptons': Description.objects.all(),
    }
    return render(request, 'main_app/index.html', context)

def create(request):
    descripton = Description.objects.create(content=request.POST['content'])
    Course.objects.create(name = request.POST['name'], descripton = descripton)
    return redirect('courses:index')

def course_delete(request, course_id):
    Course.objects.filter(descripton_id = course_id).delete()
    return redirect('courses:index')

def descripton_delete(request, descripton_id):
    Description.objects.filter(id = descripton_id).delete()
    return redirect('courses:index')

def show_course(request, course_id):
    print 'in show'
    context = {
        'course': course_id
    }
    return render(request, 'main_app/show.html', context)

def check(request):
    print 'in check'
    return redirect('courses:show_course', course_id=2)
