import twstock
import pandas as p

stock = twstock.realtime.get('2455')
print(stock)
