from django.shortcuts import render, redirect
import random
import string
# Create your views here.
def index(request):
    randomWord = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
    if not 'attempt' in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    context = {
        'randomWord': randomWord,
    }
    return render(request, 'wordApps/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('word:index')
