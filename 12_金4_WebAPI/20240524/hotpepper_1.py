import requests
import re

shopname = input('店名の一部を入力してください>>>')
area = input('都道府県名を入力してください>>>')
url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
payload = {"key":"2c2a30877b8369ee",
           "name":shopname,
        #    "karaoke":1,
           "format":"json",
           "address":area
           }


response = requests.get(url,payload)

#JSONで取得
json = response.json()

# print(json)
result = json["results"]
for shops in result["shop"]:
    print(f'名前：{shops["name"]}')
    print(f'住所：{shops["address"]}')
    print(f'最寄り駅：{shops["station_name"]}')
    print('')
