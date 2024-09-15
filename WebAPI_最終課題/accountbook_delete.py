def delete():
    import requests
    import input_util

    print('⋆⋆⋆ 帳簿削除 ⋆⋆⋆')
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
            print('以下の帳簿を削除します')
            if result["bop"] == 1:
                result["bop"] = '収入'
                result["price"] = f"{result["price"]:,}"
                print(f'{result["id"]:<4}{result["date"]:<12}{result["bop"]:<4}{result["breakdown"]:<7}¥{result["price"]:>5}')
            else:
                result["bop"] = '支出'
                result["price"] = f"{result["price"]:,}"
                print(f'{result["id"]:<4}{result["date"]:<12}{result["bop"]:<4}{result["breakdown"]:<7}¥{result["price"]:>5}')

        url = f"http://127.0.0.1:8000/accountbook/{id}"
        while True :
            judge = input('本当に削除しますか (y/n) : ')
            if judge.lower() == 'y' :
                response = requests.delete(url)
                status_put = response.status_code
                if status_put == 204:
                    print('帳簿を削除しました')
                    break
                else:
                    print('削除に失敗しました')
            elif judge.lower() == 'n':
                return None
            else:
                print('yかnを入力してください')
        break