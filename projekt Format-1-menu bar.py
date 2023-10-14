from tkinter import *
import tkinter as tk
from tkinter import font
import time
import datetime

#Erstellen Sie eine leere GUI mit Länge = 700 px
#und Breite = 500 px mit einem Titel "Schrittmotor Steuerung mit GUI - Menü"
#app ist der Name der Variable von GUI
app= tk.Tk() 
app.geometry('700x500')
app.title("Schrittmotor Steuerung mit GUI - Menü")
app.configure(bg= "white")
def clock_time():
    time= datetime.datetime.now()
    time= (time.strftime("Date: %Y -%m -%d \nTime: %H:%M:%S"))
    txt.set(time)
    app.after(1000,clock_time)

app.after(1000,clock_time)

#Erstellen Sie einen menu bar mit ein Seite heißt Home
menubar = tk.Menu(app)
homemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=homemenu)
#homemenu.add_cascade(label="Exit",command=app.quit)


#Addieren Sie andere Seite zum Menü heißt "Motor Control"
#diese Seite hat zwei Teilen, die erste heißt "Motor Status check",
# die zeigt, am welchem Winkel der Motor zurzeit ist,
# die zweite Seite lässt der Benutzer den Motor winkel anderen. 
MotorControl=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Motor Control", menu=MotorControl)
MotorControl.add_command(label="Motor Status check")
MotorControl.add_command(label="Run Motor")


#Addieren Sie andere Seite zum Menü heißt "About the Project"
#diese Seite hat zwei Teilen, die erste heißt "Project Documentation",
# die die Documenations von Projekt zeigt
# die zweite Seite zeigt Informationen über den Entwickelern von GUI-App. 
aboutmenu =tk.Menu(menubar)
menubar.add_cascade(label="About the Project", menu=aboutmenu)
aboutmenu.add_command(label="Project Documentation")
aboutmenu.add_command(label="Project Authors")

app.config(menu=menubar)
txt = StringVar()
fnt = font.Font(family = "helvetica",size=10, weight ="bold")

lbl = tk.Label(app,textvariable=txt, font = fnt, foreground= "black",background= "white")
lbl.place(relx=0.8,rely=0.1, anchor=CENTER)

app.mainloop()


