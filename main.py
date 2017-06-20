import Character


loot = []

loot.append("Tomb of Sageras Loot Table Normal.csv")
#loot.append("Tomb of Sageras Loot Table Heroic.csv")

Naboco = Character.Character("Naboco","shaman","resto")

Naboco.Load_loot_batch(loot)

Naboco.Compare()


