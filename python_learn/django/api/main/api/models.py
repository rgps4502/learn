from django.db import models


# Create your models here.
class google_account_table(models.Model):
    email = models.CharField(max_length=255, null=False, blank=False, verbose_name="信箱")
    password = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="密碼"
    )
    bakemail = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="備用信箱"
    )
    phone = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="手機號碼"
    )
    birthday = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="生日"
    )

    def __str__(self) -> str:
        return self.email


class google_account_search(models.Model):
    email = models.CharField(max_length=255, null=False, blank=False, verbose_name="信箱")

    def __str__(self) -> str:
        return self.email


# admin==================
# 景點位置
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # 顯示景點位置

class Post(models.Model):
    subject = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # 顯示景點位置


