import requests
import json
import os
f= open("running.txt","w")
def connection():
    try:
        response = requests.get("http://192.168.178.10/?JSON",timeout=5)
        with open("datastore.json", "w") as filehandle:  
            filehandle.write(str(response.text))
        f.close()
    except requests.exceptions.ReadTimeout:
        print("readtimedout")
        connection()
    except requests.exceptions.ConnectTimeout:
        print("connectTimeOut")
        connection()
while True:
    connection()
#        weatherList = json.loads(response.text)