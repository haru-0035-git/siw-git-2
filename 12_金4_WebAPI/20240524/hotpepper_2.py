import requests
import random 
try:
    while True:
        area = input('地域名を入力してください>>>')
        keyword = input('ジャンルを入力してください>>>')
        url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
        payload = {"key":"2c2a30877b8369ee",
                "keyword":keyword,
                "format":"json",
                "address":area
                }
        response = requests.get(url,payload)

        #JSONで取得
        json = response.json()
        if json["results"]["results_available"] == 0:
            print('条件に該当するお店が存在しません')
        else:
            result = random.choice(json["results"]["shop"])
            print('おすすめのお店')
            print(f'名前:{result["name"]}')
            print(f'住所:{result["address"]}')
            print(f'URL:{result["urls"]["pc"]}')
            print('')
            break
except Exception as e:
    print('エラーが発生しました')



