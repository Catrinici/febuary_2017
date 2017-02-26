from django.shortcuts import render

# Create your views here.
# This is a controller in the MVC framework structure
ninjas = {
    'donatello': 'donatello.jpg',
    'leonardo': 'leonardo.jpg',
    'michelangelo': 'michelangelo.jpg',
    'raphael': 'raphael.jpg',
}

def index(request):
    return render(request, 'ninjas/index.html')

def show(request):
    context = {
        'ninjas': ninjas,
    }
    return render(request, 'ninjas/show.html', context)

def showOne(request, ninja):
    sendNinga = {}
    if ninja in ninjas:
        sendNinga[ninja] = ninjas[ninja]
    else:
        sendNinga['april'] = 'notapril.jpg'
    context = {
        'ninjas': sendNinga,
    }

    return render(request, 'ninjas/show.html', context)
