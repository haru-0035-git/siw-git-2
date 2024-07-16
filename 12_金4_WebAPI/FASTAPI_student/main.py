import sys
sys.dont_write_bytecode = True
import delete,findbyid,register,selectall,update
from util import input_util
while True:
    print('1:一覧表示')
    print('2:ID検索')
    print('3:登録')
    print('4:更新')
    print('5:削除')
    print('6:終了')
    judge = input_util.input_int('メニューを選択してください>>')
    if judge == 1:
        selectall.select_all()
    elif judge == 2:
        findbyid.find_by_id()
    elif judge == 3:
        register.insert()
    elif judge == 4:
        update.update_student()
    elif judge == 5:
        delete.delete_student()
    else:
        break