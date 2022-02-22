### django_rest_framework
#### 1、定义api接口过程
```python
# 1、创建项目
# 2、创建应用
# 3、创建models
from django.db import models
from utils.models_base import BaseModels


class Student(BaseModels):
    # 模型字段
    name = models.CharField(max_length=100, verbose_name="姓名", help_text='提示文本：不能为空')
    sex = models.BooleanField(default=1, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    class Meta:
        db_table = "tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
# 4、设置settings,填写INSTALLED_APPS
# 5、执行数据迁移python manager.py makemigrations & python manager.py migrate
# 6、创建序列化器
from rest_framework import serializers
from apps.students.models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
# 7、创建视图
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
# 8、编辑路由
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentViewSet


# 实例化路由并注册
router = DefaultRouter()

router.register("student_set", StudentViewSet)

urlpatterns = [
    path("", include(router.urls))
]
```
#### 2、序列化和反序列化
```text
# 1、序列化：序列化器会把模型对象转换为字典,经过response之后会变成json字符串
# 2、反序列化：把客户端发送过来的数据经过request以后变成字典,序列化器可以把字典转换为模型
```