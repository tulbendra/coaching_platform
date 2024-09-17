from django.db import models
from authentication.models import User

# Attendance model remains as it is
class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.date}"

# Lecture model remains as it is
class Lecture(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    title = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} by {self.teacher.username}"

# New model for subjects
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Updated TestResult model with test name
class TestResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    test_name = models.CharField(max_length=200)  # Test name column added
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test_name}"

# New model for storing subject-specific results for a test
class TestSubjectResult(models.Model):
    test_result = models.ForeignKey(TestResult, related_name='subject_results', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    max_marks = models.FloatField()

    def __str__(self):
        return f"{self.test_result.test_name} - {self.subject.name}"
