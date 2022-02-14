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
```