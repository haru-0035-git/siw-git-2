import requests
import input_util

print('⋆⋆⋆ 帳簿更新 ⋆⋆⋆')
while True:
    id = input_util.input_int('更新したいIDを選択してください : ')
    url = f"http://127.0.0.1:8000/accountbook/{id}"
    response_list = requests.get(url)
    list_response = response_list.json()
    if list_response["accountbook"] == []:
        print('そのIDは存在していません')
    else:
        break