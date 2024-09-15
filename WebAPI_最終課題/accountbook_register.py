def insert():
    import requests
    import input_util
    print('⋆⋆⋆ 帳簿登録 ⋆⋆⋆')
    bop = input_util.input_bop('収入(1) or 支出(2)を入力してください : ')
    date = input_util.input_date_day('日付を入力してください [%Y-%m-%d] : ')
    breakdown = input_util.input_space('内訳を入力してください : ')
    price = input_util.input_int('金額を入力してください : ')


    url = "http://127.0.0.1:8000/accountbook/"

    payload = {
        "date":date,
        "bop":bop,
        "breakdown":breakdown,
        "price":price
    }

    respons_post = requests.post(url,json=payload)

    status_post = respons_post.status_code
    if status_post == 201:
        print('帳簿に登録しました')
    else:
        print('エラーが発生しました')