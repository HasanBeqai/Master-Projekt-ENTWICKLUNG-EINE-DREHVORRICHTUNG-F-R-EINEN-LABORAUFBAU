#*********************************************************************************************************#
#Biblioteken:
#*********************************************************************************************************#

from tkinter import *
import tkinter  as tk
import datetime as dt
import time
from tkinter import font
from tkinter import ttk
import webbrowser
import turtle
import RPi.GPIO as gpio

#*********************************************************************************************************#
# Ganz Fenster erstellen:
#*********************************************************************************************************#
app= tk.Tk() 
#app.geometry('760x700')
app.title("Schrittmotor Steuerung mit GUI - Menü")
app.grid_rowconfigure(0, weight=1) #Konfigurieren Sie die Seitenbreite entsprechend der Anzahl der Spalten
app.grid_columnconfigure(0, weight=1)#Konfigurieren Sie die Seitenlänge entsprechend der Anzahl der Zeilen

#*********************************************************************************************************#
#Definiere die Variablen:
#*********************************************************************************************************#

txt = StringVar()#diese Variable wird in der Methode "clock_time()" verwendet, um immer Datum und Uhrzeit zu aktualisieren.
fnt = font.Font(family = "helvetica",size=20, weight ="bold")#diese Schriftart wird in der App verwendet.
angle =0 # global varibale
tetaOld=0 # global variable
retVal = [] # global variable

startMotor="""
map S16 ControlWord as outpout 0x6040:00 
map U32 ProfileVelocity as outpout 0x6081:00 
map S32 TargetPosition as outpout 0x607A:00 
map U32 Inputs as input 0x60FD:00 
map S32 ActualPosition as input 0x6064:00

void user()
{
    od_write(0x6060,0x00, 1);
    od_write(0x01, 360);
    od_write(0x608F,0x02, 1);
    Out.ProfileVelocity=20;
    Out.TargetPosition=1000000000;
    Out.ControlWord=0x6;
    do {
        yield();
        }
    while ((od_read(0x6041, 0x00)& 0xEF) != 0x21);
    Out.ControlWord=0x7;
    do {
        yield();
        }
    while ((od_read(0x6041, 0x00)& 0xEF) !=0x23);
    Out.ControlWord=0x4F;
    do {
        yield();
        }
    while ((od_read(0x6041, 0x00)& 0xEF) !=0x27);
    Out.ControlWord=0x5F;
    yield();
    while(true)
    {
        if((In.Inputs & 0x1000)==0x10000)
        {
            Out.TargetPosition=In.ActualPosition + 180;
            Out.ProfileVelocity = 100;
            yield();
            Out.ControlWord=0x2F;
            yield();
            Out.ControlWord=0x3F;
            yield();
            while((In.Inputs & 0x10000)==0x10000)
            {
                yield();
                }
            }
        yield();
        }
    }
"""




x =23

gpio.setmode(gpio.BOARD)
gpio.setup(x,gpio.OUT)
#*********************************************************************************************************#
#Methoden:
#*********************************************************************************************************#


#include "wrapper.h"

'''
'''
def clock_time():
    time= dt.datetime.now()
    time= (time.strftime("Datum:\n %Y -%m -%d \n \n Uhr: \n %H:%M:%S"))
    txt.set(time)
    app.after(1000,clock_time)
#Diese Methode wird verwendet, um Datum und Uhrzeit einzustellen und zu aktualisieren.
app.after(100,clock_time)#Rufen Sie diese Methode nach 100 ms nach dem Erstellen der App auf.



def Simpletoggle():
    
    if b1.config('text')[-1] == '      ON       ':
        b1.config(text='      OFF       ')
        print(startMotor)
        StringToBytes(startMotor)
        print(retVal)
        gpio.output(x,retVal)
    else:
        b1.config(text='      ON       ')
#Dies ist eine Umschaltmethode zwischen Ein und Aus. So wird der Motor ein- und ausgeschaltet.

def run_motor():
    global angle
    global tetaOld
    tetaOld = float(angle)
    angle = winkel.get()
    return print("der Motor lauft mit Winkel " + str(angle))


def fw():
    teta = tetaOld+ float(angle)
    draw.left(teta)
    draw.forward(100)
    time.sleep(2)
    draw.reset()

def callback(url):
    webbrowser.open_new(url)

