from django import forms

class BMICalculatorForm(forms.Form):
    height = forms.FloatField(min_value=0, max_value=3, label="Height (m)")
    weight = forms.FloatField(min_value=0, max_value=400, label="Weight (kg)")