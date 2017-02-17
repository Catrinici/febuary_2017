from django.shortcuts import render, redirect

def index(request):
    return render(request, 'dojo_survey/index.html')

def results(request):
    if 'sbmsn_count' not in request.session:
        request.session['sbmsn_count'] = 0
    if request.method == "POST":
        request.session['sbmsn_count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']

        return render(request, 'dojo_survey/results.html')
    # else:
    #     return redirect('/')

def back(request):
    return redirect('/')

# Create your views here.
