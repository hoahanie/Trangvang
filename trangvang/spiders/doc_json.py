import json
with open('out_bat_dong_san.json') as f:
    data = json.loads(f.read())
    for url in data:
        for n in url["url"]:
            print(n)
            