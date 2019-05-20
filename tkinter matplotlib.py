# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import os, requests, json, threading, pickle
#root = Tk()

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
current = 0
values = ["Date & Time","Temperature Outside", "Min Temperature Time", "Minimal Temperature","Max Temperature Time", "Maximum Temperature","Temperature 4M","Temperature Inside","Humidity Inside","Temp 1M","Batterylevel 1M Module","Humidity Outside 3M","DewPoint","Temperature Humidity Sensor 3M","Avg. Air Pressure","Airpressure Difference","Air Pressure Tendency","Light Level Outside","Light Level Inside","Windspeed 15s","WindSpeed 15m","Max Windspeed 15s","Max Windspeed 5m","WindVaneValue 15s","windDirection 15s","WindVaneValue 15m","windDirection 15m","Average WindSpeed","WindSpeed 15m","windSpeed 12h","Rain 15s","Rain 3h","rain 24h","Mains Frequency","Mains Voltage","SolarCurrent","Solar PowerFactor","Lux 1m","Moment of Sunrise","Moment of Sunset","Whatt Generated 12h","WaterUsage 24h","GasUsage 24h","Averages Last 15s","Uno Millis","Uno-Ontime","Mega Millis","Mega-Ontime","MegaLocalTime"]
weatherList = []
jsonDataList = [[],[]]

def animate(i):
    if current is not 0 and current is not 2 and current is not 4 and current is not 24 and current is not 26 and current is not 38 and current is not 39 and current is not 48:
        x = []
        y = []
        a.clear()
        for z in range(0,int(len(jsonDataList[1])/49)):
            x.append(str(jsonDataList[1][z*49]))
            #print(jsonDataList[1][z*49])
            y.append(jsonDataList[1][current+(49*z)])
        a.plot(x, y)
    else:
        ...#textData = str(jsonDataList[0][current]), str(jsonDataList[1][current]), '\n'
        #print(str(textData))
        #text.insert(END,textData)
        #del textData
    print(current)

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
        print("data Retrieved")
        with open('listFile', 'wb') as fp:
            pickle.dump(jsonDataList, fp)
        os.remove("running.txt")
        t = threading.Timer(15.0, getData)
        t.start()
    except requests.exceptions.ReadTimeout:
        print("readtimeOut")
        connection()
    except:
        print("ConnectTimeOut")
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
            y.append(jsonDataList[1][d+(49*z)])
        #textData = str(jsonDataList[0][d]),x,y, '\n'
        #text.insert(END,textData)
        #del textData
        plt.plot(x,y)
        plt.show()
    else:
        textData = str(jsonDataList[0][d]), str(jsonDataList[1][d]) + '\n'
        print(str(textData))
        #text.insert(END,textData)
        #del textData

try:
    os.remove("running.txt")
except FileNotFoundError:
    print("done")
try:
    with open('listfile', 'rb') as readfile:
        jsonDataList = pickle.load(readfile)
    print(jsonDataList)
    # responseOld = requests.get("https://192.168.178.10/?JSON")
    # oldWeatherList = json.loads(responseOld.text)
    # for data in oldWeatherList:
    #     if data['title'] not in jsonDataList[0]:
    #         jsonDataList[0].append(data['title'])
    # for data in oldWeatherList:
    #     jsonDataList[1].append(data['value'])
    t = threading.Timer(15.0, getData)
    t.start()
except requests.exceptions.ConnectTimeout:
    print("connectTimeOut")
except requests.exceptions.ReadTimeout:
    print("readTimeOut")

class WeatherData(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Weather Data Visualisation")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
       
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Select graph:", font=LARGE_FONT)
        label.grid(column=1, row=0)
        self.grid_rowconfigure(5, weight=1,pad=1)
        self.grid_columnconfigure(1, weight=1,pad=1)
        def handler(event):
            global current
            current = Selection.current()
            value = values[current]
            print("current: ", current, "Value: ",value)

            #print(text_var.get())
        def exitprogram():
            with open('listfile', 'rb') as readfile:
                dataListToRemove = pickle.load(readfile)
                del dataListToRemove[1][0:len(dataListToRemove[1])-(49*2)]
            os.remove('listfile')
            with open('listfile', 'wb') as writingfile:
                    pickle.dump(dataListToRemove, writingfile)
            app.destroy()
        Selection = Combobox(self, state='readonly', width=30,values=values)
        Selection.bind('<<ComboboxSelected>>', handler)
        Selection.current(0)
        Selection.grid(column=1, row=1)
        TextButton = ttk.Button(self, text="Text Page", command=lambda: controller.show_frame(PageTwo))
        TextButton.grid(column=1,row=2)
        DataButton = ttk.Button(self, text="Data Page", command=lambda: controller.show_frame(PageThree))
        DataButton.grid(column=1, row=3)
        ExitButton = ttk.Button(self, text='exit program',command=exitprogram)
        ExitButton.grid(column=1,row=4)

class PageTwo(tk.Frame):
    def tmpCommand(self):
        self.var1.set(values[current])
        self.var2.set(jsonDataList[1][int(len(jsonDataList[1]))-(49-current)])
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.var1 = StringVar()
        self.var1.set('Hello')
        self.var2 = StringVar()
        data = jsonDataList[1][int(len(jsonDataList[1]))-(49-current)]
        self.var2.set(data)
        label = tk.Label(self, text="Text Page!", font=LARGE_FONT)
        label.grid(column = 1, row = 0)
        Data = tk.Label(self, textvariable = self.var1)
        Data.grid(column = 1, row = 1)
        Data = tk.Label(self, textvariable = self.var2)
        Data.grid(column = 1, row = 2)
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(column = 1, row = 3)
        button2 = ttk.Button(self, text="showData", command = self.tmpCommand)
        button2.grid(column = 1, row = 4)
        self.grid_rowconfigure(5, weight=1,pad=1)
        self.grid_columnconfigure(1, weight=1,pad=1)
        Tk.update(self)

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
app = WeatherData()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
