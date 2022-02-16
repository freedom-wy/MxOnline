# Generated by Django 4.0.2 on 2022-02-16 15:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='课程难度')),
                ('learn_times', models.IntegerField(default=0, verbose_name='课程时长')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='课程标签')),
                ('category', models.CharField(default='', max_length=20, verbose_name='课程类别')),
                ('youneed_know', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='老师告诉你')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程相关',
                'verbose_name_plural': '课程相关',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='章节名称')),
                ('learn_times', models.IntegerField(default=0, verbose_name='章节时长')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '章节相关',
                'verbose_name_plural': '章节相关',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='视频名称')),
                ('url', models.CharField(default='', max_length=200, verbose_name='视频地址')),
                ('learn_times', models.IntegerField(default=0, verbose_name='视频时长')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频相关',
                'verbose_name_plural': '视频相关',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='资源名称')),
                ('file', models.FileField(upload_to='course/resource/%Y%m', verbose_name='资源文件')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
    ]
