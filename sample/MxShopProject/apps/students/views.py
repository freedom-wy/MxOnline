# from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Student
from .serializers import StudentModelSerializer, StudentSerializer, StudentModelSerializerSub
# from django.views import View
# from django.http.response import HttpResponse, JsonResponse
# import json
# 引入rest-framework的视图基类和response
# from rest_framework.views import APIView
# from rest_framework.response import Response
# http状态码
# from rest_framework import status
# #
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
# 5个视图扩展类
# 获取多条数据
from rest_framework.mixins import ListModelMixin
# 添加数据
from rest_framework.mixins import CreateModelMixin
# 获取单条数据
# from rest_framework.mixins import RetrieveModelMixin
# 更新数据
# from rest_framework.mixins import UpdateModelMixin
# 删除数据
# from rest_framework.mixins import DestroyModelMixin
# from rest_framework.viewsets import GenericViewSet
# class StudentSingleView(RetrieveModelMixin, GenericAPIView, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#     def put(self, request, pk):
#         return self.update(request, pk)
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
from rest_framework.viewsets import GenericViewSet
class StudentsListView(ListModelMixin, GenericViewSet, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # def get(self, request):
    #     return self.list(request)
    # def post(self, request):
    #     return self.create(request)
# class StudentGenericAPIViewPk(GenericAPIView):
#     """
#     获取单条数据
#     """
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#     def get(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object())
#         return Response(serializer.data, status.HTTP_200_OK)
# class StudentGenericAPIView(GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#     def get_serializer_class(self):
#         """
#         通过逻辑控制视图调用的序列化器
#         :return:
#         """
#         if self.request.method == "POST":
#             return StudentModelSerializer
#         return StudentModelSerializerSub
#     def get(self, request):
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         data = request.data
#         # 反序列化
#         serializer1 = self.get_serializer(data=data)
#         # 验证数据
#         serializer1.is_valid(raise_exception=True)
#         # 保存数据入库
#         instance = serializer1.save()
#         # 序列化一条数据
#         serializer2 = self.get_serializer(instance=instance)
#         return Response(serializer2.data)
# class StudentView(View):
#     """
#     未使用django rest framework
#     """
#     def get(self, request):
#         # 取出多条要序列化的数据
#         students = Student.objects.all()
#         # 取出一条要序列化的数据
#         # student = Student.objects.first()
#         # 创建序列化器对象, 如果是多条数据需要使用many参数
#         serializer = StudentSerializer(instance=students, many=True)
#         # 如果是一条数据则不需要使用many参数
#         # serializer = StudentSerializer(instance=student)
#         # 序列化数据
#         students_data = serializer.data
#         # print(type(students_data))
#         # 返回数据
#         return JsonResponse(data=students_data, safe=False)
#     def post(self, request):
#         """
#         用于操作反序列化
#         :param request:
#         :return:
#         """
#         # 获取前端传递过来的json数据,需要关闭csrf中间件
#         data = json.loads(request.body)
#         # 反序列化
#         serializer1 = StudentSerializer(data=data)
#         # 验证数据,如果验证数据失败,直接抛出异常
#         serializer1.is_valid(raise_exception=True)
#         # 通过view保存数据
#         # save_student = Student.objects.create(**serializer1.validated_data)
#         # 通过serializers保存数据,如果是添加数据则会调用create,如果是更新则会调用update
#         save_student = serializer1.save()
#         # 如果需要向前端展示则需要进行序列化
#         serializer2 = StudentSerializer(instance=save_student)
#         return JsonResponse(data=serializer2.data, status=200)
#     def put(self, request):
#         """
#         更新数据
#         :param request:
#         :return:
#         """
#         data = json.loads(request.body)
#         # 查找要更新的数据
#         instance = Student.objects.get(pk=data.get("id"))
#         # 反序列化
#         serializer1 = StudentSerializer(instance=instance, data=data)
#         # 数据验证
#         serializer1.is_valid(raise_exception=True)
#         # 更新数据,调用序列化器中的update方法
#         update_student = serializer1.save()
#         # 向前端返回序列化数据
#         serializer2 = StudentSerializer(instance=update_student)
#         return JsonResponse(data=serializer2.data, status=200)
# class StudentApiView(APIView):
#     def post(self, request):
#         """
#         :param request:
#         :return:
#         """
#         # 取客户端数据
#         data = request.data
#         # 反序列化
#         serializer1 = StudentModelSerializer(data=data)
#         # 校验数据
#         serializer1.is_valid(raise_exception=True)
#         # 保存数据
#         save_student = serializer1.save()
#         # response_data = serializer1.data
#         serializer2 = StudentSerializer(instance=save_student)
#         return Response(data=serializer2.data, status=status.HTTP_200_OK)

# from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
#     DestroyModelMixin
# from .models import Student
# from .serializers import StudentSerializer
#
#
# class StudentTestView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


