from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import IntegrityError
from django.core.exceptions import ValidationError


# Create your views here.



def get_home_page(requests):
    return HttpResponse('Hello')

def create_account(reuests):
    '''
    將gmail帳號寫入數據庫
    必須參數 account  比如 /api/v1/create?account=test@gmail.com
    '''
    email = reuests.GET.get('account',None)
    if not email:
        return HttpResponse("缺少必要的參數 account")
    elif '@' not in email:
        return HttpResponse('不是正email格式')
    

    new_account = google_account_table(email=email, password='password123', bakemail='backup@example.com', phone='1234567890', birthday='2000-01-01')
    try:
        new_account.save()
        # 保存成功
        return(HttpResponse('創建帳號完成'))
    except (IntegrityError, ValidationError) as e:
        # 保存失敗，處理相應的錯誤
        return('創建帳號失敗',e)
    

def delete_account(request):
    '''
    將gmail帳號從數據庫刪除
    必須參數 account  比如 api/v1/delete?account=test@gmail.com
    '''

    # 從 POST 參數中獲取 email
    email = request.GET.get('account', None)
    if not email:
        return HttpResponse("缺少必要的參數 account")

    # 根據 email 找到對應的記錄
    try:
        accounts = google_account_table.objects.filter(email=email)
        print (accounts)
    except google_account_table.DoesNotExist as e:
        return HttpResponse("找不到符合條件的記錄")

    # 確定只有一個符合條件的記錄
    account = accounts.first()

    # 執行刪除操作
    if accounts:
        # 獲取該記錄的 id
        account_id = account.id
        account.delete()

        return HttpResponse(f"已成功刪除帳號為 {email} id 為 {account_id}的記錄")
    else:
        return HttpResponse(f'找不到該帳號的資料')