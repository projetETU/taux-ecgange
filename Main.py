import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('API_TOKEN')
print(api_token)