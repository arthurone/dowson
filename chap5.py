# Records
scores = []
choise = None
while choise != "0":
    print("""
    Records
    0 - Exit
    1 - Show records
    2 - Add Records
    3 - Delete Records
    4 - Sort list""")
    choise = input("Your choise: ")
    print()
    if choise == "0":
        print("GoodBye")
    elif choise == "1":
        print("Records")
        for score in scores:
            print(score)
    elif choise == "2":
        score = int(input("Enter your record"))
        scores.append(score)
    elif choise == "3":
        score = int(input("What are record you want to delete"))
        if score in scores:
            scores.remove(score)
        else:
            print("Result", score, "not find in records")
    elif choise == "4":
        scores.sort(reverse=True)
    else:
        print("This point is not in menu")
input("\nPress Enter to exit")
