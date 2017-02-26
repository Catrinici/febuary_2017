from django.shortcuts import render
import time

# Create your views here.
def index(request):
    currentTime = time.localtime()
    context = {
        'currentTime': time.strftime("%H:%M:%S", currentTime)
    }
    return render(request, 'timeApp/index.html', context)
