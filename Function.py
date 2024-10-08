import requests
import schedule
import datetime
import os
import json
class Function:

    def __init__(self) :
        self.date = datetime.date.today()



    def api_call(base,api_token):
        url = f"https://data.fixer.io/api/latest?access_key={api_token}"
        querry = {"base":f"{base}"}
        response = requests.get(url,params=querry)
        return response.json()

    def create_file(self):
        file = f"{self.date}-ECHANGE-TAUX.json"
        with open(file,'w') as file :
            json.dump(file,indent=4)
        print(f"{file} creee")

    # def set_file(api_token):

