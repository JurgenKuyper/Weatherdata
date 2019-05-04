import json, requests
import matplotlib.pyplot as plt
jsonDataList = [[],[]]
x = []
y = []
selector = 1
with open('datastore.json', 'r') as filehandle:  
    weatherList = json.loads(filehandle.read())
for data in weatherList:
    if data['title'] == "DateTime" and data["value"] not in jsonDataList[1]:
        for Data in weatherList:
            jsonDataList[1].append(Data['value'])
        for Data in weatherList:
            jsonDataList[1].append(Data['value'])
responseOld = requests.get("https://raw.githubusercontent.com/JurgenMK/Weatherdata/master/dataTest.json")
oldWeatherList = json.loads(responseOld.text)
for data in oldWeatherList:
    if data['title'] not in jsonDataList[0]:
        jsonDataList[0].append(data['title'])
for data in oldWeatherList:
    jsonDataList[1].append(data['value'])
print(jsonDataList)
#print(len(jsonDataList[1]) / 49)
for z in range(0,int(len(jsonDataList[1])/49)):
    x.append(str(jsonDataList[1][z*49]))
    y.append(str(jsonDataList[1][selector+(49*z)]))
    print(x,y)
plt.plot(x,y)
plt.show()
