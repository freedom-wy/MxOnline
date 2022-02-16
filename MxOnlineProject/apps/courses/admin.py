from django.contrib import admin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(admin.ModelAdmin):
    pass


class LessionAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class CourseResourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)


