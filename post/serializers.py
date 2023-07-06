from rest_framework import serializers
from .models import Student, Course

class PostSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(allow_blank=True, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)
