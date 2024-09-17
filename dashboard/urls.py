from django.urls import path
from .views import StudentDashboardView, TeacherDashboardView, AddTestResultView

urlpatterns = [
    path('student/', StudentDashboardView.as_view(), name='student_dashboard'),
    path('teacher/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('add-test-result/', AddTestResultView.as_view(), name='add_test_result'),
]
