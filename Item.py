class Item:

    def __init__(self,name,dificultty,type,slot,stam,main,crit,mastery,haste,ver,tier,cl,boss,gem_slot=False):
        self.type = type.lower()
        self.slot = slot.lower()
        self.name = name
        self.dificulty = dificultty
        self.stamina = int(stam)
        self.attribute = int(main)
        self.critical = int(crit)
        self.mastery = int(mastery)
        self.haste = int(haste)
        self.versatility = int(ver)

        if tier.lower()=="true":
            self.tier = True
        else:
            self.tier = False

        self.cl = cl.lower()
        self.boss = boss
        self.gem_slot = gem_slot

    def show(self):
        print(self.name,",",self.dificulty,"(",self.type,",",self.slot,")","@",self.boss,":","\n\t",self.stamina,self.attribute,self.critical,self.mastery,self.haste,self.versatility,self.tier,self.cl)

    def Get_Score(self,stam_weight,main_weight,crit_weight,mast_weight,haste_weight,vers_weight):
        sum = self.stamina*stam_weight + self.attribute*main_weight + self.critical*crit_weight + self.mastery*mast_weight + self.haste*haste_weight + self.versatility*vers_weight
        if self.gem_slot:
            sum += 150*max(crit_weight,mast_weight,haste_weight,vers_weight)*0,75
        return sum