def select_all():
    import sys
    sys.dont_write_bytecode = True
    import requests

    url = "http://192.168.0.30:8000/students"
    respons = requests.get(url)

    json = respons.json()

    results = json["students"]
    for result in results:
        print("")
        print(f"{result["id"]}")
        print(f"{result["name"]}")
        print(f"{result["birthday"]}")
        print(f"{result["class"]}")
        print("")
