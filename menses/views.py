from datetime import timedelta, datetime
from django.shortcuts import render
from .forms import MensesCalculatorForm

def index(request):
    return  render(request, 'menses/index.html', {'name':'Victor'})

def menses_calculator_view(request):
    
    next_period_date = None
    ovulation_date = None
    fertile_window_start = None
    fertile_window_end = None
    
    if request.method == "POST":
        form = MensesCalculatorForm(request.POST)
        if form.is_valid():
            last_period_date = form.cleaned_data['last_period_date']
            cycle_length = form.cleaned_data['cycle_length']
            
            next_period_date = last_period_date + timedelta(days=cycle_length)
            ovulation_date = last_period_date + timedelta(days=(cycle_length // 2))
            fertile_window_start = ovulation_date - timedelta(days=4)
            fertile_window_end = ovulation_date + timedelta(days=1)
    else:
        form = MensesCalculatorForm()
        
    context = {
        'form': form,
        'next_period_date': next_period_date,
        'ovulation_date': ovulation_date,
        'fertile_window_start': fertile_window_start,
        'fertile_window_end': fertile_window_end,
    }

    return render(request, 'menses/menses_calculator.html', context)
