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
#### 3、对数据进行校验
```python
# 1、在serializers字段中进行校验,添加字段约束
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
# 2、在serializers中通过validate_字段名或validate方法进行校验
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
# 3、在视图中启用校验
def post(self, request):
    """
    用于操作反序列化
    :param request:
    :return:
    """
    # 获取前端传递过来的json数据,需要关闭csrf中间件
    data = json.loads(request.body)
    # 反序列化
    serializer = StudentSerializer(data=data)
    # 验证数据,如果验证数据失败,直接抛出异常
    serializer.is_valid(raise_exception=True)
    return JsonResponse(data=serializer.validated_data)
```
#### 4、保存数据和更新数据
```python
# 保存数据
# 1、在视图中,数据验证后,调用序列化器的save方法
def post(self, request):
    """
    用于操作反序列化
    :param request:
    :return:
    """
    # 获取前端传递过来的json数据,需要关闭csrf中间件
    data = json.loads(request.body)
    # 反序列化
    serializer1 = StudentSerializer(data=data)
    # 验证数据,如果验证数据失败,直接抛出异常
    serializer1.is_valid(raise_exception=True)
    # 通过view保存数据
    # save_student = Student.objects.create(**serializer1.validated_data)
    # 通过serializers保存数据,如果是添加数据则会调用create,如果是更新则会调用update
    save_student = serializer1.save()
    # 如果需要向前端展示则需要进行序列化
    serializer2 = StudentSerializer(instance=save_student)
    return JsonResponse(data=serializer2.data, status=200)
# 2、调用序列化器的save方法后会调用序列化器的create方法
def create(self, validated_data):
    """
    保存数据
    :param validated_data: 验证通过后的数据
    :return:
    """
    student = Student.objects.create(**validated_data)
    return student
# 更新数据
# 1、在视图中调用序列化器时需要传递要更新数据的实例并调用序列化器的save方法
def put(self, request):
    """
    更新数据
    :param request:
    :return:
    """
    data = json.loads(request.body)
    # 查找要更新的数据
    instance = Student.objects.get(pk=data.get("id"))
    # 反序列化
    serializer1 = StudentSerializer(instance=instance, data=data)
    # 数据验证
    serializer1.is_valid(raise_exception=True)
    # 更新数据,调用序列化器中的update方法
    update_student = serializer1.save()
    # 向前端返回序列化数据
    serializer2 = StudentSerializer(instance=update_student)
    return JsonResponse(data=serializer2.data, status=200)
# 2、调用序列化器的save方法后会调用序列化器的update方法
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
    # 调用模型类的save方法
    instance.save()
    return instance
```
#### 5、ModelSerializer与常规的Serailizer相同,提供了基于模型类自动生成一系列字段,基于模型类自动生成validators,也可以重写,包含默认的create()和update()方法
#### 6、视图如果继承的是View,则需要在get,post,put等方法中显示的进行序列化和反序列化,验证数据,save等操作,在序列化器类中不需要定义create和update方法