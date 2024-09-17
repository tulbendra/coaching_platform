from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance, TestResult, TestSubjectResult, Lecture, Subject
from .serializers import AttendanceSerializer, TestResultSerializer, LectureSerializer, TestSubjectResultSerializer

# View for Student Dashboard, including attendance, test results, and lectures
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

# View for Teacher Dashboard, including attendance and test results with subject-specific data
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

# View for teacher to add test results for students, including subject-wise marks
class AddTestResultView(APIView):
    def post(self, request):
        if request.user.is_teacher:
            # Create TestResult
            test_result_data = request.data.get('test_result')
            test_result = TestResult.objects.create(
                student_id=test_result_data['student_id'],
                test_name=test_result_data['test_name']
            )

            # Add subject-specific marks
            for subject_data in request.data.get('subject_results'):
                subject = Subject.objects.get(id=subject_data['subject_id'])
                TestSubjectResult.objects.create(
                    test_result=test_result,
                    subject=subject,
                    marks_obtained=subject_data['marks_obtained'],
                    max_marks=subject_data['max_marks']
                )
            return Response({"message": "Test result added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
