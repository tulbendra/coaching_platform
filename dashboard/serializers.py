from rest_framework import serializers
from .models import Attendance, TestResult, TestSubjectResult, Lecture, Subject

# Serializer for Attendance remains as it is
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

# Serializer for Lecture remains as it is
class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

# New serializer for Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

# New serializer for TestSubjectResult
class TestSubjectResultSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = TestSubjectResult
        fields = ['subject', 'marks_obtained', 'max_marks']

# Updated serializer for TestResult to include subject-specific results
class TestResultSerializer(serializers.ModelSerializer):
    subject_results = TestSubjectResultSerializer(many=True)

    class Meta:
        model = TestResult
        fields = ['student', 'test_name', 'date', 'subject_results']
