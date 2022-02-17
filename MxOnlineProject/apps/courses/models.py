# 课程表模型类
from django.db import models
from utils.models_base import BaseModels
from apps.organizations.models import Teacher


class Course(BaseModels):
    """
    课程相关模型类
    """
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=(
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    ), max_length=2, verbose_name="课程难度")
    learn_times = models.IntegerField(default=0, verbose_name="课程时长")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    tag = models.CharField('课程标签', default='', max_length=10)
    category = models.CharField("课程类别", max_length=20, default="")
    youneed_know = models.CharField('课程须知', max_length=300, default='')
    teacher_tell = models.CharField('老师告诉你', max_length=300, default='')
    # 课程关联的讲师
    teacher = models.ForeignKey(Teacher, verbose_name="讲师", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "课程相关"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModels):
    """
    章节相关模型类
    """
    # 设置章节关联的课程外键
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="章节名称", max_length=100)
    learn_times = models.IntegerField(verbose_name="章节时长", default=0)

    class Meta:
        verbose_name = "章节相关"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 课程名称-章节名称
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)


class Video(BaseModels):
    """
    章节下的视频相关
    """
    # 视频关联的章节
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="视频名称", max_length=100)
    url = models.CharField(verbose_name="视频地址", max_length=200, default="")
    learn_times = models.IntegerField(verbose_name="视频时长", default=0)

    class Meta:
        verbose_name = "视频相关"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModels):
    """
    课程资源相关
    """
    # 课程资源关联到课程
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="资源名称", max_length=100)
    download = models.FileField(verbose_name="资源文件", upload_to="course/resource/%Y%m", max_length=100)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




