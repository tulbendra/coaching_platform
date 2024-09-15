from django.db import models
from authentication.models import User

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    date = models.DateField()
    present = models.BooleanField(default=False)

class TestResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    score = models.FloatField()
    subject = models.CharField(max_length=100)

class Lecture(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
