import requests

#郵便番号検索APIのURL
def input_int():
    while True:
        try:
            code = int(input('郵便番号を入力してください(ハイフンなし)>>>'))
            return code
        except:
            print('半角数字で入力してください')





while True:
    try:
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
            break
        else:
            for address in json['results']:
                print(f'{address["address1"]} {address["address2"]} {address["address3"]}')
        break
    except Exception as e:
        print(e)