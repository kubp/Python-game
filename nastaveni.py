#Jakub Dolezal V2C
#importy
import tkinter.simpledialog
import re  #import knihovny pro praci s retezcem
import nastaveni


class nastaveni:
    def __init__(self):
        setting=[0,1,2,3,4]
        try:
            lines = tuple(open("nastaveni.txt", 'r'))
        except:
            soubor=open("nastaveni.txt",'w')
            soubor.write("""name:anonym
zvuk:1
obrazek:0
zamichani:40
animace:1""")

            soubor.close()
       
       
       
        #cteni hodnot ze souboru
        for i in range(5):
            line=lines[i]
            line = re.sub('\n','', line)  
            line=re.split(":",line)#Rozdeleni hodnot
            line=line[1]
            setting[i]=line
        self.names=setting[0]
        self.zvuks=setting[1]
        self.obrazeks=setting[2]
        self.zamichanis=setting[3]
        self.animaces=setting[4]
    
    #vraci hodnoty, ktere jsou ulozeni v nastaveni.txt    
    def zvuk(self):
        return(self.zvuks)
        
    def name(self):
        return(self.names)
        
    def obrazek(self):
        return(self.obrazeks)
    
    def zamichani(self):
        return(self.zamichanis)
        
        
    def animace(self):
            return(self.animaces)    
        
        
   #Zmena nastaveni 
    def zvukSet(self):
        if(self.zvuks=="1"):
            self.zvuks="0"
        else:
            self.zvuks="1"     
        self.Update()
    
    def nameSet(self,hodnota):     
        self.names=hodnota 
        print(self.names)
        self.Update()
   
    def obrazekSet(self):     
        if(self.obrazeks=="1"):
            self.obrazeks="0"
        else:
            self.obrazeks="1"     
        self.Update()
   
   
    def animaceSet(self):     
        if(self.animaces=="1"):
            self.animaces="0"
        else:
            self.animaces="1"
        
        
        self.Update()
    
   
   #Samotne zapsani zmen do souboru
    def Update(self):
        soubor=open("nastaveni.txt",'w')
        soubor.write("name:"+self.names+"\nzvuk:"+self.zvuks+"\nobrazek:"+self.obrazeks+"\nzamichani:40\nanimace:"+self.animaces+"")
        soubor.close()        
    