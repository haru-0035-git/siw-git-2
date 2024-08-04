def find_by_id():
    import sys
    sys.dont_write_bytecode = True
    import requests
    from util import input_util
    while True:
        id = input_util.input_int("idを入力してください>>>")
        url = f"http://172.0.0.1:8000/students/{id}"

        respons = requests.get(url)
        status = respons.status_code
        if status == 404:
            print("404 Not Found")
            continue
        else:
            break


    json = respons.json()
    results = json["students"]
    print("")
    print(f"{results["id"]}")
    print(f"{results["name"]}")
    print(f"{results["birthday"]}")
    print(f"{results["class"]}")
    print("")