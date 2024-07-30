def selectall():
    import requests
    import input_util

    print('⋆⋆⋆ 帳簿一覧 ⋆⋆⋆')
    date = input_util.input_date_month('年月を入力してください[%Y-%m] : ')

    print(f"--- {input_util.format_date_str(date)} ---")

    url = f"http://127.0.0.1:8000/accountbook/{date}"

    respons = requests.get(url)

    json = respons.json()
    result = json["accountbook"]
    print(f"{'ID':<4}{'年月日':<9}{'種別':<4}{'内訳':<7}{'金額':<5}")
    print("-"*60)


    income = 0
    spending = 0

    for results in result:
        if results["bop"] == 1:
            results["bop"] = '収入'
            income += results["price"]
            results["price"] = f"{results["price"]:,}"
            print(f'{results["id"]:<4}{results["date"]:<12}{results["bop"]:<4}{results["breakdown"]:<7}¥{results["price"]:>5}')
        else:
            results["bop"] = '支出'
            spending += results['price']
            results["price"] = f"{results["price"]:,}"
            print(f'{results["id"]:<4}{results["date"]:<12}{results["bop"]:<4}{results["breakdown"]:<7}¥{results["price"]:>5}')
    total = income - spending
    print(f'収入 : ¥{income:,}')
    print(f'支出 : ¥{spending:,}')
    print(f'合計 : ¥{total:,}')
