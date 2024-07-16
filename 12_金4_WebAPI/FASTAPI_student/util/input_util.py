import sys
sys.dont_write_bytecode = True
import datetime
def input_int(prompt):
    while True:
        try:
            id = int(input(prompt))
            return id
        except:
            print('整数で入力してください')

def input_date(prompt):
    while True:
        date = input(prompt)
        try:
            datetime.datetime.strptime(date,'%Y-%m-%d')
            return date
        except:
            print('日付で入力してください')