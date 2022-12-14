from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
评论模块
"""


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )
    target = models.ForeignKey(User, verbose_name="评论目标", on_delete=models.CASCADE)
    content = models.CharField(max_length=200, verbose_name="评论内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    website = models.URLField(verbose_name="网址")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"