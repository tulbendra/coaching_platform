from django.db import models
from authentication.models import User


class Test(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    title = models.CharField(max_length=200)
    date = models.DateField()


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()


class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    student_answer = models.TextField()
