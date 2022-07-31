import random
words = ["Bounce", "melman", "bauty", "torsman"]
new = []
while len(words) != 0:
    k = len(words) - 1
    i = random.randint(0,k)
    print(words.pop(i))

