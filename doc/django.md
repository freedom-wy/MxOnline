### django笔记  
***
#### 1、django项目和应用的创建  
```shell
# 创建项目
django-admin startproject mysite
# 运行项目
python manage.py runserver
# 创建应用
python manage.py startapp polls
```
#### 2、在django项目中显示一个html
```text
# 1、配置url
# 2、配置对应的views逻辑
# 3、拆分静态文件,可以放在对应的app下面,也可以放到公共的static目录下
# 4、在settings中配置全局的static文件访问路径,STATICFILES_DIRS
# 5、注意：配置url后无法访问,需修改settings文件中'DIRS': [os.path.join(BASE_DIR, "templates")]项；
# 单独的静态文件可直接放在相应的应用目录下,如果放置于公用static目录下需修改settings文件,添加
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static")
# ]
6、应用创建后需要在settings文件下注册
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.message_form1.apps.MessageForm1Config'
]
```
#### 3、在django中创建数据库模型类models
```text
# 1、在相应的app下找到models.py文件,创建模型类
# 2、在settings文件中配置数据库连接信息
# 3、执行数据库迁移python manage.py makemigrations和python manage.py migrate
```
```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        "ENGINE": "django.db.backends.mysql",
        "NAME": "vuln_manage",
        "USER": "root",
        "PASSWORD": "abcd1234",
        "HOST": "127.0.0.1"
    }
}
```
```python
class Message(models.Model):
    """
    创建留言板的表结构
    """
    name = models.CharField(max_length=20, verbose_name="姓名")
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.TextField(verbose_name="留言信息")

    class Meta:
        """
        这张表的一些信息
        """
        verbose_name = "留言信息"
        verbose_name_plural = verbose_name
        # 表名
        db_table = "message"
```
#### 4、orm增删改查
```python
# save()方法,如无数据则插入,如有数据则更新
```
#### 5、项目部署
```text
# 1、安装gunicorn
# 2、通过gunicorn启动django应用
gunicorn -w 4 -b 127.0.0.1:8081 Message.wsgi
# 3、配置nginx
server {
            listen 80;
            server_name message.yase.me; # 这是HOST机器的外部域名，用地址也行
            root /var/www/MxOnline;

            location / {
                proxy_pass http://127.0.0.1:8081; # 这里是指向 gunicorn host 的服务地址
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }
            
            location /static {
                alias /var/www/MxOnline/sample/Message/static;
            }

        }
# 4、检查nginx配置文件
nginx -t
# 5、重新加载nginx配置文件
nginx -s reload
```
