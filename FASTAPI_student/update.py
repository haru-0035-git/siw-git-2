def update_student():
    import sys
    sys.dont_write_bytecode = True
    import requests
    from util import input_util

    while True:
        id = input_util.input_int("更新したいidを入力してください>>>")
        url = f"http://34.229.128.86:8000/students/{id}"
        respons_get = requests.get(url,params=payload)
        status_get = respons_get.status_code
        if status_get == 404:
            print('404 Not Found')
        else:
            break
    name = input('名前を入力してください>>')

    url = "http://34.229.128.86:8000/students/"
    payload={
        "name":name,
        "id":id
    }
    respons_put = requests.put(url,params=payload)

    status_put = respons_put.status_code
    if status_put == 204:
        print('Success!!')
    else:
        print('できてない')