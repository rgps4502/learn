from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# Create your views here.


# account_tabe = google_account_table()
# account_tabe.save



# accounts = google_account_table.objects.all()
# print(accounts)

def get_home_page(requests):
    return HttpResponse('Hello')

def create_account(reuests):
    new_account = google_account_table(email=None, password='password123', bakemail='backup@example.com', phone='1234567890', birthday='2000-01-01')
    print(new_account)
    
    try:
        new_account.save()
        # 保存成功
        return(HttpResponse('創建帳號完成'))
    except (IntegrityError, ValidationError) as e:
        # 保存失敗，處理相應的錯誤
        return('創建帳號失敗',e)