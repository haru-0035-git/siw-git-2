import requests

num1 = input("1つ目の数値を入力してください>>>")
num2 = input("2つ目の数値を入力してください>>>")

url = "http://127.0.0.1:8000/div/"

#WebAPI呼び出し
payload = {"num1":num1,
           "num2":num2
           }
response = requests.get(url,payload)

#JSONで取得
json = response.json()

# print(json)
ans = json["ans"]
print(f'割り算の答え:{ans}')