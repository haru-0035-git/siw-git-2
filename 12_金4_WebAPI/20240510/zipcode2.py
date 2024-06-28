import requests
import re

#郵便番号検索APIのURL
def input_int():
    pattern = r"^\d{7}$"
    while True:
            code = input('郵便番号を入力してください(ハイフンなし)>>>')
            if re.match(pattern,code) is not None:
                return code
            print('エラー‼ 郵便番号はハイフンなしの７桁の数字で入力してください')





# url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={code}"
code = input_int()
url = "https://zipcloud.ibsnet.co.jp/api/search"
payload = {"zipcode":code}

#WebAPI呼び出し
# response = requests.get(url)

response = requests.get(url,payload)

#JSONで取得
json = response.json()

# print(json)
print(f'status={json["status"]}')

#ステータスコードのチェック
if json['status'] != 200:
    print(json["message"])
else:
    if json["results"] is None:
         print('該当住所がありません')
    else:
        for address in json['results']:
            print(f'{address["address1"]} {address["address2"]} {address["address3"]}')