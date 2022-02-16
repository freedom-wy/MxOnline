from django.db import models
from utils.models_base import BaseModels


class City(BaseModels):
    """
    课程机构所在城市
    """
    name = models.CharField(verbose_name="城市名称", max_length=20)
    desc = models.CharField(verbose_name="城市描述", max_length=200)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        用于在admin中添加城市显示名字
        :return:
        """
        return self.name


class CourseOrg(BaseModels):
    """
    课程机构相关
    """
    name = models.CharField(verbose_name="机构名称", max_length=50)
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(max_length=20, choices=(
        ("pxjg", "培训机构"),
        ("gx", "高校"),
        ("gr", "个人")
    ), verbose_name="机构类别", default="pxjg")
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    tag = models.CharField(verbose_name="机构标签", max_length=10, default="全国知名")
    fav_nums = models.IntegerField('收藏数', default=0)
    students = models.IntegerField("学习人数", default=0)
    course_nums = models.IntegerField("课程数", default=0)
    image = models.ImageField('logo', upload_to='org/%Y/%m', max_length=100)
    address = models.CharField('机构地址', max_length=150, )
    city = models.ForeignKey(City, verbose_name='所在城市', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(BaseModels):
    """
    讲师相关
    """
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField('教师名', max_length=50)
    work_years = models.IntegerField('工作年限', default=0)
    work_company = models.CharField('就职公司', max_length=50)
    work_position = models.CharField('公司职位', max_length=50)
    points = models.CharField('教学特点', max_length=50)
    click_nums = models.IntegerField('点击数', default=0)
    fav_nums = models.IntegerField('收藏数', default=0)
    teacher_age = models.IntegerField('年龄', default=25)
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100)

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name


