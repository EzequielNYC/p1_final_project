import requests 
from config import key
import time
import csv 

stocks = ["AAPL","MSFT","ABNB","CVS"]

for stock in stocks:
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&limit=300&apiKey={key}"
    data = requests.get(url)
    json_data = data.json()

    results = json_data["results"]
    stock_data = []
    

    for closing in results:
        closing_price = closing["c"]
        date = time.strftime('%Y-%m-%d', time.localtime(closing['t']/1000))

        stock_dict = {
                    'Date':date,
                    'Closing_Price':closing_price
                    }
                
        stock_data.append(stock_dict)

    with open(f"{stock}.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=["Date","Closing_Price"])
        writer.writeheader()
        writer.writerows(stock_data)
