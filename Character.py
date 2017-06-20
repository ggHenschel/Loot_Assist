import Player_Class as pc
import Loot_Table as lt
import sys

class Character:
    def __init__(self,Name,Class,Spec):
        self.Player_c = pc.Player_Class(Class,Spec)
        self.Name = Name
        self.Loot = lt.Loot_Table()
        self.Force_Set_Value = self.Player_c.Force_set()

    def Load_Loot_Table(self,path_to_loot):
        self.Loot.import_loot_table(path_to_loot)

    def Load_loot_batch(self,batch_path):
        for path in batch_path:
            self.Loot.import_loot_table(path)

    def Compare(self):
        self.Cmp_results = []

        (self.stam_weight, self.main_weight, self.crit_weight, self.mast_weight, self.haste_weight, self.vers_weight) = self.Player_c.get_weights()

        for item in self.Loot.Itens:
            self.Cmp_results.append((item.Get_Score(self.stam_weight, self.main_weight, self.crit_weight, self.mast_weight, self.haste_weight, self.vers_weight),item))

        self.Cmp_results.sort(key=lambda tup: tup[0],reverse=True)

        self.Set_Pieces = []
        self.Head = []
        self.Shoulders = []
        self.Neck = []
        self.Chest = []
        self.Back = []
        self.Wrist = []
        self.Hands = []
        self.Waist = []
        self.Legs = []
        self.Feet = []
        self.Rings = []
        self.Trinkets = []
        self.Other = []

        for (GS,item) in self.Cmp_results:
            cont = True
            if item.tier and item.cl==self.Player_c.class_name:
                self.Set_Pieces.append((GS,item))
                cont = True
            elif item.tier and not item.cl==self.Player_c.class_name:
                cont = False

            if cont and (item.type==self.Player_c.armor_type or item.type=="neutral"):
                if item.slot=="head":
                    self.Head.append((GS,item))
                elif item.slot=="shoulder":
                    self.Shoulders.append((GS,item))
                elif item.slot=="neck":
                    self.Neck.append((GS, item))
                elif item.slot=="chest":
                    self.Chest.append((GS,item))
                elif item.slot=="back":
                    self.Back.append((GS,item))
                elif item.slot=="wrist":
                    self.Wrist.append((GS, item))
                elif item.slot=="hands":
                    self.Hands.append((GS,item))
                elif item.slot=="waist":
                    self.Waist.append((GS,item))
                elif item.slot=="legs":
                    self.Legs.append((GS,item))
                elif item.slot=="feet":
                    self.Feet.append((GS,item))
                elif item.slot=="finger":
                    self.Rings.append((GS,item))
                elif item.slot=="trinket" and item.cl==self.Player_c.class_type:
                    self.Trinkets.append((GS,item))
                elif item.slot=="trinket" and item.cl=="dps" and (self.Player_c.class_type=="ranged" or self.Player_c.class_type=="melee"):
                    self.Trinkets.append((GS, item))
                else:
                    self.Other.append((GS,item))

        if self.Force_Set_Value>=0:
            for (GS, item) in self.Set_Pieces[0:self.Force_Set_Value]:
                if item.slot=="head":
                    self.Head=[(GS,item)]
                elif item.slot=="shoulder":
                    self.Shoulders=[(GS,item)]
                elif item.slot=="chest":
                    self.Chest=[(GS,item)]
                elif item.slot=="hands":
                    self.Hands=[(GS,item)]
                elif item.slot=="back":
                    self.Back=[(GS,item)]
                elif item.slot=="legs":
                    self.Legs=[(GS,item)]
                else:
                    print("Error, INVALID TIER PIECE")
                    sys.exit(-2)

        self.CompDone = True

        # Agredador = []
        # Agredador.append(self.Set_Pieces)
        # Agredador.append(self.Head)
        # Agredador.append(self.Neck)
        # Agredador.append(self.Shoulders)
        # Agredador.append(self.Chest)
        # Agredador.append(self.Back)
        # Agredador.append(self.Wrist)
        # Agredador.append(self.Hands)
        # Agredador.append(self.Waist)
        # Agredador.append(self.Legs)
        # Agredador.append(self.Feet)
        # Agredador.append(self.Rings)
        # Agredador.append(self.Trinkets)
        # Agredador.append(self.Other)
        #
        # for ag in Agredador:
        #     #print(ag.__str__())
        #     for (GS,item) in ag:
        #         print(item.name,item.type,item.cl,item.slot,GS)
        #     print("------")

    def Print_Choices(self):
        print("Character: ",self.name,self.Player_c.class_spec.title(),self.Player_c.class_name.title())
        print("\t-Head:\t",self.Head[0][1])




