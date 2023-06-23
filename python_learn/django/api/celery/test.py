from task import add
from celery.result import AsyncResult
from time import sleep

# 執行異步任務
task_id = add.delay(10, 99)
print(task_id)

# 等待一段時間，讓異步任務有時間執行
sleep(1)

# 印出任務結果
print(task_id.get())
