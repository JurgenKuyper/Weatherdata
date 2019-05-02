# url = 'http://192.168.178.10/?LastReading'
import requests
while True:
    response = requests.get("http://192.168.178.10/?JSON", timeout=15)
    print(response)
    with open('datastore.txt', 'w') as filehandle:  
        filehandle.write(str(response))
