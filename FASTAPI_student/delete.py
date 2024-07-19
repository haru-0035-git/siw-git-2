def delete_student():
    import sys
    sys.dont_write_bytecode = True
    import requests
    from util import input_util

    while True:
        id = input_util.input_int("削除したいidを入力してください>>>")
        url = f"http://54.82.49.225:8000/students/{id}"
        respons_get = requests.get(url)
        status_get = respons_get.status_code
        if status_get == 404:
            print('404 Not Found')
        else:
            break

    url = "http://54.82.49.225:8000/students/"
    payload={
        "id":id
    }
    respons_put = requests.delete(url,params=payload)

    status_put = respons_put.status_code
    if status_put == 204:
        print('Success!!')
    else:
        print('できてない')