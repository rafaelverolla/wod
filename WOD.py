from tkinter import Button, Toplevel, Entry, Label, Tk, messagebox, Menu, Frame, END
from tkinter import ttk
import copy
import json
import openpyxl

#Objective: make a WoD sheet manager that let you create an initial char, save it permanently, export/import to/from an excel file.
#The ui must be intuitive. Also more then 1 type of character must be accepted (Mage, Werewolf and Vampire, at least).
#The program must do all the  math automatically (Points distribution, freebies and experience), and let the user know if something is wrong.
#A ST mode should be done, where the user can do a sheet without mathematical limits, and the NPC sheet exported should be simple, with only what the npc have dots in it.




class Sheet_UI:
    def __init__(self):
        self.window = root
        root.geometry('800x800')
        vlist= [0,1,2,3,4,5,6,7,8,9]
        wlist= [5,6,7,8,9,10]
        priolistAt= [7,5,3]
        priolistAb=[13,9,5]
        self.d ={}
        c=0
        r=0
        #start header
        #todo: get the object names from a external file, so you can declare them with a loop. solve how to arrange the objects in the gui.
        label_name = Label(self.window, text = "Name", background="dark grey")
        label_name.grid(column= c , row = r+0)

        self.d["name"] = Entry(self.window)
        self.d["name"].grid(column = c+1, row = r+0)

        label_name = Label(self.window, text = "Nature", background="dark grey")
        label_name.grid(column= c+2, row=0)

        self.d["nature"] = Entry(self.window)
        self.d["nature"].grid(column = c+3, row = r+0)

        label_name = Label(self.window, text = "Faction", background="dark grey")
        label_name.grid(column=4, row=0)

        self.d["faction"] = Entry(self.window)
        self.d["faction"].grid(column = c+5, row = r+0)

        label_player = Label(self.window, text= "Player", background="dark grey")
        label_player.grid(column = c+0, row = r+1)

        self.d["player"] = Entry(self.window)
        self.d["player"].grid(column = c+1, row = r+1)

        label_demeanor = Label(self.window, text="Demeanor", background="dark grey")
        label_demeanor.grid(column = c+2, row = r+1)

        self.d["demeanor"] = Entry(self.window)
        self.d["demeanor"].grid(column = c+3, row = r+1)

        label_cabal = Label(self.window, text="Cabal", background="dark grey")
        label_cabal.grid(column = c+4, row = r+1)

        self.d["cabal"] = Entry(self.window)
        self.d["cabal"].grid(column = c+5, row = r+1)

        label_chronicle = Label(self.window, text= "Chronicle", background="dark grey")
        label_chronicle.grid(column = c+0, row = r+2)

        self.d["chronicle"] = Entry(self.window)
        self.d["chronicle"].grid(column = c+1, row = r+2)

        label_essence = Label(self.window, text="Essence", background="dark grey")
        label_essence.grid(column = c+2, row = r+2)

        self.d["essence"] = Entry(self.window)
        self.d["essence"].grid(column = c+3, row = r+2)

        label_concept = Label(self.window, text="Concept", background="dark grey")
        label_concept.grid(column = c+4, row = r+2)

        self.d["concept"] = Entry(self.window)
        self.d["concept"].grid(column = c+5, row = r+2)

        #end header

        #Start of Attributes , followed column by column, instead of row by row like above.
        Label(self.window, text= "ATTRIBUTES", background="dark grey").grid(column=c+3, row=r+3)

        Label(self.window, text= "Physical", background="dark grey").grid(column=c+0, row=r+4)

        self.d["phyPrio"] = ttk.Combobox(self.window, values = priolistAt, width = 5)
        self.d["phyPrio"].grid(column= c+1, row=r+4)

        Label(self.window, text= "Strength", background="dark grey").grid(column = c+0, row = r+5)

        self.d["strength"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["strength"].grid(column = c+1, row = r+5)

        Label(self.window, text="Dexterity", background="dark grey").grid(column = c+0, row = r+6)

        self.d["dexterity"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["dexterity"].grid(column = c+1, row = r+6)

        Label(self.window, text="Stamina", background="dark grey").grid(column = c+0, row = r+7)

        self.d["stamina"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["stamina"].grid(column = c+1, row = r+7)

        Label(self.window, text= "Social", background="dark grey").grid(column=c+2, row=c+4)

        self.d["socPrio"] = ttk.Combobox(self.window, values = priolistAt, width = 5)
        self.d["socPrio"].grid(column= c+3, row=r+4)

        Label(self.window, text= "Charisma", background="dark grey").grid(column = c+2, row = r+5)

        self.d["charisma"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["charisma"].grid(column = c+3, row = r+5)

        Label(self.window, text="Manipulation", background="dark grey").grid(column = c+2, row = r+6)

        self.d["manipulation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["manipulation"].grid(column = c+3, row = r+6)

        Label(self.window, text="Appearance", background="dark grey").grid(column = c+2, row = r+7)

        self.d["appearance"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["appearance"].grid(column = c+3, row = r+7)

        Label(self.window, text= "Mental", background="dark grey").grid(column=c+4, row=r+4)
    
        self.d["menPrio"] = ttk.Combobox(self.window, values = priolistAt, width = 5)
        self.d["menPrio"].grid(column= c+5, row=r+4)

        Label(self.window, text= "Perception", background="dark grey").grid(column = c+4, row = r+5)

        self.d["perception"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["perception"].grid(column = c+5, row = r+5)

        Label(self.window, text="Intelligence", background="dark grey").grid(column = c+4, row = r+6)

        self.d["intelligence"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["intelligence"].grid(column = c+5, row = r+6)

        Label(self.window, text="Wits", background="dark grey").grid(column = c+4, row = r+7)

        self.d["wits"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["wits"].grid(column = c+5, row = r+7)

        #start of the abilities

        Label(self.window, text= "ABILITIES", background="dark grey").grid(column=c+3, row=r+8) 

        Label(self.window, text= "Talents", background="dark grey").grid(column=c+0, row=9)

        self.d["talPrio"] = ttk.Combobox(self.window, values = priolistAb, width = 4)
        self.d["talPrio"].grid(column= c+1, row=r+9)

        Label(self.window, text= "Alertness", background="dark grey").grid(column = c+0, row = r+11)

        self.d["alertness"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["alertness"].grid(column = c+1, row = r+11)

        Label(self.window, text="Art", background="dark grey").grid(column = c+0, row = r+12)

        self.d["art"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["art"].grid(column = c+1, row = r+12)

        Label(self.window, text="Athletics", background="dark grey").grid(column = c+0, row = r+13)

        self.d["athletics"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["athletics"].grid(column = c+1, row = r+13)

        Label(self.window, text= "Awareness", background="dark grey").grid(column = c+0, row = r+14)

        self.d["awareness"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["awareness"].grid(column = c+1, row = r+14)

        Label(self.window, text="Brawl", background="dark grey").grid(column = c+0, row = r+15)

        self.d["brawl"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["brawl"].grid(column = c+1, row = r+15)

        Label(self.window, text="Empathy", background="dark grey").grid(column = c+0, row = r+16)

        self.d["empathy"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["empathy"].grid(column = c+1, row = r+16)

        Label(self.window, text= "Expression", background="dark grey").grid(column = c+0, row = r+17)

        self.d["expression"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["expression"].grid(column = c+1, row = r+17)

        Label(self.window, text="Intimidation", background="dark grey").grid(column = c+0, row = r+18)

        self.d["intimidation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["intimidation"].grid(column = c+1, row = r+18)

        Label(self.window, text="Leadership", background="dark grey").grid(column = c+0, row = r+19)

        self.d["leadership"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["leadership"].grid(column = c+1, row = r+19)

        Label(self.window, text="Streetwise", background="dark grey").grid(column = c+0, row = r+20)

        self.d["streetwise"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["streetwise"].grid(column = c+1, row = r+20)

        Label(self.window, text="Subterfuge", background="dark grey").grid(column = c+0, row = r+21)

        self.d["subterfuge"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["subterfuge"].grid(column = c+1, row = r+21)

        Label(self.window, text= "Skills", background="dark grey").grid(column=c+2, row=9) #skills

        self.d["skiPrio"] = ttk.Combobox(self.window, values = priolistAb, width = 4)
        self.d["skiPrio"].grid(column= c+3, row=r+9)

        Label(self.window, text= "Crafts", background="dark grey").grid(column = c+2, row = r+11)

        self.d["crafts"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["crafts"].grid(column = c+3, row = r+11)

        Label(self.window, text="Drive", background="dark grey").grid(column = c+2, row = r+12)

        self.d["drive"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["drive"].grid(column = c+3, row = r+12)

        Label(self.window, text="Etiquette", background="dark grey").grid(column = c+2, row = r+13)

        self.d["etiquette"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["etiquette"].grid(column = c+3, row = r+13)

        Label(self.window, text= "Firearms", background="dark grey").grid(column = c+2, row = r+14)

        self.d["firearms"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["firearms"].grid(column = c+3, row = r+14)

        Label(self.window, text="Martial Arts", background="dark grey").grid(column = c+2, row = r+15)

        self.d["martialarts"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["martialarts"].grid(column = c+3, row = r+15)

        Label(self.window, text="Meditation", background="dark grey").grid(column = c+2, row = r+16)

        self.d["meditation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["meditation"].grid(column = c+3, row = r+16)

        Label(self.window, text= "Melee", background="dark grey").grid(column = c+2, row = r+17)

        self.d["melee"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["melee"].grid(column = c+3, row = r+17)

        Label(self.window, text="Research", background="dark grey").grid(column = c+2, row = r+18)

        self.d["research"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["research"].grid(column = c+3, row = r+18)

        Label(self.window, text="Stealth", background="dark grey").grid(column = c+2, row = r+19)

        self.d["stealth"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["stealth"].grid(column = c+3, row = r+19)

        Label(self.window, text="Survival", background="dark grey").grid(column = c+2, row = r+20)

        self.d["survival"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["survival"].grid(column = c+3, row = r+20)

        Label(self.window, text="Technology", background="dark grey").grid(column = c+2, row = r+21)

        self.d["technology"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["technology"].grid(column = c+3, row = r+21)

        Label(self.window, text= "Knowledges", background="dark grey").grid(column=c+4, row=9) #knowledges

        self.d["knoPrio"] = ttk.Combobox(self.window, values = priolistAb, width = 4)
        self.d["knoPrio"].grid(column= c+5, row=r+9)

        label_academics = Label(self.window, text= "Academics", background="dark grey")
        label_academics.grid(column = c+4, row = r+11)

        self.d["academics"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["academics"].grid(column = c+5, row = r+11)

        label_computer = Label(self.window, text="Computer", background="dark grey")
        label_computer.grid(column = c+4, row = r+12)

        self.d["computer"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["computer"].grid(column = c+5, row = r+12)

        label_cosmology = Label(self.window, text="Cosmology", background="dark grey")
        label_cosmology.grid(column = c+4, row = r+13)

        self.d["cosmology"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["cosmology"].grid(column = c+5, row = r+13)

        label_enigmas = Label(self.window, text= "Enigmas", background="dark grey")
        label_enigmas.grid(column = c+4, row = r+14)

        self.d["enigmas"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["enigmas"].grid(column = c+5, row = r+14)

        label_esoterica = Label(self.window, text="Esoterica", background="dark grey")
        label_esoterica.grid(column = c+4, row = r+15)

        self.d["esoterica"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["esoterica"].grid(column = c+5, row = r+15)

        label_investigation = Label(self.window, text="Investigation", background="dark grey")
        label_investigation.grid(column = c+4, row = r+16)

        self.d["investigation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["investigation"].grid(column = c+5, row = r+16)

        label_law = Label(self.window, text= "Law", background="dark grey")
        label_law.grid(column = c+4, row = r+17)

        self.d["law"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["law"].grid(column = c+5, row = r+17)

        label_medicine = Label(self.window, text="Medicine", background="dark grey")
        label_medicine.grid(column = c+4, row = r+18)

        self.d["medicine"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["medicine"].grid(column = c+5, row = r+18)

        label_occult = Label(self.window, text="Occult", background="dark grey")
        label_occult.grid(column = c+4, row = r+19)

        self.d["occult"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["occult"].grid(column = c+5, row = r+19)

        label_politics = Label(self.window, text="Politics", background="dark grey")
        label_politics.grid(column = c+4, row = r+20)

        self.d["politics"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["politics"].grid(column = c+5, row = r+20)

        label_science = Label(self.window, text="Science", background="dark grey")
        label_science.grid(column = c+4, row = r+21)

        self.d["science"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["science"].grid(column = c+5, row = r+21)

        Label(self.window, text= "SPHERES", background="dark grey").grid(column=c+3, row=c+22) #spheres

        label_correspondence = Label(self.window, text="Correspondence", background="dark grey")
        label_correspondence.grid(column = c+0, row = r+23)

        self.d["correspondence"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["correspondence"].grid(column = c+1, row = r+23)

        label_entropy = Label(self.window, text="Entropy", background="dark grey")
        label_entropy.grid(column = c+0, row = r+24)

        self.d["entropy"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["entropy"].grid(column = c+1, row = r+24)

        label_forces = Label(self.window, text="Forces", background="dark grey")
        label_forces.grid(column = c+0, row = r+25)

        self.d["forces"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["forces"].grid(column = c+1, row = r+25)

        label_life = Label(self.window, text="Life", background="dark grey")
        label_life.grid(column = c+2, row = r+23)

        self.d["life"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["life"].grid(column = c+3, row = r+23)

        label_matter = Label(self.window, text="Matter", background="dark grey")
        label_matter.grid(column = c+2, row = r+24)

        self.d["matter"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["matter"].grid(column = c+3, row = r+24)

        label_mind = Label(self.window, text="Mind", background="dark grey")
        label_mind.grid(column = c+2, row = r+25)

        self.d["mind"]= ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["mind"].grid(column = c+3, row = r+25)

        label_prime = Label(self.window, text="Prime", background="dark grey")
        label_prime.grid(column = c+4, row = r+23)

        self.d["prime"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["prime"].grid(column = c+5, row = r+23)

        label_spirit = Label(self.window, text="Spirit", background="dark grey")
        label_spirit.grid(column = c+4, row = r+24)

        self.d["spirit"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["spirit"].grid(column = c+5, row = r+24)

        label_time = Label(self.window, text="Time", background="dark grey")
        label_time.grid(column = c+4, row = r+25)

        self.d["time"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["time"].grid(column = c+5, row = r+25)
        self.d["time"].set("0")

        Label(self.window, text = "ADVANTAGES", background="dark grey").grid(column= 3, row = r+26)

        Label(self.window, text= "Backgrounds", background="dark grey").grid(column = c+0, row= 27) #backgrounds

        self.d["bg1"]= Entry(self.window)
        self.d["bg1"].grid(column = c+0, row = r+28)

        self.d["bg1c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg1c"].grid(column = c+1, row = r+28)

        self.d["bg2"]= Entry(self.window)
        self.d["bg2"].grid(column = c+0, row = r+29)

        self.d["bg2c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg2c"].grid(column = c+1, row = r+29)

        self.d["bg3"]= Entry(self.window)
        self.d["bg3"].grid(column = c+0, row = r+30)

        self.d["bg3c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg3c"].grid(column = c+1, row = r+30)

        self.d["bg4"]= Entry(self.window)
        self.d["bg4"].grid(column = c+0, row = r+31)

        self.d["bg4c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg4c"].grid(column = c+1, row = r+31)

        self.d["bg5"]= Entry(self.window)
        self.d["bg5"].grid(column = c+0, row = r+32)

        self.d["bg5c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg5c"].grid(column = c+1, row = r+32)

        self.d["bg6"]= Entry(self.window)
        self.d["bg6"].grid(column = c+0, row = r+33)

        self.d["bg6c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg6c"].grid(column = c+1, row = r+33)

        Label(self.window,text= "Arete", background="dark grey").grid(column =2, row =27)   #arete

        self.d["arete"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["arete"].grid(column = c+3, row = r+27)

        Label(self.window,text= "Willpower", background="dark grey").grid(column =2, row =28)   #willpower

        self.d["willpower"] = ttk.Combobox(self.window, values = wlist, width = 1)
        self.d["willpower"].grid(column = c+3, row = r+28)

        Label(self.window, text= "Other Traits", background="dark grey").grid(column = c+2, row= 29) #other traits

        self.d["ot1"]= Entry(self.window)
        self.d["ot1"].grid(column = c+2, row = r+30)

        self.d["ot1c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot1c"].grid(column = c+3, row = r+30)

        self.d["ot2"]= Entry(self.window)
        self.d["ot2"].grid(column = c+2, row = r+31)

        self.d["ot2c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot2c"].grid(column = c+3, row = r+31)

        self.d["ot3"]= Entry(self.window)
        self.d["ot3"].grid(column = c+2, row =32)

        self.d["ot3c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot3c"].grid(column = c+3, row = r+32)

        self.d["ot4"]= Entry(self.window)
        self.d["ot4"].grid(column = c+2, row = r+33)

        self.d["ot4c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot4c"].grid(column = c+3, row = r+33)

        Label(self.window, text = "Merits and flaws", background="dark grey").grid(column = c+4, row = r+27)

        mflist = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]

        self.d["mf1"]= Entry(self.window)
        self.d["mf1"].grid(column = c+4, row = r+28)

        self.d["mf1c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf1c"].grid(column = c+5, row = r+28)

        self.d["mf2"]= Entry(self.window)
        self.d["mf2"].grid(column = c+4, row = r+29)

        self.d["mf2c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf2c"].grid(column = c+5, row = r+29)

        self.d["mf3"]= Entry(self.window)
        self.d["mf3"].grid(column = c+4, row = r+30)

        self.d["mf3c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf3c"].grid(column = c+5, row = r+30)

        self.d["mf4"]= Entry(self.window)
        self.d["mf4"].grid(column = c+4, row = r+31)

        self.d["mf4c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf4c"].grid(column = c+5, row = r+31)

        self.d["mf5"]= Entry(self.window)
        self.d["mf5"].grid(column = c+4, row = r+32)

        self.d["mf5c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf5c"].grid(column = c+5, row = r+32)

        self.d["mf6"]= Entry(self.window)
        self.d["mf6"].grid(column = c+4, row = r+33)

        self.d["mf6c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf6c"].grid(column = c+5, row = r+33)

 

class Sheet:
    #todo:  exports: pdf, excel and plain text.
    # character creation: go to the proccess of making a character, and validating it. (7/5/3, 13/9/5, 5will, 7 bg, 15 freebies)
    #edit existing character
    #erase a character

    def __init__(self,name):

        self.name = name
        self.ui = Sheet_UI()
        
        if self.name != "":
            self.openSheet(name)
            button_erase = Button(self.ui.window, text= "Erase", width = 10, command=  lambda y = self.name: self.erase(y) )
            button_erase.grid(column = 0, row =34)
            button_exportExcel = Button(self.ui.window, text= "Export for Excel", width = 10, command=  lambda y = self.name: self.exportExcel(y) )
            button_exportExcel.grid(column = 4, row =34)
        else:
            self.openSheet("0")
        button_save = Button(self.ui.window, text= "Save", width= 20, command= self.save)
        button_save.grid( column = 5, row = 34)

    def openSheet(self,name):
        with open('output.json') as f:
            data = json.load(f)

        if name in data.keys():
            for key,value in data[name].items():#this is the loop to get all nested dictionaries, 3 levels in 
                if type(value) == dict:
                    for key1,value1 in value.items():
                        if type(value1) == dict:#aqui começa para os backgrounds
                            for key2 in value1.keys():
                                if type(self.ui.d[key2]) == Entry: 
                                    self.ui.d[key2].delete(0,END)
                                    self.ui.d[key2].insert(0,data[name][key][key1][key2])        
                                else:
                                    self.ui.d[key2].set(data[name][key][key1][key2])                                  
                        else:
                            if type(self.ui.d[key1])== Entry:
                                self.ui.d[key1].delete(0,END)
                                self.ui.d[key1].insert(0,data[name][key][key1])
                            else:
                                self.ui.d[key1].set(data[name][key][key1])   
                else:
                    if type(self.ui.d[key]) == Entry:
                        self.ui.d[key].delete(0,END) 
                        self.ui.d[key].insert(0,data[name][key])
                    else:
                        self.ui.d[key].set(data[name][key])                        
        else:
             messagebox.showerror("Character Not Found", "There is no character named " + name)            

    def sum(self,name,category):#give the sum of points of a certain category.
        sum= 0
        with open('output.json') as f:
            data = json.load(f)

        if name in data.keys():
            if category == "physical" or category == "social" or category=="mental":
                for value in data[name]["attributes"][category].values():
                    sum+= int(value)
            elif category == "talents" or category =="skills" or category == "knowledges":
                for value in data[name]["abilities"][category].values():
                    sum+= int(value)            
            elif category == "backgrounds" or category == "spheres":
                for value in data[name][category].values():
                    sum+= int(value)                                    
            elif category == "merits and flaws" or category == "other traits":
                for value in data[name][category].values():
                    sum+= int(value)   
            else:
                return "invalid category"
            
            with open('output.json', 'w') as f: #dump the changes into the json file
                json.dump(data, f, indent = 2) 

            return sum  
        else:
            return "invalid name"

        with open('output.json', 'w') as f: #dump the changes into the json file
            json.dump(data, f, indent = 2)

    def save(self):#creates a new entry in the json file. 
       
        with open('output.json') as f:
            data = json.load(f)
        if self.ui.d["name"].get() == '0':
             messagebox.showerror("Invalid Character name.", "Character name cannot be 0.")
             return
        else: #character doesnt have a 0 as name            
            if self.ui.d["name"].get() in data:
                 messagebox.showerror("Invalid Character name.", "There is already one named "+self.ui.d["name"].get())
                 return        
                #message: do you want to overwrite the 
                # sheet named self.ui.entry_name.get()? if yes, go to else, if no, get out of the function
                #elif no:  commented out to implement later 
            else:              
                #sheet isnt name 0, have a unique name or the user wants to overwrite the sheet, you can proceed to save
                ##### Save procedure #####
                x = ''
                x = self.ui.d["name"].get()
                data[x] = copy.deepcopy(data['0']) # data['0'] is the empty form for the sheets
                #bipty bopty get all of the data from the self.ui and shove into data[nameofthesheet]opty
                #data[x]["name"] = self.d["name"].get()
                for key,value in data[x].items():#this is the loop to get all nested dictionaries, present in sheet0, 2 levels in
                    if type(value) == dict:
                        for k,v in value.items():
                            if type(v) == dict:
                                for p in v.keys():# p é key, x é value
                                    data[x][key][k][p] = self.ui.d[p].get()
                            else:
                                data[x][key][k] = self.ui.d[k].get()   
                    else:
                        data[x][key] = self.ui.d[key].get()              
        with open('output.json', 'w') as f: #dump the changes into the json file
            json.dump(data, f, indent = 2)

    def erase(self, name):
        res = messagebox.askquestion('askquestion', 'Are you sure you want to erase the sheet?')
        if res == 'yes':
            with open('output.json') as f:
                data = json.load(f)
            del data[name]
            with open('output.json', 'w') as f: #dump the changes into the json file
                json.dump(data, f, indent = 2)
            messagebox.showinfo('Response', 'Sheet deleted!')
        elif res == 'no':
            messagebox.showinfo('Response', 'Phew! Nothing was erased.')
        else:
            messagebox.showwarning('error', 'Something went wrong!')

               

    def exportExcel(self, name):
        wb = openpyxl.Workbook()
        tab = wb.active #tab is the name used for the excel sheet, cant be named sheet because sheet is used for character sheet
        tab.title = name    
        with open('output.json') as f:
            data = json.load(f)

        c=1
        r=1
                
        for key,value in data[name].items():
            if type(data[name][key])== dict:
                break      
            cellref = tab.cell(row = r, column = c)
            cellref.value = key + ' :'
            c+=1
            cellref = tab.cell(row = r, column = c)
            cellref.value = value
            c+=1
            if c == 7:
                r+=1
                c = 1  
        
        c=1
        r=6
        for key in data[name]["attributes"]["physical"].keys():
            cellref = tab.cell(row = r, column= c, value = key)
            c+=1
            cellref = tab.cell(row = r, column= c, value = data[name]["attributes"]["physical"][key])
            c-=1
            r+=1 

        c=3
        r=6
        for key in data[name]["attributes"]["social"].keys():
            cellref = tab.cell(row = r, column= c, value = key)
            c+=1
            cellref = tab.cell(row = r, column= c, value = data[name]["attributes"]["social"][key])
            c-=1
            r+=1 

        c=5
        r=6
        for key in data[name]["attributes"]["mental"].keys():
            cellref = tab.cell(row = r, column= c, value = key)
            c+=1
            cellref = tab.cell(row = r, column= c, value = data[name]["attributes"]["mental"][key])
            c-=1
            r+=1 

        c=1
        r=11
        for key in data[name]["abilities"]["talents"].keys():
            cellref = tab.cell(row = r, column= c, value = key)
            c+=1
            cellref = tab.cell(row = r, column= c, value = data[name]["abilities"]["talents"][key])
            c-=1
            r+=1            

        c=3
        r=11
        for key in data[name]["abilities"]["skills"].keys():
            cellref = tab.cell(row = r, column= c, value = key)
            c+=1
            cellref = tab.cell(row = r, column= c, value = data[name]["abilities"]["skills"][key])
            c-=1
            r+=1    

        c=5
        r=11
        for key in data[name]["abilities"]["knowledges"].keys():
            cellref = tab.cell(row = r, column= c, value = key)
            c+=1
            cellref = tab.cell(row = r, column= c, value = data[name]["abilities"]["knowledges"][key])
            c-=1
            r+=1   

        c=1
        r=23

        for key,value in data[name]["spheres"].items(): #unique to mage   
            cellref = tab.cell(row = r, column = c)
            cellref.value = key + ' :'
            c+=1
            cellref = tab.cell(row = r, column = c)
            cellref.value = value
            c+=1
            if c == 7:
                r+=1
                c = 1  

        c=1
        r=29
        for key in data[name]["backgrounds"].keys():
            if data[name]["backgrounds"][key] =="":
                break
            cellref = tab.cell(row = r, column= c, value = data[name]["backgrounds"][key])
            c+=1
            if c==3:
                c=1
                r+=1
        c=3
        r=30
        for key in data[name]["other traits"].keys():
            if data[name]["other traits"][key] =="":
                break
            cellref = tab.cell(row = r, column= c, value = data[name]["other traits"][key])
            c+=1
            if c==5:
                c=3
                r+=1

        c=5
        r=28

        for key in data[name]["merits and flaws"].keys():
            if data[name]["merits and flaws"][key] =="":
                break
            cellref = tab.cell(row = r, column= c, value = data[name]["merits and flaws"][key])
            c+=1
            if c==7:
                c=5
                r+=1


        cellref = tab.cell(row =27 , column =3, value = "arete")  #unique to mage
        cellref = tab.cell(row =27 , column =4, value = data[name]["arete"])   #unique to mage     
        cellref = tab.cell(row =28 , column =3, value = "willpower")  
        cellref = tab.cell(row =28 , column =4, value = data[name]["willpower"]) 

        cellref = tab.cell(row=4 , column=4, value="Attributes")  
        cellref = tab.cell(row=5 , column=1, value="Physical") 
        cellref = tab.cell(row=5 , column=3, value="Social") 
        cellref = tab.cell(row=5 , column=5, value="Mental") 
        cellref = tab.cell(row=9 , column=4, value="Abilities")
        cellref = tab.cell(row=10 , column=1, value="Talents")         
        cellref = tab.cell(row=10 , column=3, value="Skills")         
        cellref = tab.cell(row=10 , column=5, value="Knowledges")
        cellref = tab.cell(row=22 , column=4, value="Spheres")#unique to mage
        cellref = tab.cell(row=26 , column=4, value="Advantages")
        cellref = tab.cell(row=28 , column=1, value="Backgrounds")
        cellref = tab.cell(row=27 , column=5, value="Merits and Flaws")
        cellref = tab.cell(row=29 , column=3, value="Other Traits")

    def unwrap(self, name):#unwrap the json sheet into a unested dict
        sheet = {}
        with open('output.json') as f:
            data = json.load(f)

        for key,value in data[name].items():#this is the loop to get all nested dictionaries, 3 levels in, and unwrap in a unested dict
            if type(value) == dict:
                for key1,value1 in value.items():
                    if type(value1) == dict:
                        for key2 in value1.keys():
                                sheet[key2] = data[name][key][key1][key2]                                  
                    else:
                        sheet[key1] = data[name][key][key1] #bg ot and mf are all recorded here   
            else:
                sheet[key] = data[name][key]      
        return sheet


"""
    def validateNewCharacter(self):
        self.save()
        with open('output.json') as f:
            data = json.load(f)
        

        self.ui["name"](state='disabled')
        name = ""
        name = data["name"]["name"]
        if self.sum(name, "spheres")<6:
            #messagem : faltam self.sum(name, "spheres") - 6*(-1) pts de esferas
        elif self.sum(name, "spheres")>6:
            #message: sobram self.sum(name, "spheres") -6 pts de esferas
        if self.sum(name, "backgrounds")<7:
            #message: faltam self.sum(name, "backgrounds") -7*(-1) pts de bg
        elif self.sum(name, "backgrounds")>7:
            #message: self.sum(name, "backgrounds") -7 pts de bg
        priority= {"physical":data["name"]["phyPrio"],"mental":data["name"]["menPrio"],"social":data["name"]["socPrio"]}
        if priority["physical"] == priority["mental"] or priority["physical"]==priority["social"] or priority["mental"]==priority["social"]:
            #message: you cannot have 2 categories with the same priority
        for key in priority.keys():
            if self.sum(name,key)-3 != int(priority[key]):
                if sum < points:
                    #message: faltam points-sum em key
                else:
                    #message: sobram sum-points em key
        priorityAb = {"talents":data["name"]["talPrio"] , "skills":data["name"]["skiPrio"] , "knowledges"data["name"]["knoPrio"]:}
        if priority["physical"] == priority["mental"] or priority["physical"]==priority["social"] or priority["mental"]==priority["social"]:
            #message: you cannot have 2 categories with the same priority
        for key in priorityAb.keys():
            if self.sum(name,key) != int(priorityAb[key]):
                if sum < points:
                    #message: faltam points-sum em key
                else:
                    #message: sobram sum-points em key
        totalFreebiesAtt = (sum(name,"physical") + sum(name,"social") + sum(name,"mental") - 21) *5 #da o total de pontos gastos nos att
        totalFreebiesAbi = (sum(name,"talents")+ sum(name,"skills") + sum(name,"skills") - 27) *2
        totalFreebiesBgs = sum(name,"backgrounds") -7
        totalFreebiesAre = (int(data["name"]["arete"])-1)*4
        totalFreebiesWil = int(data["name"]["will"])-5
        totalFreebiesMfs = sum(name,"merits and flaws")
        totalFreebiesOtt = sum(name, "other traits")*2
        totalFreebiesSph = (sum(name,"spheres")-6)*7

"""
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)
        with open('output.json') as f:
            data = json.load(f)
        
        fileMenu = Menu(menu, tearoff=False)
        empty = ""
        fileMenu.add_command(label="New", command = lambda y=empty :Sheet(y))
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        openMenu = Menu(menu, tearoff=False)
        for key in data.keys():
            if key == "0":
                print("")#how to instruct do nothing?
            else:
                openMenu.add_command(label=key, command=lambda y=key :Sheet(y))
        menu.add_cascade(label="Open", menu=openMenu)

        exportMenu = Menu(menu, tearoff=False)
        exportMenu.add_command(label="Export to PDF")
        exportMenu.add_command(label="Export to Excel")
        exportMenu.add_command(label="Export to plain text")
        menu.add_cascade(label="Export", menu=exportMenu)

    def exitProgram(self):
        exit()
                    
root = Tk()
root.title('Wod Sheet Manager')
root.configure(background= "dark grey")
root.geometry('700x500')
app = Window(root)
root.mainloop()
