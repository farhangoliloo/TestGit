import requests

def Get_Price(price):
    if price == "قیمت بیت کوین":
        res = requests.get("https://blockchain.info/ticker")
        response1 = res.json()['USD']['last']
        response2 = res.json()['USD']["symbol"]
        print(response1,response2)
        
Get_Price("قیمت بیت کوین")