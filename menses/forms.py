from django import forms

class MensesCalculatorForm(forms.Form):
    last_period_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Last Period Date")
    cycle_length = forms.IntegerField(min_value=21, max_value=35, label="Cycle Length (days)")
