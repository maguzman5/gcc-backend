from django.db import models
from django.utils import timezone


class Department(models.Model):
    department = models.CharField(max_length=100)

    class Meta:
        db_table = '"employees_data"."departments"'


class Job(models.Model):
    job = models.CharField(max_length=100)

    class Meta:
        db_table = '"employees_data"."jobs"'


class HiredEmployee(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        db_table = '"employees_data"."hired_employees"'
