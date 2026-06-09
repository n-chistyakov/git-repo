import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_key = os.getenv("FMP_API_KEY")

url = f'https://financialmodelingprep.com/stable/quote?symbol=AAPL&apikey={api_key}'
response = requests.get(url)
# print(response.status_code)
try:
    data = response.json()
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print("Error decoding JSON response")
