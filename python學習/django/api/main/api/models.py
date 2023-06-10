from django.db import models

# Create your models here.
class google_account_table(models.Model):
    email = models.TextField(null=False, blank=False, verbose_name='信箱')
    password = models.TextField(null=False, blank=False, verbose_name='密碼')
    bakemail = models.TextField(null=False, blank=False, verbose_name='備用信箱')
    phone = models.TextField(null=False, blank=False, verbose_name='手機號碼')
    birthday = models.TextField(null=False, blank=False, verbose_name='生日')

    def __str__(self) -> str:
        return self.email

class google_account_search(models.Model):
    email = models.TextField(null=False, blank=False, verbose_name='信箱')
    def __str__(self) -> str:
        return self.email