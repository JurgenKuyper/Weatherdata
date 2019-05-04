# url = "http://192.168.178.10/?JSON"
import json, requests, time, subprocess, os, threading
from datetime import datetime
from tkinter import *
import matplotlib.pyplot as plt
weatherList = []
jsonDataList = [[],[]]
master = Tk()
screeny = 25
#creating text screen for non-int data
text = Text(master)
Sbar = Scrollbar(master)
Sbar.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)

def connection():
    f= open("running.txt","w")
    f.close()
    try:
        response = requests.get("http://192.168.178.10/?JSON",timeout=5)
        with open("datastore.json", "w") as filehandle:  
            filehandle.write(response.text)
        with open('datastore.json', 'r') as filehandle:  
            weatherList = json.loads(filehandle.read())
        for data in weatherList:
            if data['title'] == "DateTime" and data["value"] not in jsonDataList[1]:
                for Data in weatherList:
                    jsonDataList[1].append(Data['value'])
        print(jsonDataList)
        os.remove("running.txt")
        t = threading.Timer(15.0, getData)
        t.start()
    except requests.exceptions.ReadTimeout:
        print("readtimedout")
        connection()
    except requests.exceptions.ConnectTimeout:
        print("connectTimeOut")
        connection()

def getData():
    #print(time1[5])
    try:
        with open("running.txt", "r") as File:
            print(File.read())
    except FileNotFoundError:
        connection()
    #print(str(jsonDataList[1][1]))

def showData(d,Type):
    #getData()
    if plt.fignum_exists(num=1):
            plt.close()
    if Type == "Graph":
        x = []
        y = []
        for z in range(0,int(len(jsonDataList[1])/49)):
            x.append(str(jsonDataList[1][z*49]))
            print(jsonDataList[1][z*49])
            y.append(str(jsonDataList[1][d+(49*z)]))
        textData = str(jsonDataList[0][d]),x,y, '\n'
        text.insert(END,textData)
        del textData
        plt.plot(x,y)
        plt.show()
    else:
        textData = str(jsonDataList[0][d]), str(jsonDataList[1][d]) + '\n'
        print(str(textData))
        text.insert(END,textData)
        del textData

try:
    os.remove("running.txt")
except FileNotFoundError:
    print("done")
responseOld = requests.get("https://raw.githubusercontent.com/JurgenMK/Weatherdata/master/dataTest.json")
oldWeatherList = json.loads(responseOld.text)
for data in oldWeatherList:
    if data['title'] not in jsonDataList[0]:
        jsonDataList[0].append(data['title'])
for data in oldWeatherList:
    jsonDataList[1].append(data['value'])
with open("jsonDataList.txt", "w") as f:
    f.write(str(jsonDataList))
