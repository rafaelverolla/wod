from tkinter import Button, Toplevel, Entry, Label, Tk
from tkinter import ttk
import json

#Objective: make a WoD sheet manager that let you create an initial char, save it permanently, export/import to/from an excel file.
#The ui must be intuitive. Also more then 1 type of character must be accepted (Mage, Werewolf and Vampire, at least).
#The program must do all the  math automatically (Points distribution, freebies and experience), and let the user know if something is wrong.
#A ST mode should be done, where the user can do a sheet without mathematical limits, and the NPC sheet exported should be simple, with only what the npc have dots in it.

root = Tk()
root.title('Wod Sheet Manager')
root.configure(background= "powder blue")



class Sheet_UI:
    def __init__(self):
        self.window = Toplevel()
        vlist= [0,1,2,3,4,5,6,7,8,9]
        #start header

        label_name = Label(self.window, text = "Name")
        label_name.grid( column=0 , row =0)

        self.entry_name = Entry(self.window)
        self.entry_name.grid(column = 1, row = 0)

        label_nature = Label(self.window, text = "Nature")
        label_nature.grid(column=2, row=0)

        self.entry_nature = Entry(self.window)
        self.entry_nature.grid(column = 3, row = 0)

        label_faction = Label(self.window, text = "Faction")
        label_faction.grid(column=4, row=0)

        self.entry_faction = Entry(self.window)
        self.entry_faction.grid(column = 5, row = 0)

        label_player = Label(self.window, text= "Player")
        label_player.grid(column = 0, row = 1)

        self.entry_player = Entry(self.window)
        self.entry_player.grid(column = 1, row = 1)

        label_demeanor = Label(self.window, text="Demeanor")
        label_demeanor.grid(column = 2, row = 1)

        self.entry_demeanor = Entry(self.window)
        self.entry_demeanor.grid(column = 3, row = 1)

        label_cabal = Label(self.window, text="Cabal")
        label_cabal.grid(column = 4, row = 1)

        self.entry_cabal = Entry(self.window)
        self.entry_cabal.grid(column = 5, row = 1)

        label_chronicle = Label(self.window, text= "Chronicle")
        label_chronicle.grid(column = 0, row = 2)

        self.entry_chronicle = Entry(self.window)
        self.entry_chronicle.grid(column = 1, row = 2)

        label_essence = Label(self.window, text="Essence")
        label_essence.grid(column = 2, row = 2)

        self.entry_essence = Entry(self.window)
        self.entry_essence.grid(column = 3, row = 2)

        label_concept = Label(self.window, text="Concept")
        label_concept.grid(column = 4, row = 2)

        self.entry_concept = Entry(self.window)
        self.entry_concept.grid(column = 5, row = 2)

        #end header

        #Start of Attributes , followed column by column, instead of row by row like above.
        Label(self.window, text= "ATTRIBUTES").grid(column=3, row=3)

        Label(self.window, text= "Physical").grid(column=0, row=4)

        Label(self.window, text= "Strength").grid(column = 0, row = 5)

        self.combobox_strength = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_strength.grid(column = 1, row = 5)

        Label(self.window, text="Dexterity").grid(column = 0, row = 6)

        self.combobox_dexterity = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_dexterity.grid(column = 1, row = 6)

        Label(self.window, text="Stamina").grid(column = 0, row = 7)

        self.combobox_stamina = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_stamina.grid(column = 1, row = 7)

        Label(self.window, text= "Social").grid(column=2, row=4)

        Label(self.window, text= "Charisma").grid(column = 2, row = 5)

        self.combobox_charisma = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_charisma.grid(column = 3, row = 5)

        Label(self.window, text="Manipulation").grid(column = 2, row = 6)

        self.combobox_manipulation = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_manipulation.grid(column = 3, row = 6)

        Label(self.window, text="Appearance").grid(column = 2, row = 7)

        self.combobox_appearance = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_appearance.grid(column = 3, row = 7)

        Label(self.window, text= "Mental").grid(column=4, row=4)

        Label(self.window, text= "Perception").grid(column = 4, row = 5)

        self.combobox_perception = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_perception.grid(column = 5, row = 5)

        Label(self.window, text="Intelligence").grid(column = 4, row = 6)

        self.combobox_intelligence = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_intelligence.grid(column = 5, row = 6)

        Label(self.window, text="Wits").grid(column = 4, row = 7)

        self.combobox_wits = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_wits.grid(column = 5, row = 7)

        #start of the abilities

        Label(self.window, text= "Abilities").grid(column=3, row=8) 

        Label(self.window, text= "Talents").grid(column=1, row=9)

        Label(self.window, text= "Alertness").grid(column = 0, row = 11)

        self.combobox_alertness = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_alertness.grid(column = 1, row = 11)

        Label(self.window, text="Art").grid(column = 0, row = 12)

        self.combobox_art = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_art.grid(column = 1, row = 12)

        Label(self.window, text="Athletics").grid(column = 0, row = 13)

        self.combobox_athletics = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_athletics.grid(column = 1, row = 13)

        Label(self.window, text= "Awareness").grid(column = 0, row = 14)

        self.combobox_awareness = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_awareness.grid(column = 1, row = 14)

        Label(self.window, text="Brawl").grid(column = 0, row = 15)

        self.combobox_brawl = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_brawl.grid(column = 1, row = 15)

        Label(self.window, text="Empathy").grid(column = 0, row = 16)

        self.combobox_empathy = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_empathy.grid(column = 1, row = 16)

        Label(self.window, text= "Expression").grid(column = 0, row = 17)

        self.combobox_expression = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_expression.grid(column = 1, row = 17)

        Label(self.window, text="Intimidation").grid(column = 0, row = 18)

        self.combobox_intimidation = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_intimidation.grid(column = 1, row = 18)

        Label(self.window, text="Leadership").grid(column = 0, row = 19)

        self.combobox_leadership = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_leadership.grid(column = 1, row = 19)

        Label(self.window, text="Streetwise").grid(column = 0, row = 20)

        self.combobox_streetwise = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_streetwise.grid(column = 1, row = 20)

        Label(self.window, text="Subterfuge").grid(column = 0, row = 21)

        self.combobox_subterfuge = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_subterfuge.grid(column = 1, row = 21)

        Label(self.window, text= "Skills").grid(column=3, row=9) #skills

        Label(self.window, text= "Crafts").grid(column = 2, row = 11)

        self.combobox_crafts = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_crafts.grid(column = 3, row = 11)

        Label(self.window, text="Drive").grid(column = 2, row = 12)

        self.combobox_drive = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_drive.grid(column = 3, row = 12)

        Label(self.window, text="Etiquette").grid(column = 2, row = 13)

        self.combobox_etiquette = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_etiquette.grid(column = 3, row = 13)

        Label(self.window, text= "Firearms").grid(column = 2, row = 14)

        self.combobox_firearms = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_firearms.grid(column = 3, row = 14)

        Label(self.window, text="Martial Arts").grid(column = 2, row = 15)

        self.combobox_martialarts = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_martialarts.grid(column = 3, row = 15)

        Label(self.window, text="Meditation").grid(column = 2, row = 16)

        self.combobox_meditation = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_meditation.grid(column = 3, row = 16)

        Label(self.window, text= "Melee").grid(column = 2, row = 17)

        self.combobox_melee = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_melee.grid(column = 3, row = 17)

        Label(self.window, text="Research").grid(column = 2, row = 18)

        self.combobox_research = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_research.grid(column = 3, row = 18)

        Label(self.window, text="Stealth").grid(column = 2, row = 19)

        self.combobox_stealth = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_stealth.grid(column = 3, row = 19)

        Label(self.window, text="Survival").grid(column = 2, row = 20)

        self.combobox_survival = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_survival.grid(column = 3, row = 20)

        Label(self.window, text="Technology").grid(column = 2, row = 21)

        self.combobox_technology = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_technology.grid(column = 3, row = 21)

        Label(self.window, text= "Knowledges").grid(column=5, row=9) #knowledges

        label_academics = Label(self.window, text= "Academics")
        label_academics.grid(column = 4, row = 11)

        self.combobox_academics = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_academics.grid(column = 5, row = 11)

        label_computer = Label(self.window, text="Computer")
        label_computer.grid(column = 4, row = 12)

        self.combobox_computer = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_computer.grid(column = 5, row = 12)

        label_cosmology = Label(self.window, text="Cosmology")
        label_cosmology.grid(column = 4, row = 13)

        self.combobox_cosmology = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_cosmology.grid(column = 5, row = 13)

        label_enigmas = Label(self.window, text= "Enigmas")
        label_enigmas.grid(column = 4, row = 14)

        self.combobox_enigmas = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_enigmas.grid(column = 5, row = 14)

        label_esoterica = Label(self.window, text="Esoterica")
        label_esoterica.grid(column = 4, row = 15)

        self.combobox_esoterica = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_esoterica.grid(column = 5, row = 15)

        label_investigation = Label(self.window, text="Investigation")
        label_investigation.grid(column = 4, row = 16)

        self.combobox_investigation = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_investigation.grid(column = 5, row = 16)

        label_law = Label(self.window, text= "Law")
        label_law.grid(column = 4, row = 17)

        self.combobox_law = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_law.grid(column = 5, row = 17)

        label_medicine = Label(self.window, text="Medicine")
        label_medicine.grid(column = 4, row = 18)

        self.combobox_medicine = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_medicine.grid(column = 5, row = 18)

        label_occult = Label(self.window, text="Occult")
        label_occult.grid(column = 4, row = 19)

        self.combobox_occult = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_occult.grid(column = 5, row = 19)

        label_politics = Label(self.window, text="Politics")
        label_politics.grid(column = 4, row = 20)

        self.combobox_politics = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_politics.grid(column = 5, row = 20)

        label_science = Label(self.window, text="Science")
        label_science.grid(column = 4, row = 21)

        self.combobox_science = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_science.grid(column = 5, row = 21)

        Label(self.window, text= "Spheres").grid(column=3, row=22) #spheres

        label_correspondence = Label(self.window, text="Correspondence")
        label_correspondence.grid(column = 0, row = 23)

        self.combobox_correspondence = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_correspondence.grid(column = 1, row = 23)

        label_entropy = Label(self.window, text="Entropy")
        label_entropy.grid(column = 0, row = 24)

        self.combobox_entropy = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_entropy.grid(column = 1, row = 24)

        label_forces = Label(self.window, text="Forces")
        label_forces.grid(column = 0, row = 25)

        self.combobox_forces = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_forces.grid(column = 1, row = 25)

        label_life = Label(self.window, text="Life")
        label_life.grid(column = 2, row = 23)

        self.combobox_life = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_life.grid(column = 3, row = 23)

        label_matter = Label(self.window, text="Matter")
        label_matter.grid(column = 2, row = 24)

        self.combobox_matter = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_matter.grid(column = 3, row = 24)

        label_mind = Label(self.window, text="Mind")
        label_mind.grid(column = 2, row = 25)

        self.combobox_mind = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_mind.grid(column = 3, row = 25)

        label_prime = Label(self.window, text="Prime")
        label_prime.grid(column = 4, row = 23)

        self.combobox_prime = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_prime.grid(column = 5, row = 23)

        label_spirit = Label(self.window, text="Spirit")
        label_spirit.grid(column = 4, row = 24)

        self.combobox_spirit = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_spirit.grid(column = 5, row = 24)

        label_time = Label(self.window, text="Time")
        label_time.grid(column = 4, row = 25)

        self.combobox_time = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_time.grid(column = 5, row = 25)

        Label(self.window, text = "ADVANTAGES").grid(column= 3, row = 26)

        Label(self.window, text= "Background").grid(column = 0, row= 27) #backgrounds

        self.entry_bg1= Entry(self.window)
        self.entry_bg1.grid(column = 0, row =28)

        self.combobox_bg1 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_bg1.grid(column = 1, row = 28)

        self.entry_bg2= Entry(self.window)
        self.entry_bg2.grid(column = 0, row =29)

        self.combobox_bg2 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_bg2.grid(column = 1, row = 30)

        self.entry_bg3= Entry(self.window)
        self.entry_bg3.grid(column = 0, row =30)

        self.combobox_bg3 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_bg3.grid(column = 1, row = 30)

        self.entry_bg4= Entry(self.window)
        self.entry_bg4.grid(column = 0, row =31)

        self.combobox_bg4 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_bg4.grid(column = 1, row = 31)

        self.entry_bg5= Entry(self.window)
        self.entry_bg5.grid(column = 0, row =32)

        self.combobox_bg5 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_bg5.grid(column = 1, row = 33)

        self.entry_bg6= Entry(self.window)
        self.entry_bg6.grid(column = 0, row =33)

        self.combobox_bg6 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_bg6.grid(column = 1, row = 33)

        Label(self.window,text= "Arete").grid(column =2, row =27)   #arete

        self.combobox_arete = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_arete.grid(column = 3, row = 27)

        Label(self.window,text= "Willpower").grid(column =2, row =28)   #willpower

        self.combobox_willpower = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_willpower.grid(column = 3, row = 28)

        Label(self.window, text= "Other Traits").grid(column = 2, row= 29) #other traits

        self.entry_ot1= Entry(self.window)
        self.entry_ot1.grid(column = 2, row =30)

        self.combobox_ot1 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_ot1.grid(column = 3, row = 30)

        self.entry_ot2= Entry(self.window)
        self.entry_ot2.grid(column = 2, row =31)

        self.combobox_ot2 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_ot2.grid(column = 3, row = 31)

        self.entry_ot3= Entry(self.window)
        self.entry_ot3.grid(column = 2, row =32)

        self.combobox_ot3 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_ot3.grid(column = 3, row = 32)

        self.entry_ot4= Entry(self.window)
        self.entry_ot4.grid(column = 2, row =33)

        self.combobox_ot4 = ttk.Combobox(self.window, values = vlist, width = 1)
        self.combobox_ot4.grid(column = 3, row = 33)

        Label(self.window, text = "Merits and flaws").grid(column = 4, row = 27)

        mflist = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]

        self.entry_mf1= Entry(self.window)
        self.entry_mf1.grid(column = 4, row =28)

        self.combobox_mf1 = ttk.Combobox(self.window, values = mflist, width = 2)
        self.combobox_mf1.grid(column = 5, row = 28)

        self.entry_mf2= Entry(self.window)
        self.entry_mf2.grid(column = 4, row =29)

        self.combobox_mf2 = ttk.Combobox(self.window, values = mflist, width = 2)
        self.combobox_mf2.grid(column = 5, row = 29)

        self.entry_mf3= Entry(self.window)
        self.entry_mf3.grid(column = 4, row =30)

        self.combobox_mf3 = ttk.Combobox(self.window, values = mflist, width = 2)
        self.combobox_mf3.grid(column = 5, row = 30)

        self.entry_mf4= Entry(self.window)
        self.entry_mf4.grid(column = 4, row =31)

        self.combobox_mf4 = ttk.Combobox(self.window, values = mflist, width = 2)
        self.combobox_mf4.grid(column = 5, row = 31)

        self.entry_mf5= Entry(self.window)
        self.entry_mf5.grid(column = 4, row =32)

        self.combobox_mf5 = ttk.Combobox(self.window, values = mflist, width = 2)
        self.combobox_mf5.grid(column = 5, row = 32)

        self.entry_mf6= Entry(self.window)
        self.entry_mf6.grid(column = 4, row =33)

        self.combobox_mf6 = ttk.Combobox(self.window, values = mflist, width = 2)
        self.combobox_mf6.grid(column = 5, row = 33)

