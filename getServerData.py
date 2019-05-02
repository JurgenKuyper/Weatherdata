import requests
import json
import os
f= open("running.txt","w")
def connection():
    f= open("running.txt","w")
    f.close()
    try:
        response = requests.get("http://192.168.178.10/?JSON",timeout=5)
        with open("datastore.json", "w") as filehandle:  
            filehandle.write(response.text)
        os.remove("running.txt")
    except requests.exceptions.ReadTimeout:
        print("readtimedout")
        connection()
    except requests.exceptions.ConnectTimeout:
        print("connectTimeOut")
        connection()
connection()