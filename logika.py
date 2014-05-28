#Jakub Dolezal V2C
#importy
import random
from tkinter import *
import tkinter.messagebox
import time
import winsound
import urllib.request #Pro zapis do MySQL databaze pres GET
import tkinter.simpledialog
import re

import nastaveni
import main_menu
import nastaveni_menu
import logika   
import threading


class Logika:
    def __init__(self):
        #cteni hodnot z nastaveni.py
        self.zamichani=nastaveni.nastaveni()     
        self.zvuk=nastaveni.nastaveni()
        self.obrazek=nastaveni.nastaveni()
        self.jmeno=nastaveni.nastaveni()
        self.animace=nastaveni.nastaveni()
        
        self.okno=Tk()
        self.okno.title("Game of Squares")        
        self.okno.config(bg="grey")
        
        
        self.pole=[1,2,3,4,5,6,7,8,0] 
        self.porovnavacipole=[1,2,3,4,5,6,7,8,0]
        self.polex=[0,1,2,0,1,2,0,1,2] #Souradnice pro self.pole
        self.poley=[0,0,0,1,1,1,2,2,2]
       
        self.tah=0
        self.pocet=0
        poprve=1
        
        #Jmeno a oddelovaci cara
        self.jmenoL=Label(self.okno,width="14",height="2",text=self.jmeno.name(),bd=0, bg="white",relief=GROOVE)
        self.jmenoL.grid(row=4, column=2)          
        self.frame=Frame(height=2,bd=1,relief=SUNKEN,width=500)
        self.frame.place(relx=0.5, rely=0.90, anchor=CENTER)            
        
        
        #pri prvnim spusteni     
        if(poprve==1):
            self.cas=0
            poprve=0
            self.promichani()
            self.cas_c()
            self.okno.maxsize(317,380)
            self.okno.minsize(317,380)                   

            self.okno.mainloop()
    
            
    def promichani(self):
  
        self.pocet=self.pocet+1
        if(self.pocet<int(self.zamichani.zamichani())): #Zjisteni kolikrat promichat z nastaveni.py
            self.cas=0
            
            #Zjisteni jestli ma probihat animace mychani z nastaveni.py
            if(self.animace.animace()=="1"):
                self.okno.after(60,self.promichani) 
            else:   
                self.promichani()
            
            f=random.randint(0,8)
            ui=self.pole.index(0)
            #Nahodne promichani po tazich
            volba=random.randint(0,3)   
            
            if(volba==0):
                ui=ui+3
            if(volba==1):
                ui=ui-3
            if(volba==2):
                ui=ui-1
            if(volba==3):
                ui=ui+1
            if(ui in range(0,8)): #Ochrana proti vybrani spatneho indexu
                r=self.pole.index(0)
                self.pole[r]=self.pole[ui]
                self.pole[ui]=0
                
                if(self.zvuk.zvuk()=="1"):
                    winsound.Beep(250,100)
    
                #Obrazky 2 druhy - zapsane do pole
                if(self.obrazek.obrazek()=="0"):   
                    self.photo1=PhotoImage(file="img/0.gif" )
                    self.photo2=PhotoImage(file="img/1.gif" )
                    self.photo3=PhotoImage(file="img/2.gif" )
                    self.photo4=PhotoImage(file="img/3.gif" )
                    self.photo5=PhotoImage(file="img/4.gif" )
                    self.photo6=PhotoImage(file="img/5.gif" )
                    self.photo7=PhotoImage(file="img/6.gif" )
                    self.photo8=PhotoImage(file="img/7.gif" )
                    self.photo0=PhotoImage(file="img/8.gif" )
                else:
                    self.photo1=PhotoImage(file="img/0.gif" )
                    self.photo2=PhotoImage(file="img/o1.gif" )
                    self.photo3=PhotoImage(file="img/o2.gif" )
                    self.photo4=PhotoImage(file="img/o3.gif" )
                    self.photo5=PhotoImage(file="img/o4.gif" )
                    self.photo6=PhotoImage(file="img/o5.gif" )
                    self.photo7=PhotoImage(file="img/o6.gif" )
                    self.photo8=PhotoImage(file="img/o7.gif" )
                    self.photo0=PhotoImage(file="img/o8.gif" )                
                
                
                self.pim=[0,1,2,3,4,5,6,7,8]
                self.pim[0]=self.photo1        
                self.pim[1]=self.photo2  
                self.pim[2]=self.photo3   
                self.pim[3]=self.photo4   
                self.pim[4]=self.photo5  
                self.pim[5]=self.photo6   
                self.pim[6]=self.photo7   
                self.pim[7]=self.photo8   
                self.pim[8]=self.photo0   
                  
                for i in range(9):
                    #promichani indexu cisel
                    a=self.pole[i]
                    b=self.pole.index(a)  #Index prvku v poli           
                    f=self.polex[b]
                    g=self.poley[b]
           
                    self.entry2=Button(self.okno,width="8",height="4",text=a, bg="#000",bd=2,relief=GROOVE,cursor="pirate")
                    self.entry2.grid(row=g, column=f)
                    self.entry2.bind('<1>',self.core)
                    self.entry2.config(image=self.pim[a],width="100",height="100")
                 
                    if(a==0): #Kdzy je prvek 0
                        self.entry2=Button(self.okno,width="8",height="4",text=0,bd=0, bg="white", cursor="pirate")
                        self.entry2.grid(row=g, column=f)
                        self.entry2.bind('<1>',self.core)
                        self.entry2.config(image=self.pim[a],width="50",height="50")
                          


  
   
   
    def cas_c(self):
        self.thread=threading.Timer(1.0, self.cas_c)
        self.thread.start()
        
        self.cas=self.cas+1
        cas2=self.cas//60   #Zjisteni minut
        cas3=self.cas%60   
        cas2=str(cas2)
        if(len(cas2)==1):
            cas2=("0"+cas2)
       
            cas3=str(cas3)
        if(len(str(cas3))==1):
            cas3=("0"+cas3)      
        try:   #Ukoncovani vlakna pri zavreni okna
            self.casovac=Label(self.okno,width="14",height="2",text=str(cas2)+":"+str(cas3),bd=0, bg="white")
            self.casovac.grid(row=4, column=0,pady=30)
            self.casUpraven=(str(cas2)+":"+str(cas3))
                  
       
        except:
            self.thread.cancel()
    
    
    def getCas(self):
        return(self.casUpraven)
  
      
  
  
   
    def pocet_tahu(self):
        self.tah=self.tah+1 #Zvysi pocet tahu o 1
        return(self.tah)
   
   
   #logika posunu  tlacitek
    def core(self,udalost):
        text=udalost.widget.cget('text')#zjisteni textu na tlacitku
        text=int(text) 
        b=self.pole.index(text)            
        f=self.polex[b]
        g=self.poley[b]
       
        nula=self.pole.index(0) #index prvku kde je nula
        fn=self.polex[nula]
        gn=self.poley[nula]
        
        
        
        da=nula+3
        dg=nula-3
        dv=nula-1
        dr=nula+1
        #Kontrola rohu
        if((nula==0) or (nula==3) or (nula==6)):
            dv=-5
           
        if((nula==2) or (nula==5) or (nula==8)):
            dr=-5
           
        if((b==da) or (b==dg) or (b==dv) or (b==dr)):
           
            if(self.zvuk.zvuk()=="1"):
                #Zvuk pri tahu
                winsound.Beep(250,100)
                
            tahy="Tahy: "+str(self.pocet_tahu())
            #presunuti buttonu
            self.casovac=Label(self.okno,width="14",height="2",text=tahy,bd=0, bg="white",relief=GROOVE)
            self.casovac.grid(row=4, column=1)              
            
          
            
            self.entry2=Button(self.okno,width="8",height="4",text=text, bg="#000",bd=2,relief=GROOVE)
            self.entry2.grid(row=gn, column=fn)
            self.entry2.bind('<1>',self.core)
            self.entry2.config(image=self.pim[text],width="100",height="100")            
            
          
            self.entry2=Button(self.okno,width="8",height="4",text=0,bg="white",relief=GROOVE)
            self.entry2.grid(row=g, column=f)
            self.entry2.bind('<1>',self.core)
            self.entry2.config(image=self.pim[0],width="100",height="100")         
       
   
            self.pole[nula]=text
            self.pole[b]=0
                 
            if(self.pole==self.porovnavacipole):
                #
                if tkinter.messagebox.askyesno("Konec hry!","Chcete ulozit do online vysledku? \n Pocet tahu "+str(self.pocet_tahu())+ "\n Cas: "+ self.getCas()):
                    #Zapis vysledku do databaze
                    pristup = urllib.request.urlopen('http://vysledky.pyw.be/?add&name='+str(self.jmeno.name())+'&cas='+self.getCas()+'&tahy='+str(self.pocet_tahu()-1)+'')   
                   
                    
                    
                   
                    self.exit()             
                else: 
                  
                    self.exit()
   
              
              
    def exit(self):
        self.thread.cancel()  #Ukonceni aplikace
        self.okno.destroy()
      
        main_menu.main_menu()