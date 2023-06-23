import pandas as pd

# 單維度操作
# 建立Series
# data = pd.Series([20, 10, 15])
# print(data)
# # 取最大值
# print('Max', data.max())
# # 取中間值
# print('Median', data.median())
# # 把數據X2
# data = data*2
# print(data)

# 比較裡面的數據有沒有等於20  如果有返回True  否則 False
# data = data == 20
# print(data)


# 雙維度操作
# # 建立DataFrame 字典格式
# data = pd.DataFrame({
#     "name": ["AMY", "john", "bob"],
#     "salary": [3000, 5000, 4000]
# })
# # 基本操作
# print(data)
# # 取得特定欄位
# # print(data['name'])
# print('===============')
# # 取得特定的列 橫向
# print(data.iloc[0])
