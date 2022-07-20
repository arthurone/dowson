# Records
# Show work with lists

scores = []
none = None
menu_point = none
while menu_point != "0":
    print("""
    Records
    0 - Exit
    1 - Show records
    2 - Add Records
    3 - Delete Records
    4 - Sort list""")
    menu_point = input("Your choise: ")
    print()
    if menu_point == "0":
        print("GoodBye")
    elif menu_point == "1":
        print("Records")
        for score in scores:
            print(score)
    elif menu_point == "2":
        score = int(input("Enter your record: "))
        scores.append(score)
    elif menu_point == "3":
        score = int(input("What are record you want to delete: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Result", score, "not find in records")
    elif menu_point == "4":
        scores.sort(reverse=True)
    else:
        print("This point is not in menu")
input("\nPress Enter to exit")