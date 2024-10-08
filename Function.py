import requests
from dotenv import load_dotenv
import datetime
import os
import json

load_dotenv()
api_token = os.getenv('API_TOKEN')


def api_call(base,date,api_token):
    url = f"https://data.fixer.io/api/latest?access_key={api_token}"
    querry = {"base":f"{base}","date":f"{date}"}
    response = requests.get(url,params=querry)
    return response.json()

def create_file(api_token):
    date_now = datetime.date.today()
    data = api_call("EUR",date_now,api_token)
    file = f"{date_now}-ECHANGE-TAUX.json"
    with open(file,'w') as file :
        json.dump(data,file,indent=4)
    print(f"{file} creee")

def exists_file(file):
    return os.path.exists(file)

def empty_file(file):
    return os.path.getsize(file) == 0 
   
    
def load_json_file(file):
    with open(file, 'r') as json_file:
        data = json.load(json_file) 
    return data

def convert(): 
    date_now = datetime.date.today()
    file = f"{date_now}-ECHANGE-TAUX.json"
    if exists_file(file):
        if not empty_file(file):
            data = load_json_file(file)
        else:
            create_file(api_token)
            convert()
            return
    else:
        create_file(api_token)
        convert()
        return
    return data 
  
    


        