getData()
t = threading.Timer(15.0, getData)
t.start()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("SensorData")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)
        dateButton = Button(self, text = "Date",command= lambda: showData(0,"noGraph"))
        tempOutButton = Button(self, text = "Temperature Outside",command= lambda: showData(1,"Graph"))
        minTempTButton = Button(self, text = "Min Temperature Time",command= lambda: showData(2,"noGraph"))
        minTempVButton = Button(self, text = "Min Temperature Value",command= lambda: showData(3,"Graph"))
        maxTempTButton = Button(self, text = "Max Temperature Time",command= lambda: showData(4,"noGraph"))
        maxTempVButton = Button(self, text = "Max Temperature Value",command= lambda: showData(5,"Graph"))
        tempOutMButton = Button(self, text = "Temperature Outside Mast",command= lambda: showData(6,"Graph"))
        tempInButton = Button(self, text = "Temperature Inside",command= lambda: showData(7,"Graph"))
        humidInButton = Button(self, text = "Humidity Inside",command= lambda: showData(8,"Graph"))
        WifiTempButton = Button(self, text = "Temperature Wifimodule 1m",command= lambda: showData(9,"Graph"))
        wifiBatButton = Button(self, text = "Battery Wifimodule",command= lambda: showData(10,"Graph"))
        humidOutButton = Button(self, text = "Humidity Outside",command= lambda: showData(11,"Graph"))
        humidDewButton = Button(self, text = "Humidity Dewpoint Outside",command= lambda: showData(12,"Graph"))
        tempHumOutButton = Button(self, text = "Temperature Humiditysensor Outside",command= lambda: showData(13,"Graph"))
        avgAirPrButton = Button(self, text = "Average Airpressure",command= lambda: showData(14,"Graph"))
        avgAirdTButton = Button(self, text = "Average Airpressure Over Time",command= lambda: showData(15,"Graph"))
        airPressTendButton = Button(self, text = "Airpressure Tendency",command= lambda: showData(16,"Graph"))
        lightOutButton = Button(self, text = "LightLevel Outside",command= lambda: showData(17,"Graph"))
        lightInButton = Button(self, text = "LightLevel Inside",command= lambda: showData(18,"Graph"))
        windSpdButton = Button(self, text = "WindSpeed",command= lambda: showData(19,"Graph"))
        windMin15sButton = Button(self, text = "Minimum Windspeed 15s",command= lambda: showData(20,"Graph"))
        windMax15sButton = Button(self, text = "Maximum Windspeed 15s",command= lambda: showData(21,"Graph"))
        windMax15mButton = Button(self, text = "Maximum Windspeed 15m",command= lambda: showData(22,"Graph"))
        windVane15sButton = Button(self, text = "WindVane Position 15s",command= lambda: showData(23,"noGraph"))
        windDir15sButton = Button(self, text = "WindDirection 15s",command= lambda: showData(24,"noGraph"))
        windVane15mButton = Button(self, text = "WindVane Position 15m",command= lambda: showData(25,"noGraph"))
        windDir15mButton = Button(self, text = "WindDirection 15m",command= lambda: showData(26,"noGraph"))
        windSpdAvgButton = Button(self, text = "Average WindSpeed",command= lambda: showData(27,"Graph"))
        windSpd15mButton = Button(self, text = "Average WindSpeed 15m",command= lambda: showData(28,"Graph"))
        windSpd12hButton = Button(self, text = "Average WindSpeed 12h",command= lambda: showData(29,"Graph"))
        rain15sButton = Button(self, text = "Rain 15s",command= lambda: showData(30,"Graph"))
        rain3hButton = Button(self, text = "Rain 3h",command= lambda: showData(31,"Graph"))
        rain24hButton = Button(self, text = "Rain 12h",command= lambda: showData(32,"Graph"))
        mainsFrqButton = Button(self, text = "Mains Frequency",command= lambda: showData(33,"Graph"))
        mainsVolButton = Button(self, text = "Mains Voltage",command= lambda: showData(34,"Graph"))
        solarCurrButton = Button(self, text = "Solar Current",command= lambda: showData(35,"Graph"))
        solarPFButton = Button(self, text = "Solar PowerFactor",command= lambda: showData(36,"Graph"))
        luxSmlPnlButton = Button(self, text = "Lux Small SolarPanel",command= lambda: showData(37,"Graph"))
        dawnButton = Button(self, text = "DawnTime",command= lambda: showData(38,"noGraph"))
        duskButton = Button(self, text = "DuskTime",command= lambda: showData(39,"noGraph"))
        solar12hButton = Button(self, text = "Solar Genned 12h",command= lambda: showData(40,"Graph"))
        water24hButton = Button(self, text = "WaterUsage 24h",command= lambda: showData(41,"Graph"))
        gas24hButton = Button(self, text = "GasUsage 24h",command= lambda: showData(42,"Graph"))
        avg15sButton = Button(self, text = "Averages 15s",command= lambda: showData(43,"Graph"))
        unoMillButton = Button(self, text = "Uno Millis",command= lambda: showData(44,"Graph"))
        unoOntimeButton = Button(self, text = "Uno Ontime",command= lambda: showData(45,"noGraph"))
        megaMillButton = Button(self, text = "Mega Millis",command= lambda: showData(46,"Graph"))
        megaOntimeButton = Button(self, text = "Mega Ontime",command= lambda: showData(47,"noGraph"))
        megaTimeButton = Button(self, text = "Mega DateTime",command= lambda: showData(48,"noGraph"))
        # placing the button on my window
        quitButton.place(x=1280-30, y=0)
        dateButton.place(x=0,y=0)
        tempOutButton.place(x=0,y=screeny)
        minTempTButton.place(x=0,y=screeny*2)
        minTempVButton.place(x=0,y=screeny*3)
        maxTempTButton.place(x=0,y=screeny*4)
        maxTempVButton.place(x=0,y=screeny*5)
        tempOutMButton.place(x=0,y=screeny*6)
        tempInButton.place(x=0,y=screeny*7)
        humidInButton.place(x=0,y=screeny*8)
        WifiTempButton.place(x=0,y=screeny*9)
        wifiBatButton.place(x=0,y=screeny*10)
        humidOutButton.place(x=0,y=screeny*11)
        humidDewButton.place(x=0,y=screeny*12)
        tempHumOutButton.place(x=0,y=screeny*13)
        avgAirPrButton.place(x=0,y=screeny*14)
        avgAirdTButton.place(x=0,y=screeny*15)
        airPressTendButton.place(x=0,y=screeny*16)
        lightOutButton.place(x=0,y=screeny*17)
        lightInButton.place(x=0,y=screeny*18)
        windSpdButton.place(x=0,y=screeny*19)
        windMin15sButton.place(x=0,y=screeny*20)
        windMax15sButton.place(x=0,y=screeny*21)
        windMax15mButton.place(x=0,y=screeny*22)
        windVane15sButton.place(x=0,y=screeny*23)
        windDir15sButton.place(x=0,y=screeny*24)
        windVane15mButton.place(x=0,y=screeny*25)
        windDir15mButton.place(x=0,y=screeny*26)
        windSpdAvgButton.place(x=0,y=screeny*27)
        windSpd15mButton.place(x=0,y=screeny*28)
        windSpd12hButton.place(x=0,y=screeny*29)
        rain15sButton.place(x=230,y=0)
        rain3hButton.place(x=230,y=screeny)
        rain24hButton.place(x=230,y=screeny*2)
        mainsFrqButton.place(x=230,y=screeny*3)
        mainsVolButton.place(x=230,y=screeny*4)
        solarCurrButton.place(x=230,y=screeny*5)
        solarPFButton.place(x=230,y=screeny*6)
        luxSmlPnlButton.place(x=230,y=screeny*7)
        dawnButton.place(x=230,y=screeny*8)
        duskButton.place(x=230,y=screeny*9)
        solar12hButton.place(x=230,y=screeny*10)
        water24hButton.place(x=230,y=screeny*11)
        gas24hButton.place(x=230,y=screeny*12)
        avg15sButton.place(x=230,y=screeny*13)
        unoMillButton.place(x=230,y=screeny*14)
        unoOntimeButton.place(x=230,y=screeny*15)
        megaMillButton.place(x=230,y=screeny*16)
        megaOntimeButton.place(x=230,y=screeny*17)
        megaTimeButton.place(x=230,y=screeny*18)
    def client_exit(self):
        if plt.fignum_exists(num=1):
            plt.close()
        exit()
root = Tk()
root.geometry("1280x720+800+0")
app = Window(root)
root.mainloop()
