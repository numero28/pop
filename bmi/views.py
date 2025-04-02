from datetime import timedelta, datetime
from django.shortcuts import render
from .forms import BMICalculatorForm



def index(request):
    return  render(request, 'bmi/index.html', {'name':'Victor'})

def bmi_index(weight, height):
    bmi = weight / height ** 2
    return round(bmi, 2)

def bmi_status(bmi):
    if bmi >= 30:
        message = "You are Obese"
    elif bmi >= 25:
        message = "You are over weight"
    elif bmi >= 18:
        message = "You have a normal weight"
    else:
        message = "You are under weight"
    return message

def bmi_calculator_view(request):    
    bmi = None
    message = None
    
    if request.method == "POST":
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            
            bmi = bmi_index(weight, height)
            message = bmi_status(bmi)
                                    
    else:
        form = BMICalculatorForm()
        
    context = {
        'form': form,
        'bmi': bmi,
        'message' : message,
    }

    return render(request, 'bmi/bmi_calculator.html', context)