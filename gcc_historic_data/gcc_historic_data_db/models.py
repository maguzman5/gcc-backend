from django.db import models
from django.utils import timezone

class Run(models.Model):
    run_id = models.CharField(
         primary_key = True,
         max_length=200)
    process = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = '"employees_data"."runs"'

# Final schema
class Department(models.Model):
    department = models.CharField(max_length=100)
    run = models.CharField(max_length=200)

    class Meta:
        db_table = '"employees_data"."departments"'


class Job(models.Model):
    job = models.CharField(max_length=100)
    run = models.CharField(max_length=200)

    class Meta:
        db_table = '"employees_data"."jobs"'


class HiredEmployee(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    run = models.CharField(max_length=200)

    class Meta:
        db_table = '"employees_data"."hired_employees"'
