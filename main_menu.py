#Jakub Dolezal V2C
#importy
import random
from tkinter import *
import tkinter.messagebox
import time
import winsound
import urllib.request 
import tkinter.simpledialog
import re
import nastaveni
import main_menu
import nastaveni_menu
import logika   
        
class main_menu:
    def __init__(self):
        
       #nastaveni okna
        self.nastaveniOkno=Tk()
        self.nastaveniOkno.title("Game of Squares")             
        self.nastaveniOkno.config(bg="white")
        #nacteni jmena z nastaveni.txt
        self.jmeno=nastaveni.nastaveni()
 
       
      
        #menu
        photo1 = PhotoImage(file="img/main-g.gif")
        self.entry2=Label(self.nastaveniOkno,text="Game",bd=0)
        self.entry2.config(image=photo1,width="410",height="50")
        self.entry2.grid(row=1, column=1,padx=85,pady="50")       
       
       
        photo2 = PhotoImage(file="img/hrat.gif")
        self.entry2=Button(self.nastaveniOkno,text="start",bd=0,command=self.start_game)
        self.entry2.config(image=photo2,width="234",height="50")
        self.entry2.grid(row=2, column=1,padx=111,pady=50)       
        self.entry2.bind('<Enter>',self.move)
        self.entry2.bind('<Leave>',self.deleteTecka)
        
        
        photo3 = PhotoImage(file="img/nastaveni.gif")
        self.entry2=Button(self.nastaveniOkno,text="settings",bd=0, command=self.start_nastaveni)
        self.entry2.config(image=photo3,width="246.6",height="50")
        self.entry2.grid(row=3, column=1,padx=111)       
        self.entry2.bind('<Enter>',self.move)
        self.entry2.bind('<Leave>',self.deleteTecka)        
        
        
        photo4 = PhotoImage(file="img/konec.gif")
        self.entry2=Button(self.nastaveniOkno,text="exit",bd=0,command=self.nastaveniOkno.destroy)
        self.entry2.config(image=photo4,width="255",height="50")
        self.entry2.grid(row=4, column=1,padx=111 , pady=50)       
        self.entry2.bind('<Enter>',self.move)
        self.entry2.bind('<Leave>',self.deleteTecka)        
              
        
        self.photon=PhotoImage(file="img/tecka.gif")                             
        self.imgn=[0]
        self.imgn[0]=self.photon
        
        if(self.jmeno.name()=="anonym"):
            self.name = tkinter.simpledialog.askstring(self.nastaveniOkno,"Vase jmeno") 
            self.jmeno.nameSet(self.name)
        
        #Pevne dana velikost
        self.nastaveniOkno.maxsize(585,660)
        self.nastaveniOkno.minsize(585,660)          
        self.nastaveniOkno.mainloop()        
            
    #pohyb tecky u menu  
    def move(self, udalost):
        text=udalost.widget.cget('text')
        if(text=="start"):
            x=150
            y=212
        if(text=="settings"):
            x=150
            y=318
        if(text=="exit"):
            x=134
            y=420                 
        
        
        self.tecka=Label(self.nastaveniOkno,text="Hello",bd=0)
        self.tecka.config(image=self.imgn[0])
        self.tecka.place(x=x,y=y)            
        
    def deleteTecka(self, udalost):
        self.tecka.destroy()
   
    #spusteni hry
    def start_game(self):
        self.nastaveniOkno.destroy()
        logika.Logika()
        
    def start_nastaveni(self):
        self.nastaveniOkno.destroy()
        nastaveni_menu.nastaveni_menu()
          