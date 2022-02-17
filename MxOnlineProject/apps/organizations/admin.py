from django.contrib import admin
from .models import City, CourseOrg, Teacher


class CityAdmin(admin.ModelAdmin):
    # 在管理后台中搜索
    search_fields = ["name", "desc"]
    # 在管理后台中过滤
    list_filter = ["name", "desc", "add_time"]
    list_display = ['name', 'desc', 'add_time']


class CourseOrgAdmin(admin.ModelAdmin):
    """
    机构管理
    """
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'city__name', 'address', 'add_time']


class TeacherAdmin(admin.ModelAdmin):
    """
    讲师管理
    """
    list_display = ['name', 'org', 'work_years', 'work_company', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'click_nums', 'fav_nums', 'add_time']


admin.site.register(City, CityAdmin)
admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(Teacher, TeacherAdmin)

