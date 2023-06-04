from django.db import models
from datetime import datetime
# Create your models here.
class fourm_post(models.Model):
    title = models.TextField(null=True,verbose_name="主題")
    content = models.TextField(null=True,verbose_name="內容")
    user_name = models.CharField(max_length=100,default="用戶不存在",verbose_name="用戶名")
    fourm_name = models.CharField(max_length=100,default="把名不存在",verbose_name="把名")
    publish_time = models.DateTimeField(verbose_name="發帖時間",default=datetime.now())


class fourm_search(models.Model):
    title = models.TextField(null=True,verbose_name="主題")
    content = models.TextField(null=True,verbose_name="內容")
    title_id = models.BigIntegerField(verbose_name="主題ID")
    content_id = models.BigIntegerField(verbose_name="內容ID")
    fourm_name = models.CharField(max_length=100,default="把名不存在",verbose_name="把名")
    publish_time = models.DateTimeField(verbose_name="發帖時間",default=datetime.now())
    choice_result = models.TextField(verbose_name="標籤")
    sign = models.BigIntegerField(verbose_name="標記",default="0")