def StringToBytes(startMotor):
    global retVal
    for c in startMotor:
            retVal.append(ord(c))
    return retVal
#*********************************************************************************************************#
#Tabs erstellen:
#*********************************************************************************************************#
        
tabControl = ttk.Notebook(app)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3= ttk.Frame(tabControl)

tabControl.add(tab1, text ='Home')
tabControl.add(tab2, text ='Run Motor')
tabControl.add(tab3, text ='Motor Status')

tabControl.pack(fill ="both")


tab1.grid_rowconfigure(0, weight=1) #Konfigurieren Sie die Seitenbreite entsprechend der Anzahl der Spalten
tab1.grid_columnconfigure(0, weight=1)#Konfigurieren Sie die Seitenlänge entsprechend der Anzahl der Zeilen
tab2.grid_rowconfigure(0, weight=1) #Konfigurieren Sie die Seitenbreite entsprechend der Anzahl der Spalten
tab2.grid_columnconfigure(0, weight=1)#Konfigurieren Sie die Seitenlänge entsprechend der Anzahl der Zeilen
tab3.grid_rowconfigure(0, weight=1) #Konfigurieren Sie die Seitenbreite entsprechend der Anzahl der Spalten
tab3.grid_columnconfigure(0, weight=1)#Konfigurieren Sie die Seitenlänge entsprechend der Anzahl der Zeilen

#*********************************************************************************************************#
#in Tab 1: Home
#*********************************************************************************************************#
content = tk.Frame(tab1,borderwidth=5, relief="ridge", bg='#A5FF33')

frame = tk.Frame(content,borderwidth=5, relief="ridge")
img=PhotoImage(file='whlogo3.png')
Label(frame,image=img).pack()

lb1=tk.Label(content, borderwidth=5, relief="ridge",text="\n  Master Projekt" +
             "\n\n Schrittmotor Steuerung\nGUI",font = fnt)
lb1.config(anchor=CENTER)

lb2 = tk.Label(content,borderwidth=5, relief="ridge",textvariable=txt, font = fnt,
               foreground= "black")
lb2.config(anchor=CENTER)

lb3=tk.Label(content, text="Entwicklung eines Laboraufbaus mit Schrittmotor zur"+
             " Drehung von Messaufbauten",font = fnt, foreground= "black")

frame1=tk.Frame(content,borderwidth=5, relief="ridge")
img1= PhotoImage(file='img1.PNG')
Label(frame1,image=img1).pack()


b1 = Button(content, text = "        OFF      ",borderwidth=5, relief="ridge",font = fnt, command=Simpletoggle)
b1.config(anchor=W)
lb4 =tk.Label(content,text="\"Press ON to turn on the Motor \n and OFF to turn it off\"") 
lb4.config(font=("Courier", 10))
note = Label(content, text=" Hier können Sie die Projekt Dokumenatation  herenterladen", fg="blue", cursor="hand2")
note.config(font= ("Courier", 10))
note.bind("<Button-1>", lambda e: callback("/home/pi/Desktop/Projekt Beqai-Fattoum/Projekt/Bachelorarbeit_Kuruyamac.pdf"))
content1 = tk.Frame(tab1,borderwidth=5, relief="ridge", bg='#A5FF33')
lb7=tk.Label(content1,text="This project is developed by:\nHasan Beqai [202020400]\n"+
             "Saief Fattoum [202020286] ",font = fnt, foreground= "black")
lb8=tk.Label(content1, text="Project Supervisor: \n Prof. Dr. Martin Pollakowski",font = fnt, foreground= "black")


#Grid und Layouts organisieren:

