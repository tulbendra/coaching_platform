from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance, TestResult, Lecture
from .serializers import AttendanceSerializer, TestResultSerializer, LectureSerializer

class StudentDashboardView(APIView):
    def get(self, request):
        if request.user.is_student:
            attendance = Attendance.objects.filter(student=request.user)
            results = TestResult.objects.filter(student=request.user)
            lectures = Lecture.objects.all()

            return Response({
                "attendance": AttendanceSerializer(attendance, many=True).data,
                "results": TestResultSerializer(results, many=True).data,
                "upcoming_lectures": LectureSerializer(lectures, many=True).data
            })
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

class TeacherDashboardView(APIView):
    def get(self, request):
        if request.user.is_teacher:
            attendance = Attendance.objects.all()
            results = TestResult.objects.all()

            return Response({
                "attendance": AttendanceSerializer(attendance, many=True).data,
                "results": TestResultSerializer(results, many=True).data
            })
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
