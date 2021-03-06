from django.contrib import admin
from .models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    """
    外键关联的类在界面上放到一起
    """
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 配置要展示的字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 设置可以进行过滤筛选的字段
    list_filter = ['pub_date']
    # 设置可搜索字段
    search_fields = ['question_text']
    # 对字段进行分组
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]


# 问题和选项录入二合一
admin.site.register(Question, QuestionAdmin)
