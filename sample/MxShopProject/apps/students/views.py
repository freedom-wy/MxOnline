from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer, StudentSerializer
from django.views import View
from django.http.response import HttpResponse, JsonResponse
import json
# 引入rest-framework的视图基类和response
from rest_framework.views import APIView
from rest_framework.response import Response
# http状态码
from rest_framework import status


class StudentView(View):
    """
    未使用django rest framework
    """
    def get(self, request):
        # 取出多条要序列化的数据
        students = Student.objects.all()
        # 取出一条要序列化的数据
        # student = Student.objects.first()
        # 创建序列化器对象, 如果是多条数据需要使用many参数
        serializer = StudentSerializer(instance=students, many=True)
        # 如果是一条数据则不需要使用many参数
        # serializer = StudentSerializer(instance=student)
        # 序列化数据
        students_data = serializer.data
        # print(type(students_data))
        # 返回数据
        return JsonResponse(data=students_data, safe=False)

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


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
