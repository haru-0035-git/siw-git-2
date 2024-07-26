import datetime

def input_bop(prompt):
    while True:
        bop = input(prompt)
        if bop == "1" or bop == "2":
            return int(bop)
        else:
            print('1か2を入力してください')

def input_date(prompt):
    while True:
        date = input(prompt)
        try:
            date = datetime.datetime.strptime(date,'%Y-%m-%d')
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


