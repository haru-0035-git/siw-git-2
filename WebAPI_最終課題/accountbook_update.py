def update():
    import requests
    import input_util

    print('⋆⋆⋆ 帳簿更新 ⋆⋆⋆')
    while True:
        id = input_util.input_int('IDを入力してください : ')
        url = f"http://127.0.0.1:8000/accountbook/find_id/{id}"
        response_list = requests.get(url)
        get_status = response_list.status_code
        if get_status == 404:
            print('そのIDは存在していません')
        else:
            json = response_list.json()
            result = json["accountbook"]
            print('以下の帳簿を更新します')
            print(f"{'ID':<4}{'年月日':<9}{'種別':<4}{'内訳':<7}{'金額':<5}")
            print("-"*60)
            if result["bop"] == 1:
                result["bop"] = '収入'
                result["price"] = f"{result["price"]:,}"
                print(f'{result["id"]:<4}{result["date"]:<12}{result["bop"]:<4}{result["breakdown"]:<7}¥{result["price"]:>5}')
            else:
                result["bop"] = '支出'
                result["price"] = f"{result["price"]:,}"
                print(f'{result["id"]:<4}{result["date"]:<12}{result["bop"]:<4}{result["breakdown"]:<7}¥{result["price"]:>5}')
            break
    bop = input_util.input_bop('収入(1) or 支出(2)を入力してください : ')
    date = input_util.input_date_day('日付を入力してください [%Y-%m-%d] : ')
    breakdown = input('内訳を入力してください : ')
    price = input_util.input_int('金額を入力してください : ')

    url = "http://127.0.0.1:8000/accountbook/"
    payload = {
        "date":date,
        "bop":bop,
        "breakdown":breakdown,
        "price":price,
        "id":id
    }
    response_put = requests.put(url,json=payload)

    status_put = response_put.status_code
    if status_put == 204:
        print('帳簿を更新しました')
    else:
        print('更新に失敗しました')

