# 連接rabbitmq
broker_url= 'amqp://guest:guest@192.168.90.149:5672//'
backend_url= 'redis://192.168.90.149:6378/0'
broker_connection_retry_on_startup = True

# broker是獲取任務的地方
# backend是返回運算結果的地方
# 如果你希望保留現有行為以在啟動時重試連接，應將 broker_connection_retry_on_startup 設為 True。