import requests

url = "https://learn.codeit.kr/api/avatars"
headers = {"Content-Type": "application/json"}
body = {"hairType": "short2", "hairColor": "brown", "skin": "tone200", "clothes": "hoodie", "accessories": "earbuds"}
try:
    res = requests.post(url, headers=headers, json=body)
    data = res.json()
    print(data)
except Exception as e:
    print(e)