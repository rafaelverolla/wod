from tkinter import Button, Toplevel, Entry, Label, Tk, messagebox
from tkinter import ttk
import copy
import json

#Objective: make a WoD sheet manager that let you create an initial char, save it permanently, export/import to/from an excel file.
#The ui must be intuitive. Also more then 1 type of character must be accepted (Mage, Werewolf and Vampire, at least).
#The program must do all the  math automatically (Points distribution, freebies and experience), and let the user know if something is wrong.
#A ST mode should be done, where the user can do a sheet without mathematical limits, and the NPC sheet exported should be simple, with only what the npc have dots in it.

root = Tk()
root.title('Wod Sheet Manager')
root.configure(background= "dark grey")


class Sheet_UI:
    def __init__(self):
        self.window = Toplevel()
        vlist= [0,1,2,3,4,5,6,7,8,9]
        self.d ={}
        #start header
        #todo: get the object names from a external file, so you can declare them with a loop. solve how to arrange the objects in the gui.
        label_name = Label(self.window, text = "Name")
        label_name.grid( column=0 , row =0)

        self.d["name"] = Entry(self.window)
        self.d["name"].grid(column = 1, row = 0)

        label_nature = Label(self.window, text = "Nature")
        label_nature.grid(column=2, row=0)

        self.d["nature"] = Entry(self.window)
        self.d["nature"].grid(column = 3, row = 0)

        label_faction = Label(self.window, text = "Faction")
        label_faction.grid(column=4, row=0)

        self.d["faction"] = Entry(self.window)
        self.d["faction"].grid(column = 5, row = 0)

        label_player = Label(self.window, text= "Player")
        label_player.grid(column = 0, row = 1)

        self.d["player"] = Entry(self.window)
        self.d["player"].grid(column = 1, row = 1)

        label_demeanor = Label(self.window, text="Demeanor")
        label_demeanor.grid(column = 2, row = 1)

        self.d["demeanor"] = Entry(self.window)
        self.d["demeanor"].grid(column = 3, row = 1)

        label_cabal = Label(self.window, text="Cabal")
        label_cabal.grid(column = 4, row = 1)

        self.d["cabal"] = Entry(self.window)
        self.d["cabal"].grid(column = 5, row = 1)

        label_chronicle = Label(self.window, text= "Chronicle")
        label_chronicle.grid(column = 0, row = 2)

        self.d["chronicle"] = Entry(self.window)
        self.d["chronicle"].grid(column = 1, row = 2)

        label_essence = Label(self.window, text="Essence")
        label_essence.grid(column = 2, row = 2)

        self.d["essence"] = Entry(self.window)
        self.d["essence"].grid(column = 3, row = 2)

        label_concept = Label(self.window, text="Concept")
        label_concept.grid(column = 4, row = 2)

        self.d["concept"] = Entry(self.window)
        self.d["concept"].grid(column = 5, row = 2)

        #end header

        #Start of Attributes , followed column by column, instead of row by row like above.
        Label(self.window, text= "ATTRIBUTES").grid(column=3, row=3)

        Label(self.window, text= "Physical").grid(column=0, row=4)

        Label(self.window, text= "Strength").grid(column = 0, row = 5)

        self.d["strength"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["strength"].grid(column = 1, row = 5)

        Label(self.window, text="Dexterity").grid(column = 0, row = 6)

        self.d["dexterity"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["dexterity"].grid(column = 1, row = 6)

        Label(self.window, text="Stamina").grid(column = 0, row = 7)

        self.d["stamina"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["stamina"].grid(column = 1, row = 7)

        Label(self.window, text= "Social").grid(column=2, row=4)

        Label(self.window, text= "Charisma").grid(column = 2, row = 5)

        self.d["charisma"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["charisma"].grid(column = 3, row = 5)

        Label(self.window, text="Manipulation").grid(column = 2, row = 6)

        self.d["manipulation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["manipulation"].grid(column = 3, row = 6)

        Label(self.window, text="Appearance").grid(column = 2, row = 7)

        self.d["appearance"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["appearance"].grid(column = 3, row = 7)

        Label(self.window, text= "Mental").grid(column=4, row=4)

        Label(self.window, text= "Perception").grid(column = 4, row = 5)

        self.d["perception"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["perception"].grid(column = 5, row = 5)

        Label(self.window, text="Intelligence").grid(column = 4, row = 6)

        self.d["intelligence"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["intelligence"].grid(column = 5, row = 6)

        Label(self.window, text="Wits").grid(column = 4, row = 7)

        self.d["wits"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["wits"].grid(column = 5, row = 7)

        #start of the abilities

        Label(self.window, text= "Abilities").grid(column=3, row=8) 

        Label(self.window, text= "Talents").grid(column=1, row=9)

        Label(self.window, text= "Alertness").grid(column = 0, row = 11)

        self.d["alertness"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["alertness"].grid(column = 1, row = 11)

        Label(self.window, text="Art").grid(column = 0, row = 12)

        self.d["art"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["art"].grid(column = 1, row = 12)

        Label(self.window, text="Athletics").grid(column = 0, row = 13)

        self.d["athletics"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["athletics"].grid(column = 1, row = 13)

        Label(self.window, text= "Awareness").grid(column = 0, row = 14)

        self.d["awareness"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["awareness"].grid(column = 1, row = 14)

        Label(self.window, text="Brawl").grid(column = 0, row = 15)

        self.d["brawl"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["brawl"].grid(column = 1, row = 15)

        Label(self.window, text="Empathy").grid(column = 0, row = 16)

        self.d["empathy"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["empathy"].grid(column = 1, row = 16)

        Label(self.window, text= "Expression").grid(column = 0, row = 17)

        self.d["expression"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["expression"].grid(column = 1, row = 17)

        Label(self.window, text="Intimidation").grid(column = 0, row = 18)

        self.d["intimidation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["intimidation"].grid(column = 1, row = 18)

        Label(self.window, text="Leadership").grid(column = 0, row = 19)

        self.d["leadership"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["leadership"].grid(column = 1, row = 19)

        Label(self.window, text="Streetwise").grid(column = 0, row = 20)

        self.d["streetwise"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["streetwise"].grid(column = 1, row = 20)

        Label(self.window, text="Subterfuge").grid(column = 0, row = 21)

        self.d["subterfuge"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["subterfuge"].grid(column = 1, row = 21)

        Label(self.window, text= "Skills").grid(column=3, row=9) #skills

        Label(self.window, text= "Crafts").grid(column = 2, row = 11)

        self.d["crafts"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["crafts"].grid(column = 3, row = 11)

        Label(self.window, text="Drive").grid(column = 2, row = 12)

        self.d["drive"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["drive"].grid(column = 3, row = 12)

        Label(self.window, text="Etiquette").grid(column = 2, row = 13)

        self.d["etiquette"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["etiquette"].grid(column = 3, row = 13)

        Label(self.window, text= "Firearms").grid(column = 2, row = 14)

        self.d["firearms"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["firearms"].grid(column = 3, row = 14)

        Label(self.window, text="Martial Arts").grid(column = 2, row = 15)

        self.d["martialarts"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["martialarts"].grid(column = 3, row = 15)

        Label(self.window, text="Meditation").grid(column = 2, row = 16)

        self.d["meditation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["meditation"].grid(column = 3, row = 16)

        Label(self.window, text= "Melee").grid(column = 2, row = 17)

        self.d["melee"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["melee"].grid(column = 3, row = 17)

        Label(self.window, text="Research").grid(column = 2, row = 18)

        self.d["research"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["research"].grid(column = 3, row = 18)

        Label(self.window, text="Stealth").grid(column = 2, row = 19)

        self.d["stealth"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["stealth"].grid(column = 3, row = 19)

        Label(self.window, text="Survival").grid(column = 2, row = 20)

        self.d["survival"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["survival"].grid(column = 3, row = 20)

        Label(self.window, text="Technology").grid(column = 2, row = 21)

        self.d["technology"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["technology"].grid(column = 3, row = 21)

        Label(self.window, text= "Knowledges").grid(column=5, row=9) #knowledges

        label_academics = Label(self.window, text= "Academics")
        label_academics.grid(column = 4, row = 11)

        self.d["academics"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["academics"].grid(column = 5, row = 11)

        label_computer = Label(self.window, text="Computer")
        label_computer.grid(column = 4, row = 12)

        self.d["computer"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["computer"].grid(column = 5, row = 12)

        label_cosmology = Label(self.window, text="Cosmology")
        label_cosmology.grid(column = 4, row = 13)

        self.d["cosmology"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["cosmology"].grid(column = 5, row = 13)

        label_enigmas = Label(self.window, text= "Enigmas")
        label_enigmas.grid(column = 4, row = 14)

        self.d["enigmas"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["enigmas"].grid(column = 5, row = 14)

        label_esoterica = Label(self.window, text="Esoterica")
        label_esoterica.grid(column = 4, row = 15)

        self.d["esoterica"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["esoterica"].grid(column = 5, row = 15)

        label_investigation = Label(self.window, text="Investigation")
        label_investigation.grid(column = 4, row = 16)

        self.d["investigation"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["investigation"].grid(column = 5, row = 16)

        label_law = Label(self.window, text= "Law")
        label_law.grid(column = 4, row = 17)

        self.d["law"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["law"].grid(column = 5, row = 17)

        label_medicine = Label(self.window, text="Medicine")
        label_medicine.grid(column = 4, row = 18)

        self.d["medicine"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["medicine"].grid(column = 5, row = 18)

        label_occult = Label(self.window, text="Occult")
        label_occult.grid(column = 4, row = 19)

        self.d["occult"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["occult"].grid(column = 5, row = 19)

        label_politics = Label(self.window, text="Politics")
        label_politics.grid(column = 4, row = 20)

        self.d["politics"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["politics"].grid(column = 5, row = 20)

        label_science = Label(self.window, text="Science")
        label_science.grid(column = 4, row = 21)

        self.d["science"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["science"].grid(column = 5, row = 21)

        Label(self.window, text= "Spheres").grid(column=3, row=22) #spheres

        label_correspondence = Label(self.window, text="Correspondence")
        label_correspondence.grid(column = 0, row = 23)

        self.d["correspondence"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["correspondence"].grid(column = 1, row = 23)

        label_entropy = Label(self.window, text="Entropy")
        label_entropy.grid(column = 0, row = 24)

        self.d["entropy"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["entropy"].grid(column = 1, row = 24)

        label_forces = Label(self.window, text="Forces")
        label_forces.grid(column = 0, row = 25)

        self.d["forces"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["forces"].grid(column = 1, row = 25)

        label_life = Label(self.window, text="Life")
        label_life.grid(column = 2, row = 23)

        self.d["life"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["life"].grid(column = 3, row = 23)

        label_matter = Label(self.window, text="Matter")
        label_matter.grid(column = 2, row = 24)

        self.d["matter"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["matter"].grid(column = 3, row = 24)

        label_mind = Label(self.window, text="Mind")
        label_mind.grid(column = 2, row = 25)

        self.d["mind"]= ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["mind"].grid(column = 3, row = 25)

        label_prime = Label(self.window, text="Prime")
        label_prime.grid(column = 4, row = 23)

        self.d["prime"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["prime"].grid(column = 5, row = 23)

        label_spirit = Label(self.window, text="Spirit")
        label_spirit.grid(column = 4, row = 24)

        self.d["spirit"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["spirit"].grid(column = 5, row = 24)

        label_time = Label(self.window, text="Time")
        label_time.grid(column = 4, row = 25)

        self.d["time"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["time"].grid(column = 5, row = 25)

        Label(self.window, text = "ADVANTAGES").grid(column= 3, row = 26)

        Label(self.window, text= "Background").grid(column = 0, row= 27) #backgrounds

        self.d["bg1"]= Entry(self.window)
        self.d["bg1"].grid(column = 0, row =28)

        self.d["bg1c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg1c"].grid(column = 1, row = 28)

        self.d["bg2"]= Entry(self.window)
        self.d["bg2"].grid(column = 0, row =29)

        self.d["bg2c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg2c"].grid(column = 1, row = 29)

        self.d["bg3"]= Entry(self.window)
        self.d["bg3"].grid(column = 0, row =30)

        self.d["bg3c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg3c"].grid(column = 1, row = 30)

        self.d["bg4"]= Entry(self.window)
        self.d["bg4"].grid(column = 0, row =31)

        self.d["bg4c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg4c"].grid(column = 1, row = 31)

        self.d["bg5"]= Entry(self.window)
        self.d["bg5"].grid(column = 0, row =32)

        self.d["bg5c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg5c"].grid(column = 1, row = 32)

        self.d["bg6"]= Entry(self.window)
        self.d["bg6"].grid(column = 0, row =33)

        self.d["bg6c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["bg6c"].grid(column = 1, row = 33)

        Label(self.window,text= "Arete").grid(column =2, row =27)   #arete

        self.d["arete"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["arete"].grid(column = 3, row = 27)

        Label(self.window,text= "Willpower").grid(column =2, row =28)   #willpower

        self.d["willpower"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["willpower"].grid(column = 3, row = 28)

        Label(self.window, text= "Other Traits").grid(column = 2, row= 29) #other traits

        self.d["ot1"]= Entry(self.window)
        self.d["ot1"].grid(column = 2, row =30)

        self.d["ot1c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot1c"].grid(column = 3, row = 30)

        self.d["ot2"]= Entry(self.window)
        self.d["ot2"].grid(column = 2, row =31)

        self.d["ot2c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot2c"].grid(column = 3, row = 31)

        self.d["ot3"]= Entry(self.window)
        self.d["ot3"].grid(column = 2, row =32)

        self.d["ot3c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot3c"].grid(column = 3, row = 32)

        self.d["ot4"]= Entry(self.window)
        self.d["ot4"].grid(column = 2, row =33)

        self.d["ot4c"] = ttk.Combobox(self.window, values = vlist, width = 1)
        self.d["ot4c"].grid(column = 3, row = 33)

        Label(self.window, text = "Merits and flaws").grid(column = 4, row = 27)

        mflist = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]

        self.d["mf1"]= Entry(self.window)
        self.d["mf1"].grid(column = 4, row =28)

        self.d["mf1c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf1c"].grid(column = 5, row = 28)

        self.d["mf2"]= Entry(self.window)
        self.d["mf2"].grid(column = 4, row =29)

        self.d["mf2c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf2c"].grid(column = 5, row = 29)

        self.d["mf3"]= Entry(self.window)
        self.d["mf3"].grid(column = 4, row =30)

        self.d["mf3c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf3c"].grid(column = 5, row = 30)

        self.d["mf4"]= Entry(self.window)
        self.d["mf4"].grid(column = 4, row =31)

        self.d["mf4c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf4c"].grid(column = 5, row = 31)

        self.d["mf5"]= Entry(self.window)
        self.d["mf5"].grid(column = 4, row =32)

        self.d["mf5c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf5c"].grid(column = 5, row = 32)

        self.d["mf6"]= Entry(self.window)
        self.d["mf6"].grid(column = 4, row =33)

        self.d["mf6c"] = ttk.Combobox(self.window, values = mflist, width = 2)
        self.d["mf6c"].grid(column = 5, row = 33)

class Sheet:
    #todo:  open_sheet:it  open a sheet from json, put on the ui.
    # character creation: go to the proccess of making a character, and validating it. (7/5/3, 13/9/5, 5will, 7 bg, 15 freebies)
  

    def __init__(self):

        self.ui = Sheet_UI()
        button_save = Button(self.ui.window, text= "Save", width= 20, command= self.save)
        button_save.grid( column = 1, row = 34)

     

    def sum(self,name,category):#give the sum of points of a certain category.
        sum= 0
        with open('output.json') as f:
            data = json.load(f)

        if name in data.key():
            if category == "physical" or category == "social" or category=="mental":
                for value in data[name]["attributes"][category].items():
                    sum+= int(value)
            elif category == "talents" or category =="skills" or category == "knowledges":
                for value in data[name]["abilities"][category].items():
                    sum+= int(value)            
            elif category == "backgrounds":
                for value in data[name]["advantages"][category].items():
                    sum+= int(value)
            elif category == "spheres":
                for value in data[name][category].items():
                    sum+= int(value)                                       
            elif category == "merits and flaws":
                for value in data[name][category].items():
                    sum+= int(value)   
            else:
                return "unvalid category"
            
            with open('output.json', 'w') as f: #dump the changes into the json file
                json.dump(data, f, indent = 2) 

            return sum  
        else:
            return "unvalid name"

        with open('output.json', 'w') as f: #dump the changes into the json file
            json.dump(data, f, indent = 2)


    def save(self):#creates a new entry in the json file. todo: not saving merit flaws and backgrounds.
       
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
                for key,value in data[x].items():#this is the loop to get all nested dictionarys, 2 levels in
                    if type(value) == dict:
                        for k,v in value.items():
                            if type(v) == dict:
                                for p,y in v.items():# p é key, x é value
                                    data[x][key][k][p] = self.ui.d[p].get()
                            else:
                                data[x][key][k] = self.ui.d[k].get()   
                    else:
                        data[x][key] = self.ui.d[key].get() 
                aux={}
                aux = {self.ui.d["bg1"].get(): self.ui.d["bg1c"].get(),
                self.ui.d["bg2"].get(): self.ui.d["bg2c"].get(),self.ui.d["bg3"].get(): self.ui.d["bg3c"].get(),
                self.ui.d["bg4"].get(): self.ui.d["bg4c"].get(),self.ui.d["bg5"].get(): self.ui.d["bg5c"].get(),
                self.ui.d["bg6"].get(): self.ui.d["bg6c"].get()}
                data[x]["advantages"]["backgrounds"]= aux
                aux = {self.ui.d["ot1"].get(): self.ui.d["ot1c"].get(),
                self.ui.d["ot2"].get(): self.ui.d["ot2c"].get(),self.ui.d["ot3"].get(): self.ui.d["ot3c"].get(),
                self.ui.d["ot4"].get(): self.ui.d["ot4c"].get()}
                data[x]["advantages"]["other traits"]= aux 
                aux = {self.ui.d["mf1"].get(): self.ui.d["mf1c"].get(),
                self.ui.d["mf2"].get(): self.ui.d["mf2c"].get(),self.ui.d["mf3"].get(): self.ui.d["mf3c"].get(),
                self.ui.d["mf4"].get(): self.ui.d["mf4c"].get(),self.ui.d["mf5"].get(): self.ui.d["mf5c"].get(),
                self.ui.d["mf6"].get(): self.ui.d["mf6c"].get()}
                data[x]["advantages"]["merits and flaws"]= aux                        
        with open('output.json', 'w') as f: #dump the changes into the json file
            json.dump(data, f, indent = 2)
        
     




#open should give a list of saved characters. this should be all in a object
button_open = Button(root, text="Open", width = 20) #command=lambda y = i: open_Sheet(y)
button_open.grid( column = 0, row = 0)

button_new = Button(root, text="New", width = 20, command = Sheet) 
button_new.grid( column = 1, row = 0)






root.mainloop()
