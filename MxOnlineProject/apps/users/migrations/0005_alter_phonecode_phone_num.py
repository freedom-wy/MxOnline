# Generated by Django 4.0.2 on 2022-03-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_phonecode_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecode',
            name='phone_num',
            field=models.CharField(max_length=11, unique=True, verbose_name='手机号码'),
        ),
    ]