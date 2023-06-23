from celery import Celery
app = Celery('myapp', broker='redis://192.168.90.149:6378', backend='redis://192.168.90.149:6378/3', config_source='celeryconfig')


# broker是獲取任務的地方
# backend是返回運算結果的地方

@app.task
def add(x, y):
    return x + y
