u_word = input("Введите слово: ")
dlina = len(u_word)
a_word = ""
for i in range((dlina-1),-1,-1):
    a_word += u_word[i]
print(a_word)