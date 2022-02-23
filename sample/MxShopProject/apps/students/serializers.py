from rest_framework import serializers
from apps.students.models import Student


class StudentSerializer(serializers.Serializer):
    """
    使用序列化器类进行序列化数据
    """
    # required必填字段
    name = serializers.CharField(required=True)
    sex = serializers.BooleanField(required=True)
    age = serializers.IntegerField(max_value=100, min_value=0)
    class_null = serializers.CharField()
    # 允许为空
    description = serializers.CharField(allow_null=True, allow_blank=True)

    # 对反序列化单个字段进行校验
    def validate_description(self, value):
        """
        对description进行校验
        :param value:
        :return:
        """
        if "django" in value.lower():
            raise serializers.ValidationError(detail="描述中不能出现django")
        return value

    def validate(self, attrs):
        """
        对反序列化多个字段进行校验
        :param attrs:
        :return:
        """
        class_null = attrs.get("class_null")
        sex = attrs.get("sex")
        if class_null == "300" and sex:
            raise serializers.ValidationError("300班级不能有男的")
        return attrs

    def create(self, validated_data):
        """
        保存数据
        :param validated_data: 验证通过后的数据
        :return:
        """
        student = Student.objects.create(**validated_data)
        return student

    def update(self, instance, validated_data):
        """
        更新数据
        :param instance:
        :param validated_data:
        :return:
        """
        instance.name = validated_data.get("name")
        instance.sex = validated_data.get("sex")
        instance.age = validated_data.get("age")
        instance.class_null = validated_data.get("class_null")
        instance.description = validated_data.get("description")
        instance.save()
        return instance


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
