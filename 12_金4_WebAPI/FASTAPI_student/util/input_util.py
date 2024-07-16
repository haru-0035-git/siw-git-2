import sys
sys.dont_write_bytecode = True
def input_int(prompt):
    while True:
        try:
            id = int(input(prompt))
            return id
        except:
            print('整数で入力してください')