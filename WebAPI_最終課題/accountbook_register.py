import requests
import input_util
bop = input_util.input_bop('収入(1) or 支出(2)を入力してください : ')
date = input_util.input_date('日付を入力してください [%Y-%m-%d] : ')
breakdown = input('内訳を入力してください : ')
price = input_util.input_int('金額を入力してください : ')

url = "http://127.0.0.1:8000/accountbook/"
