from django.contrib import admin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    """
    课程管理
    """
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']  # 显示的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']  # 搜索
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']  # 过滤


class LessionAdmin(admin.ModelAdmin):
    """
    章节管理
    """
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 这里course__name是根据课程名称过滤
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(admin.ModelAdmin):
    """
    视频管理
    """
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(admin.ModelAdmin):
    """
    课程资源管理
    """
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'add_time', 'download']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)


