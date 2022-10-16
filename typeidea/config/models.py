from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
配置相关数据 初始化侧边栏、友链相关model
"""

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    href = models.URLField(verbose_name="链接") # 默认长度200
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    weight = models.PositiveIntegerField(default=1, # (1,1), (2,2), (3,3)
                                         choices=zip(range(1, 6), range(1, 6)), verbose_name="权重",
                                         help_text="权重高展示位置靠前")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友链"

class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, "展示"),
        (STATUS_HIDE, "隐藏"),
    )
    STATUS_TYPE = (
        (1, "HTML"),
        (2, "最新文章"),
        (3, "最热文章"),
        (4, "最近评论"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=STATUS_TYPE,
                                               verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="展示内容",
                               help_text="非Html格式可为空")
    status = models.PositiveIntegerField(default=STATUS_SHOW,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"