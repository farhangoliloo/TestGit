import requests

def Get_Price():
     
    res = requests.get("https://blockchain.info/ticker")
    response1 = res.json()['USD']['last']
    #response2 = res.json()['USD']["symbol"]
    return response1

        
