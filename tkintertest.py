import pickle
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
jsonDataList = [[],[]]
d = 1
x = []
y = []
master = Tk()
master.wm_title("Embedding in Tk")
with open ('listFile', 'rb') as fp:
    jsonDataList = pickle.load(fp)
for z in range(0,int(len(jsonDataList[1])/49)):
    x.append(str(jsonDataList[1][z*49]))
    print(jsonDataList[1][z*49])
    y.append(jsonDataList[1][d+(49*z)])
fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(111).plot(x,y)

canvas = FigureCanvasTkAgg(fig, master=master)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, master)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
def _quit():
    master.quit()
    master.destroy()
button = Button(master=master, text="Quit", command=_quit)
button.pack(side=BOTTOM)
master.mainloop()