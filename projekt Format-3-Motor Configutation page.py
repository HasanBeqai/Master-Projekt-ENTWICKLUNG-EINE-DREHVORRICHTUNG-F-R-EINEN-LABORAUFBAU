from tkinter import *
import tkinter  as tk
import datetime as dt
import time
from tkinter import font
from tkinter import ttk

#*********************************************************************************************************#
# Ganz Fenster erstellen:
#*********************************************************************************************************#
app= tk.Tk() 
#app.geometry('760x700')
app.title("Schrittmotor Steuerung mit GUI - Menü")
app.grid_rowconfigure(0, weight=1) #Konfigurieren Sie die Seitenbreite entsprechend der Anzahl der Spalten
app.grid_columnconfigure(0, weight=1)#Konfigurieren Sie die Seitenlänge entsprechend der Anzahl der Zeilen

#Definiere die Variablen:

txt = StringVar()#diese Variable wird in der Methode "clock_time()" verwendet, um immer Datum und Uhrzeit zu aktualisieren.
fnt = font.Font(family = "helvetica",size=20, weight ="bold")#diese Schriftart wird in der App verwendet.
#*********************************************************************************************************#

# Motor Seite:

#*********************************************************************************************************#
# function to open a new window
# on a button click
def openMotorWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(app)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Motor Status and Configuration") 
    #Tabs
    tabControl = ttk.Notebook(newWindow)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='Motor Status')
    tabControl.add(tab2, text ='Run Motor')
    tabControl.pack(expand = 1, fill ="both")
    #in Tab 1:
    content1 = tk.Frame(tab1,borderwidth=5, relief="ridge")
    fram1 =tk.Frame(tab1,borderwidth=5, relief="ridge", bg='#A5FF33')
    lb11=tk.Label(fram1, borderwidth=5, relief="ridge",text="\nMaster\n Projekt" +
             "\n\n Schrittmotor\n Steuerung\nGUI",font = fnt)
    lb11.config(anchor=CENTER)
    lb21 = tk.Label(fram1,borderwidth=5, relief="ridge",textvariable=txt, font = fnt,
               foreground= "black")
    lb21.config(anchor=CENTER)
    lb31= tk.Label(fram1,borderwidth=5, relief="ridge",text="Westfälische\n Hochschule\n Gelsenkirchen", font = fnt,
               foreground= "black")
    lb31.config(anchor=CENTER)
    lb41=tk.Label(fram1,text="\n\n \n\n ", bg='#A5FF33')
    lb51=tk.Label(fram1,text="\n\n \n\n ", bg='#A5FF33')

    frame3=tk.Frame(content1,borderwidth=5)
    img1= PhotoImage(file='c.png')
    lb61=tk.Label(frame3,image=img1)
   

    #Grid und Layouts organisieren in Tab1:
    content1.grid(column=0, row=0, padx=10, pady=5)
    fram1.grid(column=0, row=0, padx=10, pady=5)
    lb21.grid(column= 0, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
    lb51.grid(column= 0, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
    lb11.grid(column=0, row=4, columnspan=2, rowspan=2, padx=10, pady=5)
    lb41.grid(column= 0, row=6, columnspan=2, rowspan=2, padx=15, pady=5)
    lb31.grid(column =0, row =8, columnspan=2, rowspan=2, padx=10, pady=5)
    lb61.grid(column=2, row= 0,columnspan=6, rowspan=4, padx=10, pady=5)
    #in Tab 2:
    content1 = tk.Frame(tab2,borderwidth=5, relief="ridge")
    fram1 =tk.Frame(tab2,borderwidth=5, relief="ridge", bg='#A5FF33')
    lb11=tk.Label(fram1, borderwidth=5, relief="ridge",text="\nMaster\n Projekt" +
             "\n\n Schrittmotor\n Steuerung\nGUI",font = fnt)
    lb11.config(anchor=CENTER)
    lb21 = tk.Label(fram1,borderwidth=5, relief="ridge",textvariable=txt, font = fnt,
               foreground= "black")
    lb21.config(anchor=CENTER)
    lb31= tk.Label(fram1,borderwidth=5, relief="ridge",text="Westfälische\n Hochschule\n Gelsenkirchen", font = fnt,
               foreground= "black")
    lb31.config(anchor=CENTER)
    lb41=tk.Label(fram1,text="\n\n \n\n ", bg='#A5FF33')
    lb51=tk.Label(fram1,text="\n\n \n\n ", bg='#A5FF33')
    
    #Grid und Layouts organisieren:
    content1.grid(column=0, row=0,columnspan=8, rowspan=8, padx=10, pady=5)
    fram1.grid(column=0, row=0, padx=10, pady=5)
    lb21.grid(column= 0, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
    lb51.grid(column= 0, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
    lb11.grid(column=0, row=4, columnspan=2, rowspan=2, padx=10, pady=5)
    lb41.grid(column= 0, row=6, columnspan=2, rowspan=2, padx=15, pady=5)
    lb31.grid(column =0, row =8, columnspan=2, rowspan=2, padx=10, pady=5)
#*********************************************************************************************************#
#*********************************************************************************************************#

# Menu:

#*********************************************************************************************************#

menubar = tk.Menu(app)

homemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=homemenu)
#homemenu.add_cascade(label="Exit",command=app.quit())

#Addieren Sie andere Seite zum Menü heißt "Motor Control"
#diese Seite hat zwei Teilen, die erste heißt "Motor Status check",
# die zeigt, am welchem Winkel der Motor zurzeit ist,
# die zweite Seite lässt der Benutzer den Motor winkel anderen. 

MotorControl=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Motor Control", menu=MotorControl)
MotorControl.add_command(label="Motor Status", command = openMotorWindow)
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


# Home Seite:

#*********************************************************************************************************#


#die Methoden definieren:

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
    else:
        b1.config(text='      ON       ')
#Dies ist eine Umschaltmethode zwischen Ein und Aus. So wird der Motor ein- und ausgeschaltet.


        
#Widgets erstellen:
        
content = tk.Frame(app,borderwidth=5, relief="ridge")

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
img1= PhotoImage(file='img1.png')
Label(frame1,image=img1).pack()


b1 = Button(content, text = "        OFF      ",borderwidth=5, relief="ridge",font = fnt, command=Simpletoggle)
b1.config(anchor=W)
b2 = Button(content, text = "Motor Status\n& Configuration",borderwidth=5, relief="ridge",font = fnt, command = openMotorWindow)
lb4 =tk.Label(content,text="\"Press ON to turn on the Motor \n and OFF to turn it off\"") 
lb4.config(font=("Courier", 10))
lb5 =tk.Label(content,text="\"Here you can check at which\n angle currently is the motor\n"+
              " and change its angle\"") 
lb5.config(font=("Courier", 10))
content1 = tk.Frame(app,borderwidth=5, relief="ridge")
lb7=tk.Label(content1,text="This project is developed by:\nHasan Beqai [202020400]\n"+
             "Saief Fattoum [202020286] ",font = fnt, foreground= "black")
lb8=tk.Label(content1, text="Project Supervisor: \n Prof. Dr. Martin Pollakowski",font = fnt, foreground= "black")

#Grid und Layouts organisieren:

content.grid(column=0, row=0, padx=10, pady=5)
frame.grid(column=0, row=0, columnspan=4, rowspan=2,padx=5, pady=5)
lb1.grid(column= 5, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
lb2.grid(column=7, row=0, columnspan=2, rowspan=2, padx=10, pady=5)
lb3.grid(column=0, row=2,columnspan=8, rowspan=1, padx=10, pady=5)
b1.grid(column=1, row= 3,columnspan=1, rowspan=1)
lb4.grid(column=1, row=4,columnspan=1, rowspan=1)
b2.grid(column=1, row= 5,columnspan=1, rowspan=1)
lb5.grid(column=1, row=6,columnspan=1, rowspan=1)
frame1.grid(column=3, row= 3,columnspan=6, rowspan=4, padx=10, pady=5)
content1.grid(column=0, row=6,columnspan=2, rowspan=2, padx=10, pady=10)
lb7.grid(column=0, row=6,padx=115)
lb8.grid(column=3, row=6, columnspan=2, padx=115)




app.mainloop()

