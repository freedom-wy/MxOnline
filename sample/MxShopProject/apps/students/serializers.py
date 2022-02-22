from rest_framework import serializers
from apps.students.models import Student


class StudentSerializer(serializers.Serializer):
    """
    使用序列化器类进行序列化数据
    """
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    class_null = serializers.CharField()
    description = serializers.CharField()


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
