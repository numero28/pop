from django.urls import path
from . import views

app_name = 'bmi'

urlpatterns=[
    path('',views.index, name='index'),
    path('bmi_calculator/', views.bmi_calculator_view, name='bmi_calculator'),
    #path('menses_response/', views.menses_response, name='menses_response'),
]
