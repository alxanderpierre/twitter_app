
import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVATAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}"
print(request_url)

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

data = json.loads(response.text)
print(type(data))


breakpoint()
