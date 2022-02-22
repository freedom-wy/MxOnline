from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer, StudentSerializer
from django.views import View
from django.http.response import JsonResponse


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
        # 返回数据
        return JsonResponse(data=students_data, safe=False)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
