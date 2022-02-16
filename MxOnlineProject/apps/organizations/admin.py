from django.contrib import admin
from .models import City, CourseOrg, Teacher


class CityAdmin(admin.ModelAdmin):
    # 在管理后台中搜索
    search_fields = ["name", "desc"]
    # 在管理后台中过滤
    list_filter = ["name", "desc", "add_time"]


class CourseOrgAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)
admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(Teacher, TeacherAdmin)

