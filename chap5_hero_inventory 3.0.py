#Арсенал героя 3
inventory = ["knife", "helm", "shield", "boots"]
print("\nIn your inventory: ")
for item in inventory:
    print(item)
input("Press Enter to continuous")
print("\nNow in your inventory", len(inventory), "items")
input("\nPress Enter to continuous")
if "shield" in inventory:
    print("you have a chance")
index = int(input("\nEnter index one of your item"))
print("In index", index, "in your inventory is", inventory[index])
start = int(input("\nEnter start index of cut"))
finish = int(input("Enter finish index of cut"))
print("cut of inventory[", start, ":", finish, "] - This", end="")
print(inventory[start:finish])
input("\nPress enter to continuous")
chest = ["gols", "gems"]
print("You are find a chest. This is inside: ")
print(chest)
print("You pickup a chest")
inventory += chest
print("Now you have a: ")
print(inventory)
input("\n\nPress Enter to continuous")
print("You change your might to crossbow")
inventory[0] = "crossbow"
print("Now your arsenal contains: ")
print(inventory)
input("\nPress Enter to continuous")
print("With gold and gems you buy magic crystal, that can predict future")
inventory[4:6] = ["magic crystal"]
print("Now in your inventory")
print(inventory)
input("\nPress Enter to continuous")
print("In hard battle your shield was destroy")
del inventory[2]
print("Now in your inventory")
print(inventory)
input("\nPress Enter to continuous")
print("Thieves steal your things")
del inventory[:2]
print("In inventory only ")
print(inventory)
input("\nPress Enter to exit")



