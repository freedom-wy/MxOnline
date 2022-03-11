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
#### 6、默认的django admin
```shell
# 创建用户
python manage.py createsuperuser
# 用户名:admin,密码:abcd1234
```
#### 7、将编写好的用户模型注册到后台管理系统中
```python
# user应用下的admin中进行注册
from django.contrib import admin
from apps.users.models import UserProfile
# from django.contrib.auth.admin import UserAdmin


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
```
#### 8、cookie和session
```text
cookie
Cookie规范-默认
1、Cookie大小上限为4KB； 
2、一个服务器最多在客户端浏览器上保存20个Cookie； 
3、一个浏览器最多保存300个Cookie，因为一个浏览器可以访问多个服务器。
4、cookie是基于域名安全的,一个域名可以对应多个cookie,一个cookie对应一个域名
5、cookie有过期时间,如果不指定,默认关闭浏览器后cookie就会过期

设置cookie
response.set_signed_cookie("login", "yase", salt="abcd1234")
获取cookie
request.get_signed_cookie("login", salt="abcd1234", default=None)

session
一个网站对一个浏览器，是一个sessionid的，换一个浏览器客户端，肯定会生成另外一个sessionid，django-session表里面的session_key肯定不同，但是session_data字段的数据肯定是一样的，当然了，这个还要看人家的加密规则。
1、浏览器访问服务器,服务器生成session信息,session信息包含两部分key和value,key为sessionid,将以cookie值得形式返回给浏览器,value将存储到django_session表中
2、浏览器携带sessionid的cookie访问web应用,服务器从cookie中取出sessionid,并查库,将信息附加到request对象中
def set_session(request):
    request.session["hello"] = "world"
    return HttpResponse("设置session")


def get_session(request):
    session_value = request.session.get("hello", "")
    return HttpResponse(session_value)

清除session
request.session.flush()
设置session过期时间
设置会话的超时时间，如果没有指定过期时间则两个星期后过期。
如果value是一个整数，会话将在value秒没有活动后过期。
如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
如果value为None，那么会话永不过期。
request.session.set_expiry(value)
```





