# Generated by Django 4.0.2 on 2022-02-21 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('name', models.CharField(help_text='提示文本：不能为空', max_length=100, verbose_name='姓名')),
                ('sex', models.BooleanField(default=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('class_null', models.CharField(max_length=5, verbose_name='班级编号')),
                ('description', models.TextField(max_length=1000, verbose_name='个性签名')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'tb_student',
            },
        ),
    ]
