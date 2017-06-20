import csv

class Item:

    def __init__(self,name,dificultty,type,slot,stam,main,crit,mastery,haste,ver,tier,cl,boss):
        self.type = type
        self.slot = slot
        self.name = name
        self.dificulty = dificultty
        self.stamina = stam
        self.attribute = main
        self.critical = crit
        self.mastery = mastery
        self.haste = haste
        self.versatility = ver
        self.tier = tier
        self.cl = cl
        self.boss = boss

    def show(self):
        print(self.name,",",self.dificulty,"(",self.type,",",self.slot,")","@",self.boss,":","\n\t",self.stamina,self.attribute,self.critical,self.mastery,self.haste,self.versatility,self.tier,self.cl)

    def Get_Score(self,stam_weight,main_weight,crit_weight,mast_weight,haste_weight,vers_weight):
        sum = self.stamina*stam_weight + self.attribute*main_weight + self.critical*crit_weight + self.mastery*mast_weight + self.haste*haste_weight + self.versatility*vers_weight
        return sum

class Loot_Table:

    def __init__(self):
        self.Itens = [] #Item Holder

    def import_loot_table(self,file_path):
        file = open(file_path,mode='r')
        reader = csv.reader(file,delimiter=";")

        rows = []

        for row in reader:
            rows.append(row)

        for row in rows[1:]:
            self.Itens.append(Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))

    def print_loot_table(self):
        for item in self.Itens:
            item.show()

lt = Loot_Table()

lt.import_loot_table("Tomb of Sageras Loot Table Normal.csv")
lt.import_loot_table("Tomb of Sageras Loot Table Heroic.csv")


