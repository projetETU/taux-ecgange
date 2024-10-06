import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('API_TOKEN')

url = f"https://data.fixer.io/api/latest?access_key={api_token}"
querry = {"base":"EUR","symbols":"MGA"}

response = requests.get(url,params=querry)

print(response.json())