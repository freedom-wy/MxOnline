# Generated by Django 4.0.4 on 2022-05-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0003_alter_browseinfo_useragent'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostLogininfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=64, verbose_name='设备IP地址')),
                ('ssh_port', models.CharField(blank=True, max_length=32, null=True, verbose_name='SSH登录端口')),
                ('ssh_user', models.CharField(blank=True, max_length=32, null=True, verbose_name='SSH登录用户')),
                ('ssh_password', models.CharField(blank=True, max_length=64, null=True, verbose_name='SSH登录密码')),
                ('ssh_rsa', models.CharField(blank=True, max_length=64, null=True, verbose_name='ssh私钥')),
                ('rsa_password', models.CharField(blank=True, max_length=64, null=True, verbose_name='私钥的密码')),
                ('ssh_status', models.IntegerField(default=0, verbose_name='0-登录失败,1-登录成功')),
                ('ssh_type', models.IntegerField(default=0, verbose_name='1-rsa登录,2-dsa登录,3-普通用户rsa登录,4-docker成功,5-docker无法登录')),
                ('system_version', models.CharField(blank=True, max_length=256, null=True, verbose_name='操作系统版本')),
                ('hostname', models.CharField(blank=True, max_length=256, null=True, verbose_name='主机名')),
                ('mac_adddress', models.CharField(blank=True, max_length=512, null=True, verbose_name='MAC地址')),
                ('sn', models.CharField(blank=True, max_length=256, null=True, verbose_name='设备SN号码')),
                ('machine_type', models.IntegerField(default=0, verbose_name='机器的类型 1=物理服务器,2=虚拟资产,3=网络设备 0=其他类型(未知)')),
                ('physics_machine_type', models.CharField(max_length=256, verbose_name='虚拟机上宿主机的类型')),
            ],
            options={
                'verbose_name': '初始化扫描信息表',
                'verbose_name_plural': '初始化扫描信息表',
                'db_table': 'hostlogininfo',
            },
        ),
        migrations.DeleteModel(
            name='BrowseInfo',
        ),
        migrations.DeleteModel(
            name='UserIPInfo',
        ),
    ]