# url = "http://192.168.178.10/?JSON"
# import json, requests, time, subprocess, os
# from datetime import datetime
# from tkinter import *
# import matplotlib.pyplot as plt
# import threading
# weatherList = []
# jsonDataList = [[],[]]
# master = Tk()
# screeny = 25
# #creating text screen for non-int data
# text = Text(master)
# Sbar = Scrollbar(master)
# Sbar.pack(side=RIGHT, fill=Y)
# text.pack(side=LEFT, fill=Y)

# def connection():
#     f= open("running.txt","w")
#     f.close()
#     try:
#         response = requests.get("http://192.168.178.10/?JSON",timeout=5)
#         with open("datastore.json", "w") as filehandle:  
#             filehandle.write(response.text)
#         os.remove("running.txt")
#     except requests.exceptions.ReadTimeout:
#         print("readtimedout")
#         connection()
#     except requests.exceptions.ConnectTimeout:
#         print("connectTimeOut")
#         connection()

# def getData():
#     #print(time1[5])
#     try:
#         with open("running.txt", "r") as File:
#             print(File.read())
#     except FileNotFoundError:
#         generate = threading.Timer(15,connection())
#     #print(str(jsonDataList[1][1]))

# try:
#     os.remove("running.txt")
# except FileNotFoundError:
#     print("done")
# getData()
# while True:
#     with open('datastore.json', 'r') as filehandle:  
#         weatherList = json.loads(filehandle.read())
#         #print(weatherList)
#     responseOld = requests.get("https://raw.githubusercontent.com/JurgenMK/Weatherdata/master/dataTest.json")
#     oldWeatherList = json.loads(responseOld.text)
#     for data in weatherList:
#         if data['title'] not in jsonDataList[0]:
#             jsonDataList[0].append(data['title'])
#     for data in oldWeatherList:
#         jsonDataList[1].append(data['value'])
#     #if weatherlist[1][0] not in jsonDataList: 
#     for data in weatherList:
#         if data['title'] == "DateTime" and data["value"] not in jsonDataList[1]:
#             for Data in weatherList:
#                 jsonDataList[1].append(Data['value'])
#             print("jsonData: " + str(jsonDataList))
#             with open("jsonDataList.txt", "w") as f:
#                 f.write(str(jsonDataList))
import threading

def hello():
    print("hello, world")

t = threading.Timer(10.0, hello)
t.start() 
print("Hi")
i=10
i=i+20
print(i)