content.grid(column=0, row=0, padx=10, pady=5)
frame.grid(column=0, row=0, columnspan=4, rowspan=2,padx=5, pady=5)
lb1.grid(column= 5, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
lb2.grid(column=7, row=0, columnspan=2, rowspan=2, padx=10, pady=5)
lb3.grid(column=0, row=2,columnspan=8, rowspan=1, padx=10, pady=5)
b1.grid(column=1, row= 4,columnspan=1, rowspan=1)
lb4.grid(column=1, row=5,columnspan=1, rowspan=1)
note.grid(column=1, row=6,columnspan=1, rowspan=1)
frame1.grid(column=3, row= 3,columnspan=6, rowspan=4, padx=10, pady=5)
content1.grid(column=0, row=6,columnspan=2, rowspan=2, padx=10, pady=10)
lb7.grid(column=0, row=6,padx=115)
lb8.grid(column=3, row=6, columnspan=2, padx=115)

#*********************************************************************************************************#
#in Tab 2: Motor Status
#*********************************************************************************************************#
fram3 =tk.Frame(tab2,borderwidth=5, relief="ridge", bg='#A5FF33')
lb11=tk.Label(fram3, borderwidth=5, relief="ridge",text="\nMaster\n Projekt" +
         "\n\n Schrittmotor\n Steuerung\nGUI",font = fnt)
lb11.config(anchor=CENTER)
lb21 = tk.Label(fram3,borderwidth=5, relief="ridge",textvariable=txt, font = fnt,
           foreground= "black")
lb21.config(anchor=CENTER)
lb31= tk.Label(fram3,borderwidth=5, relief="ridge",text="Westfälische\n Hochschule\n Gelsenkirchen", font = fnt,
           foreground= "black")
lb31.config(anchor=CENTER)
lb41=tk.Label(fram3,text="\n\n \n\n ", bg='#A5FF33')
lb51=tk.Label(fram3,text="\n\n \n\n ", bg='#A5FF33')


winkel_Label=tk.Label(fram3,text="Schreiben Sie die gewünschte Winkel",  font = fnt)
winkel=tk.Entry(fram3, font = fnt)
winkel.focus()
run =tk.Button(fram3, text= "Run Motor", command= run_motor,  font = fnt)
note = tk.Label(fram3, text=" \"bitte geben Sie ein Winkel zwischen 0 degree und 365 degree\"")

#Grid und Layouts organisieren in Tab1:
fram3.grid(column=0, row=0, padx=10, pady=5)
lb21.grid(column= 0, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
lb51.grid(column= 0, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
lb11.grid(column=0, row=4, columnspan=2, rowspan=2, padx=10, pady=5)
lb41.grid(column= 0, row=6, columnspan=2, rowspan=2, padx=15, pady=5)
lb31.grid(column =0, row =8, columnspan=2, rowspan=2, padx=10, pady=5)

winkel_Label.grid(column =4, row =3, columnspan=4, rowspan=2, padx=10, pady=5)
winkel.grid(column =8, row =3, columnspan=6, rowspan=2, padx=10, pady=5)
run.grid(column =8, row =5, columnspan=4, rowspan=2, padx=10, pady=5)
note.grid(column =4, row =5, columnspan=6, rowspan=2, padx=10, pady=5)
#*********************************************************************************************************#
#in Tab 3: Run Motor
#*********************************************************************************************************#
fram2 =tk.Frame(tab3,borderwidth=5, relief="ridge", bg='#A5FF33')
lb11=tk.Label(fram2, borderwidth=5, relief="ridge",text="\nMaster\n Projekt" +
         "\n\n Schrittmotor\n Steuerung\nGUI",font = fnt)
lb11.config(anchor=CENTER)
lb21 = tk.Label(fram2,borderwidth=5, relief="ridge",textvariable=txt, font = fnt,
           foreground= "black")
lb21.config(anchor=CENTER)
lb31= tk.Label(fram2,borderwidth=5, relief="ridge",text="Westfälische\n Hochschule\n Gelsenkirchen", font = fnt,
           foreground= "black")
lb31.config(anchor=CENTER)
lb41=tk.Label(fram2,text="\n\n \n\n ", bg='#A5FF33')
lb51=tk.Label(fram2,text="\n\n \n\n ", bg='#A5FF33')


fram4 = tk.Frame(fram2,borderwidth=5, relief="ridge", bg='#A5FF33')
flb1= tk.Label(fram4, text= "120", font = fnt,foreground= "black")
flb2= tk.Label(fram4, text= "100", font = fnt,foreground= "black")
flb3= tk.Label(fram4, text= " 90 ", font = fnt,foreground= "black")
flb4= tk.Label(fram4, text= " 80 ", font = fnt,foreground= "black")
flb5= tk.Label(fram4, text= " 60 ", font = fnt,foreground= "black")
flb0=tk.Label(fram4, text="135", font = fnt,foreground= "black")
flb01=tk.Label(fram4, text=" 45 ", font = fnt,foreground= "black")
flb6= tk.Label(fram4, text= "150", font = fnt,foreground= "black")
flb7= tk.Label(fram4, text= "170", font = fnt,foreground= "black")
flb8= tk.Label(fram4, text= "180", font = fnt,foreground= "black")
flb9= tk.Label(fram4, text= "190", font = fnt,foreground= "black")
flb10= tk.Label(fram4, text= "210", font = fnt,foreground= "black")
flb11= tk.Label(fram4, text= "225", font = fnt,foreground= "black")
flb12=tk.Label(fram4, text="250", font = fnt,foreground= "black")
flb13= tk.Label(fram4, text= "260", font = fnt,foreground= "black")
flb14= tk.Label(fram4, text= "270", font = fnt,foreground= "black")
flb15= tk.Label(fram4, text= "280", font = fnt,foreground= "black")
flb16= tk.Label(fram4, text= "300", font = fnt,foreground= "black")
flb17= tk.Label(fram4, text= "315", font = fnt,foreground= "black")
flb18= tk.Label(fram4, text= "330", font = fnt,foreground= "black")
flb19= tk.Label(fram4, text= "350", font = fnt,foreground= "black")
flb20= tk.Label(fram4, text= "  0  ", font = fnt,foreground= "black")
flb21= tk.Label(fram4, text= " 10 ", font = fnt,foreground= "black")
flb22= tk.Label(fram4, text= " 30 ", font = fnt,foreground= "black")


fram5= tk.Frame(fram4,borderwidth=5, relief="ridge", bg='#A5FF33')
canvas = tk.Canvas(fram5)
draw = turtle.RawTurtle(canvas)
Board_Button = tk.Button(fram2, text ="check the motor angle", command = fw)



#Grid und Layouts organisieren in Tab1:
fram2.grid(column=0, row=0, padx=10, pady=5)
lb21.grid(column= 0, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
lb51.grid(column= 0, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
lb11.grid(column=0, row=4, columnspan=2, rowspan=2, padx=10, pady=5)
lb41.grid(column= 0, row=6, columnspan=2, rowspan=2, padx=15, pady=5)
lb31.grid(column =0, row =8, columnspan=2, rowspan=2, padx=10, pady=5)
fram4.grid(column = 4, row = 0,columnspan=10, rowspan=10, padx=10, pady=5)
flb1.grid(column = 6, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb0.grid(column = 4, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb2.grid(column = 8, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb3.grid(column = 10, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb4.grid(column = 12, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb5.grid(column = 14, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb01.grid(column = 16, row = 0,columnspan=2, rowspan=2, padx=10, pady=5)
flb6.grid(column = 4, row = 2,columnspan=2, rowspan=2, padx=10, pady=5)
flb7.grid(column = 4, row = 4,columnspan=2, rowspan=2, padx=10, pady=5)
flb8.grid(column = 4, row = 6,columnspan=2, rowspan=2, padx=10, pady=5)
flb9.grid(column = 4, row = 8,columnspan=2, rowspan=2, padx=10, pady=5)
flb10.grid(column = 4, row = 10,columnspan=2, rowspan=2, padx=10, pady=5)
flb11.grid(column = 4, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb12.grid(column = 6, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb13.grid(column = 8, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb14.grid(column = 10, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb15.grid(column = 12, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb16.grid(column = 14, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb17.grid(column = 16, row = 12,columnspan=2, rowspan=2, padx=10, pady=5)
flb18.grid(column = 16, row = 10,columnspan=2, rowspan=2, padx=10, pady=5)
flb19.grid(column = 16, row = 8,columnspan=2, rowspan=2, padx=10, pady=5)
flb20.grid(column = 16, row = 6,columnspan=2, rowspan=2, padx=10, pady=5)
flb21.grid(column = 16, row = 4,columnspan=2, rowspan=2, padx=10, pady=5)
flb22.grid(column = 16, row = 2,columnspan=2, rowspan=2, padx=10, pady=5)
fram5.grid(column =7, row= 3, columnspan=8, rowspan=8, padx=10, pady=5)

canvas.grid(column =7, row= 3, columnspan=8, rowspan=8, padx=10, pady=5)

Board_Button.grid( row=0, column=2, sticky='nsew')


#*********************************************************************************************************#
#Run main application:
#*********************************************************************************************************#

app.mainloop()
app.user()
