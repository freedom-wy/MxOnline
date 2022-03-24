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
# 设置主键 primary_key
class PhoneCode(BaseModels):
    phone_num = models.CharField(max_length=11, verbose_name="手机号码", primary_key=True)
    phone_code = models.CharField(max_length=4, verbose_name="短信验证码")
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
#### 9、django生命周期
```text
1、浏览器发送请求到wsgi
2、wsgi转发请求到中间件的process_request方法,按照中间件的顺序,顺序执行
3、经过中间件后到url控制器,转发到视图
4、在视图中返回响应
5、到中间件的process_response方法,按照中间件的顺序,顺序执行
6、封装为response返回到浏览器
```
#### 10、中间件
```text
中间件可以定义五个方法
1、process_request
2、process_view(self, request, view_func, view_args, view_kwargs)
3、process_template_response(self,request,response)
4、process_exception(self, request, exception)
5、process_response(self, request, response)
以上方法的返回值可以是None或一个HttpResponse对象，如果是None，则继续按照django定义的规则向后继续执行，如果是HttpResponse对象，则直接将该对象返回给用户。
```
```python
# 自定义中间件
from django.utils.deprecation import MiddlewareMixin

class MD1(MiddlewareMixin):
    #自定义中间件，不是必须要有下面这两个方法，有request方法说明请求来了要处理，有response方法说明响应出去时需要处理，不是非要写这两个方法，如果你没写process_response方法，那么会一层一层的往上找，哪个中间件有process_response方法就将返回对象给哪个中间件
    def process_request(self, request):
        print("MD1里面的 process_request")

    def process_response(self, request, response):
        print("MD1里面的 process_response")
        return response
```
```text
中间件的process_request方法是在执行视图函数之前执行的。
当配置多个中间件时，会按照MIDDLEWARE中的注册顺序，也就是列表的索引值，从前到后依次执行的。
不同中间件之间传递的request都是同一个对象
多个中间件中的process_response方法是按照MIDDLEWARE中的注册顺序倒序执行的，也就是说第一个中间件的process_request方法首先执行，而它的process_response方法最后执行，最后一个中间件的process_request方法最后一个执行，它的process_response方法是最先执行。
```
```text
process_response,process_response方法是在视图函数之后执行的
它有两个参数，一个是request，一个是response，request就是上述例子中一样的对象，response是视图函数返回的HttpResponse对象。该方法的返回值也必须是HttpResponse对象。
from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):

    def process_request(self, request):
        print("MD1里面的 process_request")
        #不必须写return值
    def process_response(self, request, response):#request和response两个参数必须有，名字随便取
        print("MD1里面的 process_response")        #print(response.__dict__['_container'][0].decode('utf-8')) #查看响应体里面的内容的方法，或者直接使用response.content也可以看到响应体里面的内容，由于response是个变量，直接点击看源码是看不到的，你打印type(response)发现是HttpResponse对象，查看这个对象的源码就知道有什么方法可以用了。
　　　　 return response  #必须有返回值，写return response  ，这个response就像一个接力棒一样
        #return HttpResponse('瞎搞') ,如果你写了这个，那么你视图返回过来的内容就被它给替代了

class MD2(MiddlewareMixin):
    def process_request(self, request):
        print("MD2里面的 process_request")
        pass

    def process_response(self, request, response): #request和response两个参数必须要有，名字随便取
        print("MD2里面的 process_response") 
        return response  #必须返回response，不然你上层的中间件就没有拿到httpresponse对象，就会报错
```
```text
process_view方法是在process_request之后，reprocess_response之前，路由之后，视图函数之前执行的，执行顺序按照MIDDLEWARE中的注册顺序从前到后顺序执行的
process_exception 在process_view之后，只有在视图函数中出现异常了才执行，多个process_exception中间件，倒叙执行。
它返回的值可以是一个None也可以是一个HttpResponse对象。如果是HttpResponse对象，Django将调用模板和中间件中的process_response方法，并返回给浏览器，否则将默认处理异常。如果返回一个None，则交给下一个中间件的process_exception方法来处理异常。它的执行顺序也是按照中间件注册顺序的倒序执行。
```
#### 11、jwt
```text
传统token方式
用户登录成功后，服务端生成一个随机token给用户，并且在服务端(数据库或缓存)中保存一份token，以后用户再来访问时需携带token，服务端接收到token之后，去数据库或缓存中进行校验token的是否超时、是否合法。

jwt方式
用户登录成功后，服务端通过jwt生成一个随机token给用户（服务端无需保留token），以后用户再来访问时需携带token，服务端接收到token之后，通过jwt对token进行校验是否超时、是否合法。
```
#### 12、通过中间件进行Jwt验证
```python
# 1、校验用户后生成token
def create_token(self, payload):
    jwt_salt = "abcd1234567890!@#$%^&*()"
    import datetime
    import jwt
    headers = {
        "typ": "jwt",
        "alg": "HS256"
    }
    # 过期时间
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    token = jwt.encode(payload=payload, key=jwt_salt, algorithm="HS256", headers=headers)
    return token
# 接收用户发送过来的请求,校验token,中间件逻辑
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


def parse_payload(token):
    """
    验证token
    :param token:
    :return:
    """
    import jwt
    jwt_salt = "abcd1234567890!@#$%^&*()"
    result = {"status": False, "data": None, "error": None}
    try:
        verified_payload = jwt.decode(token, jwt_salt, "HS256")
    except jwt.exceptions.ExpiredSignatureError:
        result["error"] = "token已过期"
    except jwt.exceptions.DecodeError:
        result["error"] = "token认证失败"
    except jwt.exceptions.InvalidTokenError:
        result["error"] = "非法token"
    else:
        result["status"] = True
        result["data"] = verified_payload
    return result


class JwtAuthorizationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        定义jwt验证的中间件
        :param request:
        :return:
        """
        if request.path_info == "/get_token/" and request.method == "POST":
            return
        elif request.path_info == "/get_token/" and request.method == "GET":
            authorization = request.META.get("HTTP_AUTHORIZATION", "")
            authorization_info = authorization.split()
            if not authorization_info:
                return JsonResponse({"error": "未获取到token", "status": False})
            elif authorization_info[0].lower() != "jwt":
                return JsonResponse({"error": "token认证方式错误", "status": False})
            elif len(authorization_info) == 1 or len(authorization_info) > 2:
                return JsonResponse({"error": "非法token", "status": False})
            token = authorization_info[1]
            print(token)
            result = parse_payload(token)
            if not result["status"]:
                return JsonResponse(result)
            request.user_info = result["data"]
# 3、在视图中获取payload
# 4、注意要在settings中添加该中间件
```
#### 13、django websocket
##### 13.1 轮询
```text
1、轮询分为短轮询和长轮询
2、短轮询多是基于前端定时器不断轮询获取数据库中数据,长轮询多是基于前端发送请求后不断递归取数据,后端使用队列技术,有数据时直接返回,无数据时等待超时时间
```
##### 13.2 websocket 特点：建立连接后服务端可以主动发起请求
```text
1、应用场景：聊天室，实时图表
2、当django接收http请求时,他会根据URLconf以查找视图函数,然后调用视图函数来处理请求,当channels接收websocket连接时,
他会根据路由配置以查找对应的consumer,然后调用consumer上的各种函数来处理来自这个连接的事件
```
##### 13.3 websocket创建流程
```python
# 1、在项目目录下创建总websocket路由
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# 应用自己的路由
import chat.routing


# 和django总的urls.py相同,用于寻找应用下的websocket路由
application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    }
)
# 2、在settings中添加channels应用
INSTALLED_APPS = [
    "chat",
    "channels"
]

ASGI_APPLICATION = "ChannelsRooms.routing.application"

# 3、编写websocket的视图文件consumers.py
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

# 4、编写应用的websocket路由chat/routing.py
from django.urls import re_path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    re_path("^ws/chat/(?P<room_name>[^/]+)/$", ChatConsumer.as_asgi())
]
```



