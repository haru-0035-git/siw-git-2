from menu import accountbook_delete
from menu import accountbook_register
from menu import accountbook_list
from menu import accountbook_update
while True:
    print('=== 帳簿メニュー ===')
    print('1. 帳簿登録')
    print('2. 帳簿一覧')
    print('3. 帳簿更新')
    print('4. 帳簿削除')
    print('5. 終了')
    judge = input('メニューを選択してください : ')
    if judge == '1':
        accountbook_register.insert()
    elif judge == '2':
        accountbook_list.selectall()
    elif judge == '3':
        accountbook_update
    elif judge == '4':
        accountbook_delete
    elif judge == '5':
        break
    else:
        print('1~5の中から選んでください')