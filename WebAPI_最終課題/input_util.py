import datetime

def input_bop(prompt):
    while True:
        bop = input(prompt)
        if bop == "1" or bop == "2":
            return int(bop)
        else:
            print('1か2を入力してください')

def input_date_day(prompt):
    while True:
        date = input(prompt)
        try:
            datetime.datetime.strptime(date,'%Y-%m-%d')
            return date
        except:
            print('指定された形式で入力してください')

def input_int(prompt):
    while True:
        try:
            price = int(input(prompt))
            return price
        except:
            print('整数で入力してください')

def input_date_month(prompt):
    while True:
        date = input(prompt)
        try:
            datetime.datetime.strptime(date,'%Y-%m')
            return date
        except:
            print('指定された形式で入力してください')

import datetime

def format_date_str(date):
    if isinstance(date, str):
        # 日付文字列をdatetimeオブジェクトに変換
        date = datetime.datetime.strptime(date, '%Y-%m')
    formatted_date = date.strftime('%Y年%m月')
    formatted_date = formatted_date.replace('年0', '年')
    return formatted_date

def input_space(prompt):
    while True:
        str = input(prompt)
        str2 = str.strip()
        if str2 == "":
            print('この欄は必須のフィールドです')
        else:
            return str