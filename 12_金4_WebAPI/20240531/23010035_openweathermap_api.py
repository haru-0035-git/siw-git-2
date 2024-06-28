import requests

try:
    while True:

        name = input('地域名を入力してください（ローマ字）>>>')

        url = "https://api.openweathermap.org/data/2.5/weather"
        payload = {"appid":"91032946538a463d0a38afcc50dcdb2f",
                "q":name,"jp"
                "lang":"ja",
                "units":"metric"
                }
        response = requests.get(url,payload)
        #JSONで取得
        json = response.json()
        result = json["weather"]
        if f'{result[0]["main"]}' == "Suns":
            print('天気：晴れ')
        elif f'{result[0]["main"]}' == "Clouds":
            print('天気：曇り')
        elif f'{result[0]["main"]}' == "Rain":
            print('天気：雨')
        elif f'{result[0]["main"]}' == "Clear":
            print('天気：晴れ')
        elif f'{result[0]["main"]}' == "Thunderstorm":
            print('天気：雷雨')
        elif f'{result[0]["main"]}' == "Drizzle":
            print('天気：小雨')
        elif f'{result[0]["main"]}' == "Snow":
            print('天気：雪')
        print(f'気温：{json["main"]["temp"]}°')
        print(f'湿度：{json["main"]["humidity"]}%')
        print('')
        break
except Exception as e:
    print(e)