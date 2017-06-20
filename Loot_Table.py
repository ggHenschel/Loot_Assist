import csv
import Item

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
            self.Itens.append(Item.Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))

        file.close()

    def print_loot_table(self):
        for item in self.Itens:
            item.show()
