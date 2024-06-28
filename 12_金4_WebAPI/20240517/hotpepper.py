import requests
import re

# #郵便番号検索APIのURL
# def input_int():
#     pattern = r"^\d{7}$"
#     while True:
#             code = input('郵便番号を入力してください(ハイフンなし)>>>')
#             if re.match(pattern,code) is not None:
#                 return code
#             print('エラー‼ 郵便番号はハイフンなしの７桁の数字で入力してください')




key = "2c2a30877b8369ee"
# code = input_int()
url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
payload = {"key":key,
           "name":"焼肉",
           "karaoke":1,
           "format":"json"
           }

#WebAPI呼び出し
# response = requests.get(url)

response = requests.get(url,payload)

#JSONで取得
json = response.json()

# print(json)
result = json["results"]
for shop in result["shop"]:
    print(f'{shop["name"]}')

#ステータスコードのチェック
# if json['status'] != 200:
#     print(json["message"])
# else:
#     if json["results"] is None:
#          print('該当住所がありません')
#     else:
#         for address in json['results']:
#             print(f'{address["address1"]} {address["address2"]} {address["address3"]}')