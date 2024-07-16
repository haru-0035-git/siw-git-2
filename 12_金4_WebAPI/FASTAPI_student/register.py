def insert():
    import sys
    sys.dont_write_bytecode = True
    import requests
    from util import input_util

    while True:
        id = input_util.input_int("idを入力してください>>>")
        url = f"http://192.168.0.30:8000/students/{id}"
        payload = {
            id:id
        }
        respons_get = requests.get(url,params=payload)
        status_get = respons_get.status_code
        if status_get == 404:
            break
        else:
            print('そのIDはすでに存在しています')
    name = input('名前を入力してください>>')
    birthday = input_util.input_date('生年月日を入力してください>>')
    cls = input('クラスを入力してください>>')

    url = "http://192.168.0.30:8000/students/"
    payload={
        "id":id,
        "name":name,
        "birthday":birthday,
        "cls":cls
    }
    respons_post = requests.post(url,json=payload)

    status_post = respons_post.status_code
    if status_post == 201:
        print('Success!!')
    else:
        print('できてない')