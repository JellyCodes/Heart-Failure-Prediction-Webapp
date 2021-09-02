from django.shortcuts import render
from . import functions as fn


# home page view
def index(request):
    return render(request, 'index.html')


# result page view
def result(request):
    if request.method == 'POST':
        # getting user inputs for prediction
        age = float(request.POST.get("age"))

        anaemia = request.POST.get('anaemia')
        if anaemia == 'Yes':
            anaemia = 1
        elif anaemia == 'No':
            anaemia = 0

        diabetes = request.POST.get('diabetes')
        if diabetes == 'Yes':
            diabetes = 1
        elif diabetes == 'No':
            diabetes = 0
        
        HBP = request.POST.get('HBP')
        if HBP == 'Yes':
            HBP = 1    
        elif HBP == 'No':
            HBP = 0
        
        serum = float(request.POST.get('serum'))
        
        smoke = request.POST.get('smoke')
        if smoke == 'Yes':
            smoke = 1
        elif smoke == 'No':
            smoke = 0

        # getting prediction
        result = fn.getPrediction(age, anaemia, diabetes, HBP, serum, smoke)

    return render(request, 'result.html', {'result': result})