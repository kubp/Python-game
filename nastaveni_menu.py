#Jakub Dolezal V2C
#importy
from tkinter import *
import tkinter.messagebox
import webbrowser
import time
import winsound
import urllib.request 
import tkinter.simpledialog
import re
import nastaveni
import main_menu
import nastaveni_menu
import logika   
        
class nastaveni_menu:
    def __init__(self):
                
        
        self.okno=Tk()
        self.okno.title("Game of Squares")             
        self.okno.config(bg="white")
        self.jmeno=nastaveni.nastaveni()  #vycteni jmena z nastaveni.py
        
        #menu
        photo1 = PhotoImage(file="img/nastaveni-g.gif")
        self.entry2=Label(self.okno,text="Game",bd=0)
        self.entry2.config(image=photo1,width="410",height="80")
        self.entry2.grid(row=1, column=1,padx=85,pady="50")            
       
       
        photo2 = PhotoImage(file="img/hraci_mod.gif")
        self.entry2=Button(self.okno,bd=0,command=self.mod)
        self.entry2.config(image=photo2,width="250" ,height="45")
        self.entry2.grid(row=2, column=1,padx=111,pady=50)       
    
    
        photo3 = PhotoImage(file="img/zvuky.gif")
        self.entry2=Button(self.okno,bd=0,command=self.zvuk)
        self.entry2.config(image=photo3,width="160",height="35")
        self.entry2.grid(row=3, column=1,padx=111)       
    
        
        photo4 = PhotoImage(file="img/efekt.gif")
        self.entry2=Button(self.okno,bd=0,command=self.anim)
        self.entry2.config(image=photo4,width="146",height="55")
        self.entry2.grid(row=4, column=1,padx=111 , pady=50)       
       
       
        photo5 = PhotoImage(file="img/vysledky.gif")
        self.entry2=Button(self.okno,bd=0,command=self.vysledky)
        self.entry2.config(image=photo5,width="246",height="55")
        self.entry2.grid(row=5, column=1,padx=111 , pady=10)         

        
        
        
        
        
        zpet = PhotoImage(file="img/zpet.gif")
        self.entry2=Button(self.okno,bd=0,command=self.start_menu)
        self.entry2.config(image=zpet,width="140" ,height="35")
        self.entry2.place(relx=0.75,rely=0.9)              
       
      
        self.okno.maxsize(605,660)
        self.okno.minsize(605,660)          
        self.okno.mainloop()
  
  
    def start_menu(self):
        self.okno.destroy()
        main_menu.main_menu()
    
   #anim, zvuk, mod nastavuji v souboru nastaveni.py - zapisuje se do souboru
   
    def anim(self):
        tkinter.messagebox.showinfo('Zmena nastaveni','Zmenil jste nastaveni animace')   
        self.config=nastaveni.nastaveni() 
        self.config.animaceSet()
        
    def zvuk(self):
        tkinter.messagebox.showinfo('Zmena nastaveni','Zmenil jste nastaveni zvuku')           
        self.config=nastaveni.nastaveni() 
        self.config.zvukSet()
    
    def mod(self):
        tkinter.messagebox.showinfo('Zmena nastaveni','Zmenil jste nastaveni obrazku')           
        self.config=nastaveni.nastaveni()         
        self.config.obrazekSet()
    def vysledky(self):
        #otevre prohlizec k online vysledkum
        webbrowser.open("http://vysledky.pyw.be/"+self.jmeno.name())