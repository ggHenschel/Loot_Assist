import csv
import sys

class Player_Class:
    def __init__(self,class_name,class_spec):
        self.class_name = class_name.lower()
        self.class_spec = class_spec.lower()

        self.found = False

        file = open("player_class.csv")

        csv_reader = csv.reader(file,delimiter=";")

        for row in csv_reader:
            if row[0]== self.class_name and row[2]==self.class_spec:
                self.armor_type = row[1].lower()
                self.class_type = row[3].lower()
                self.stam_weight = float(row[4])
                self.main_weight = float(row[5])
                self.crit_weight = float(row[6])
                self.mast_weight = float(row[7])
                self.haste_weight = float(row[8])
                self.vers_weight = float(row[9])
                self.set_importance = row[10]
                self.found = True
                break

        if not self.found:
            print("Class or Spec not found, plz run program again or include class/spec in 'player_class.csv'.")
            sys.exit(-1)


    def get_weights(self):
        return (self.stam_weight,self.main_weight,self.crit_weight,self.mast_weight,self.haste_weight,self.vers_weight)

    def Force_set(self):
        if self.set_importance=="F4":
            return 4
        elif self.set_importance=="F2":
            return 2
        elif self.set_importance=="NI":
            return 0
        else:
            return -1

    def print(self):
        print(self.class_name,self.class_spec,self.stam_weight,self.main_weight,self.crit_weight,self.mast_weight,self.haste_weight,self.vers_weight,self.Force_set())