class Sheet: #resolver: _id começa sempre em 0, tem que começar da última ficha feita. open_sheet tem que estar em um objeto. passar a ficha para json.
  
    _id=0
    def __init__(self):
        """
        self._id= Sheet._id 
        Sheet._id += 1 
        self._idstr = str(self._id) 
        """
        self.ui = Sheet_UI()
        button_save = Button(self.ui.window, text= "Save", width= 20, command= self.save)
        button_save.grid( column = 1, row = 34)

    def save(self):#cria ou um sheets.json file, appenda no file uma sheet que sera reconhecida através do seu ID
        with open('output.json') as f:
            data = json.load(f)

        for sheet in data['sheets']:
            if sheet['ID']==1:
                sheet['Name']="Capitao"
        with open('output.json', 'w') as f:
            json.dump(data, f, indent = 2)

         #   print(sheet['ID'], sheet['Concept'], sheet['Atributes']['Physical']['Strength'])
                  



    @property
    def id(self):
        return self._id

def open_Sheet(): #vai abrir uma nova janela que tem varios botões, que tem como text o name, e vai abrir uma Sheet_UI com os dados do arquivo txt correspondente.
    return






button_open = Button(root, text="Open", width = 20) #command=lambda y = i: open_Sheet(y)
button_open.grid( column = 0, row = 0)

button_new = Button(root, text="New", width = 20, command = Sheet) 
button_new.grid( column = 1, row = 0)






root.mainloop()