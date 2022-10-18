from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display: 列表页展示的字段
    list_display = ["name", "status", "is_nav", "created_time"]
    # fields：表单显示的字段
    fields = ("name", "status", "is_nav")

    def save_model(self, request, obj, form, change):
        """
        默认情况下，将当前用户注册为owner；未登录时使用匿名用户
        """
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_time")
    fields = ("name", "status")

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # operator为自定义展示字段
    list_display = ["title", "status", "category", "created_time", "operator"]
    list_display_links = [] # 配置哪些字段可以作为链接，点击即可配置
    list_filter = ["category"] #配置 category 作为过滤条件
    search_fields = ["title", "category__name"] # 搜索字段

    actions_on_top = True # 动作相关配置，是否展示在顶部
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True # 保存/编辑是否在顶部

    fields = (
        ("category", "title"),
        "desc",
        "status",
        "content",
        "tag"
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = "操作"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
