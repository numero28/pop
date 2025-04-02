from django.db import models
from datetime import timedelta, date

# Create your models here.
class Person(models.Model):
    cycle_length = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    """
    last_menses_start_date = date(year, month, day) 
    next_menses_date = last_menses_start_date + timedelta(days=cycle_length-1)
    end_date = next_menses_date + duration - 1
    ovulation_date = last_menses_start_date + timedelta(days=cycle_length / 2 - 1)
    fertile_window = f"{1} to {1}"
    safe_period = f"{1} to {1}"
    """