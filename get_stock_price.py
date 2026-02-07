import requests

BASE_URL = "https://openapivts.koreainvestment.com:29443"
APPKEY = "..."
APPSECRET = "..."

ACCESS_TOKEN = "..."

url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
headers = {
    "content-type": "application/json; charset=utf-8",
    "authorization": f"Bearer {ACCESS_TOKEN}",
    "appkey": APPKEY,
    "appsecret": APPSECRET,
    "tr_id": "FHKST03010200",
    "custtype": "P"
}
params = {
    "FID_ETC_CLS_CODE": "",
    "FID_COND_MRKT_DIV_CODE": "J",
    "FID_INPUT_ISCD": "005930",
    "FID_INPUT_HOUR_1": "093000",
    "FID_PW_DATA_INCU_YN": "Y"
}
try:
    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    print(data)
except Exception as e:
    print(e)