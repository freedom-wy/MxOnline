### 框架
#### 1、flask和DJango中都可以添加多个app
#### 2、在flask的App中通过蓝图区分各个模块
#### 3、在django的app中通过路由来区分各个模块

### 数据库管理
#### 1、django中自带makemigrations和migrate模块
#### 2、flask中需手动安装Flask-Migrate并在app中初始化

### 模型类
#### 1、django中可以直接使用模型类方法增删改查
#### 2、flask中需要使用flask_sqlalchemy并实例化sqlalchemy
#### 3、模型类中可以通过外键简化模型类间的调用,也可以不设置外键,通过导入其他模型类操作该模型中的数据

### 用户注册
#### 1、django中应用注册到admin后,可以直接在admin中进行用户管理,注册等
#### 2、flask中通过模型类中的getter和setter方法,通过generate_password_hash设置用户密码
```python
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin, Base):
    _password = Column('password', String(128), nullable=False)

    # 精妙代码
    @property
    def password(self):
        """
        读取password的值
        :return:
        """
        return self._password

    @password.setter
    def password(self, raw):
        """
        设置密码的值
        :return:
        """
        self._password = generate_password_hash(raw)
```

### 登录验证
#### 1、django中使用authenticate验证输入的用户名密码是否正确,使用login模块进行登录操作和设置cookie等
```python
from django.contrib.auth import authenticate, login
# 校验用户名密码是否正确
user = authenticate(username=username, password=password)
if user:
    # 校验成功,执行登录操作
    login(request, user)
    # 跳转到首页
    return HttpResponseRedirect(reverse("index"))
```
#### 2、flask中需要先查询是否有该账号,通过check_password_hash模块校验,通过flask_login模块中的login_user进行登录操作和设置cookie等
```python
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
user = User.query.filter_by(email=login_form.email.data).first()
# 校验密码
if user and user.check_password(login_form.password.data):
    # 写入cookie信息, 需要在user模型类中继承UserMixin类, 可以在login_user中设置是否记住cookie
    login_user(user, remember=True)
```
#### 3、django的templages中通过全局变量request下的user实例的is_authenticated方法查看是否登录成功
```html
{% if request.user.is_authenticated %}
    pass
{% endif %}
```
#### 4、flask的templages中通过current_user的is_authenticated方法查看是否登录成功
```html
{% if current_user.is_authenticated %}
    pass
{% endif %}
```

### 页面跳转
#### 1、django中使用HttpResponseRedirect进行页面跳转
```python
from django.http import HttpResponseRedirect
return HttpResponseRedirect(reverse("index"))
```
#### 2、flask中使用redirect进行跳转
```python
from flask import render_template, request, redirect, url_for, flash, abort
return redirect(url_for("web.login"))
```

### 查找URL
#### 1、flask中通过url_for进行查找
#### 2、django中通过reverse进行查找,from django.urls import reverse