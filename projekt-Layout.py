#*********************************************************************************************************#
#Biblioteken:
#*********************************************************************************************************#

from tkinter import *
import tkinter  as tk
import datetime as dt
import time
from tkinter import font
from tkinter import ttk


# Importing tkPDFViewer to place pdf file in gui. 
# In tkPDFViewer library there is 
# an tkPDFViewer module. That I have imported as pdf 
from tkPDFViewer import tkPDFViewer as pdf

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

#*********************************************************************************************************#
#Methoden:
#*********************************************************************************************************#

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

#*********************************************************************************************************#
#Tabs erstellen:
#*********************************************************************************************************#
        
tabControl = ttk.Notebook(app)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3= ttk.Frame(tabControl)
tab4 =ttk.Frame(tabControl)

tabControl.add(tab1, text ='Home')
tabControl.add(tab2, text ='Motor Status')
tabControl.add(tab3, text ='Run Motor')
tabControl.add(tab4, text ='Dokumentation')
tabControl.pack(expand = 1, fill ="both")

#*********************************************************************************************************#
#in Tab 1: Home
#*********************************************************************************************************#

content = tk.Frame(tab1,borderwidth=5, relief="ridge")

frame = tk.Frame(content,borderwidth=5, relief="ridge", bg='#A5FF33')
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

frame1=tk.Frame(content,borderwidth=5, relief="ridge", bg='#A5FF33')
img1= PhotoImage(file='img1.png')
Label(frame1,image=img1).pack()


b1 = Button(content, text = "        OFF      ",borderwidth=5, relief="ridge",font = fnt, command=Simpletoggle, bg='#A5FF33')
b1.config(anchor=W)
b2 = Button(content, text = "Motor Status\n& Configuration",borderwidth=5, relief="ridge",font = fnt)
lb4 =tk.Label(content,text="\"Press ON to turn on the Motor \n and OFF to turn it off\"") 
lb4.config(font=("Courier", 10))
lb5 =tk.Label(content,text="\"Here you can check at which\n angle currently is the motor\n"+
              " and change its angle\"") 
lb5.config(font=("Courier", 10))
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
b1.grid(column=1, row= 3,columnspan=1, rowspan=1)
lb4.grid(column=1, row=4,columnspan=1, rowspan=1)
b2.grid(column=1, row= 5,columnspan=1, rowspan=1)
lb5.grid(column=1, row=6,columnspan=1, rowspan=1)

frame1.grid(column=3, row= 3,columnspan=6, rowspan=4, padx=10, pady=5)

content1.grid(column=0, row=6,columnspan=2, rowspan=2, padx=10, pady=10)
lb7.grid(column=0, row=6,padx=115)
lb8.grid(column=3, row=6, columnspan=2, padx=115)


#*********************************************************************************************************#
#in Tab 2: Motor Status
#*********************************************************************************************************#
content1 = tk.Frame(tab2,borderwidth=5, relief="ridge")
fram2 =tk.Frame(tab2,borderwidth=5, relief="ridge", bg='#A5FF33')
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

frame3=tk.Frame(content1,borderwidth=5)
img1= PhotoImage(file='c.png')
lb61=tk.Label(frame3,image=img1)


#Grid und Layouts organisieren in Tab1:
content1.grid(column=0, row=0, padx=10, pady=5)
fram2.grid(column=0, row=0, padx=10, pady=5)
lb21.grid(column= 0, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
lb51.grid(column= 0, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
lb11.grid(column=0, row=4, columnspan=2, rowspan=2, padx=10, pady=5)
lb41.grid(column= 0, row=6, columnspan=2, rowspan=2, padx=15, pady=5)
lb31.grid(column =0, row =8, columnspan=2, rowspan=2, padx=10, pady=5)
lb61.grid(column=2, row= 0,columnspan=6, rowspan=4, padx=10, pady=5)


img=PhotoImage(file='degree1.png')
label = Label(tab2,image=img)
label.place(relx = 0.5, rely = 0.5, anchor = 'center')


#*********************************************************************************************************#
#in Tab 3: Run Motor
#*********************************************************************************************************#
content2 = tk.Frame(tab3,borderwidth=5, relief="ridge")
fram3 =tk.Frame(tab3,borderwidth=5, relief="ridge", bg='#A5FF33')
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

frame4=tk.Frame(content2,borderwidth=5)
img1= PhotoImage(file='c.png')
lb61=tk.Label(frame4,image=img1)


#Grid und Layouts organisieren in Tab1:
content2.grid(column=0, row=0, padx=10, pady=5)
fram3.grid(column=0, row=0, padx=10, pady=5)
lb21.grid(column= 0, row=0, columnspan=2, rowspan=2, padx=15, pady=5)
lb51.grid(column= 0, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
lb11.grid(column=0, row=4, columnspan=2, rowspan=2, padx=10, pady=5)
lb41.grid(column= 0, row=6, columnspan=2, rowspan=2, padx=15, pady=5)
lb31.grid(column =0, row =8, columnspan=2, rowspan=2, padx=10, pady=5)
lb61.grid(column=2, row= 0,columnspan=6, rowspan=4, padx=10, pady=5)



#*********************************************************************************************************#
#in Tab 4: Dokumentation
#*********************************************************************************************************#
# creating object of ShowPdf from tkPDFViewer. 
v1 = pdf.ShowPdf() 
  
# Adding pdf location and width and height. 
v2 = v1.pdf_view(tab4, 
                 pdf_location = r"C:\Users\Beqai\Desktop\westfälische Hochschule\dritte Semester\Projekt\Bachelorarbeit_Kuruyamac.pdf",
                 width = 75, height = 100)
  
# Placing Pdf in my gui. 
v2.pack()

app.mainloop()








