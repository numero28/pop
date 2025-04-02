from django.urls import path
from . import views

app_name = 'menses'

urlpatterns=[
    path('',views.index, name='index'),
    path('menses_calculator/', views.menses_calculator_view, name='menses_calculator'),
    #path('menses_response/', views.menses_response, name='menses_response'),
]
