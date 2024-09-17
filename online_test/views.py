from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test, TestQuestion, StudentAnswer
from .serializers import TestSerializer, TestQuestionSerializer, StudentAnswerSerializer


class TeacherTestView(APIView):
    def post(self, request):
        if request.user.is_teacher:
            serializer = TestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


class StudentTestView(APIView):
    def post(self, request):
        if request.user.is_student:
            serializer = StudentAnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(student=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
