
from tkinter import *
from tkinter import messagebox
import time
import datetime
from firebase import firebase
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S "

mission_name="battery/"# / - add at the end
recent_date=""
recent_time=""

firebase = firebase.FirebaseApplication('https://pytest-23462.firebaseio.com/')

def about_us():
    messagebox.showinfo("About us", "Developed by Naveen Maheswaran & Harishankar \nCopyright@ Space kidz India")


def fire_data():
    recent_date = firebase.get(mission_name+'recent_log/','date')
    recent_time = firebase.get(mission_name+'recent_log/','time')
    s=mission_name+recent_date+"/"+recent_time+"/"
    flightAlti = firebase.get(s, 'ALTITUDE')
    flightlati = firebase.get(s, 'LATITUDE')
    flightlongi = firebase.get(s, 'LONGITITUDE')
    flightvelo = firebase.get(s, "VELOCITY" )
    flighthead = firebase.get(s, 'HEADING')
    flighttemp = firebase.get(s, 'TEMPERATURE')
    flightpressure = firebase.get(s, 'PRESSURE')
    flighthumi = firebase.get(s, 'HUMIDITY')

    lati.set(flightlati)
    longi.set(flightlongi)
    alti.set(flightAlti)
    velo.set(flightvelo)
    head.set(flighthead)
    temp.set(flighttemp)
    pressure.set(flightpressure)
    humi.set(flighthumi)

    root.after(20000, fire_data)

    
root = Tk()
root.geometry("1100x700")
root.title("CrescentSAT Ground Station")
root.configure(background='black')

menubar = Menu(root)
root.configure(menu=menubar)
submenu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu_help)
submenu_help.add_command(label="About", command=about_us)
tops = Frame(root, width=1600, height=50, bg="black")

titleLabel = Label(tops, font=('Segoe UI',50, 'bold'), text="FLIGHT PARAMETERS", fg="steel blue", bg="black", bd="10", anchor='w')
titleLabel.grid(row=0,column=0)
tops.pack(side=TOP)

timeFrame = Frame(root,width=800, height=50, bg="black", relief=SUNKEN)
timeFrame = Frame(timeFrame, width=400, height=30,bg="red", relief=SUNKEN)

label_time_utc = Label(timeFrame,text="UTC : "+datetime.datetime.now(timezone('UTC')).strftime(format),bg="black",fg="steelblue", font=("Helvetica", 30))
label_time_utc.grid(row=0, column=0)

label_time_ist = Label(timeFrame,text="IST : "+datetime.datetime.now().strftime(format), bg="black",fg="steelblue", font=("Helvetica", 30))
label_time_ist.grid(row=0, column=3)

timeFrame.pack(side=LEFT)


Lparameter = Frame(root, width=770, height=600, bg="black", relief=SUNKEN)

lati = IntVar()
longi = IntVar()
alti = IntVar()
head = IntVar()
velo = IntVar()

latiLabel = Label(Lparameter, font=('Segoe UI', 20, ''), text="LATITUDE", fg="steel blue", bg="black", bd="20",anchor='w')
latiLabel.grid(row=0, column=0, sticky="E")
latiEntry = Entry(Lparameter, font=('Segoe UI', 20, 'bold'), textvariable=lati, bd=10, insertwidth=3, bg="steel blue", justify='center')
latiEntry.grid(row=0, column=1)

longiLabel = Label(Lparameter, font=('Segoe UI', 20, ''), text="LONGITUDE", fg="steel blue", bg="black", bd="20",anchor='w')
longiLabel.grid(row=1, column=0, sticky="E")
longiEntry = Entry(Lparameter, font=('Segoe UI', 20, 'bold'), textvariable=longi, bd=10, insertwidth=3,bg="steel blue", justify='center')
longiEntry.grid(row=1, column=1)

altiLabel = Label(Lparameter, font=('Segoe UI', 20, ''), text="ALTITUDE", fg="steel blue", bg="black", bd="20",anchor='w')
altiLabel.grid(row=2, column=0, sticky="E")
altiEntry = Entry(Lparameter, font=('Segoe UI', 20, 'bold'), textvariable=alti, bd=10, insertwidth=3,bg="steel blue", justify='center')
altiEntry.grid(row=2, column=1)
altisiLabel = Label(Lparameter, font=('Segoe UI', 20, ''), text="(Feet)", fg="steel blue", bg="black", bd="20",anchor='w')
altisiLabel.grid(row=2, column=2)

veloLabel = Label(Lparameter, font=('Segoe UI', 20, ''), text="VELOCITY", fg="steel blue", bg="black", bd="20",anchor='w')
veloLabel.grid(row=3, column=0, sticky="E")
veloEntry = Entry(Lparameter, font=('Segoe UI', 20, 'bold'), textvariable=velo, bd=10, insertwidth=3,bg="steel blue", justify='center')
veloEntry.grid(row=3, column=1)
velosiLabel = Label(Lparameter, font=('Segoe UI', 20, ''), text="kmph", fg="steel blue", bg="black", bd="20",anchor='w')
velosiLabel.grid(row=3, column=2)

Lparameter.pack(side=LEFT)




Rparameter = Frame(root, width=770, height=600, bg="black", relief=SUNKEN)

headLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="HEADING ", fg="steel blue", bg="black", bd="20", anchor='w')
headLabel.grid(row=0, column=0, sticky="E")
headEntry = Entry(Rparameter, font=('Segoe UI', 20, 'bold'), textvariable=head, bd=10, insertwidth=3,bg="steel blue", justify='center')
headEntry.grid(row=0, column=1)
headsiLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="(Degrees)", fg="steel blue", bg="black", bd="20",anchor='w')
headsiLabel.grid(row=0, column=2)

temp = IntVar()
pressure = IntVar()
humi = IntVar()


tempLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="TEMPERATURE", fg="steel blue", bg="black", bd="20",
                  anchor='w')
tempLabel.grid(row=1, column=0, sticky="E")
tempEntry = Entry(Rparameter, font=('Segoe UI', 20, 'bold'), textvariable=temp, bd=10, insertwidth=3,
                  bg="steel blue", justify='center')
tempEntry.grid(row=1, column=1)
tempsiLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="(C*)", fg="steel blue", bg="black", bd="20",
                    anchor='w')
tempsiLabel.grid(row=1, column=2)

pressureLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="PRESSURE", fg="steel blue", bg="black", bd="20",
                      anchor='w')
pressureLabel.grid(row=2, column=0, sticky="E")
pressureEntry = Entry(Rparameter, font=('Segoe UI', 20, 'bold'), text=pressure, bd=10, insertwidth=3,
                      bg="steel blue", justify='center')
pressureEntry.grid(row=2, column=1)
pressuresiLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="(Bar)", fg="steel blue", bg="black", bd="20",
                        anchor='w')
pressuresiLabel.grid(row=2, column=2)

humiLabel = Label(Rparameter, font=('Segoe UI', 20, ''), text="HUMIDITY", fg="steel blue", bg="black", bd="20",
                  anchor='w')
humiLabel.grid(row=3, column=0, sticky="E")
humiEntry = Entry(Rparameter, font=('Segoe UI', 20, 'bold'), text=humi, bd=10, insertwidth=3, bg="steel blue",
                  justify='center')
humiEntry.grid(row=3, column=1)

Rparameter.pack(side=RIGHT, padx=60)


root.after(20000,fire_data)
root.mainloop()


