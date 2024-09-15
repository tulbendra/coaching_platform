from django.urls import path
from .views import TeacherTestView, StudentTestView

urlpatterns = [
    path('teacher/', TeacherTestView.as_view(), name='teacher_test'),
    path('student/', StudentTestView.as_view(), name='student_test'),
]
