import random
x = 1
y = 100
tries = 1
pc_n = random.randint(x,y)
print(pc_n)
ask = input("угадал")
while ask != "да":
    if ask == "да":
        print("число", pc_n, "угадал с ", tries, "попытки")
    else:
        answer = input("больше или меньше?")
        if answer == "больше":
            x = pc_n + 1
            pc_n = random.randint(x,y)
            print(pc_n)
            ask = input("угадал?")
        elif answer == "меньше":
            y = pc_n - 1
            pc_n = random.randint(x,y)
            print(pc_n)
            ask = input("угадал?")
    tries +=1
print("угадал c ", tries, "попытки, это число", pc_n)















