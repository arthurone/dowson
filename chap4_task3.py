import random
WORDS = ("ранмдом","слово","анаконда","питон","чебуратор")
word  = random.choice(WORDS)
correct = word
jumble =""
points = 5
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print("Начинаем игру")
print("вот ваше слово:",jumble)
guess = input("\nПопробуйте угадать исходное слово: ")
while guess != correct and guess != "":

    if guess == correct:
        print("ДА именно так Вы отгадали \n")
    elif guess != correct and guess !="подсказка":
        print("К сожалению вы не правы, чтобы получить подсказку введите подсказка (вы потеряете 1 балл): ")
        guess = input("Попробуйте угадать исходное слово: ")
    elif guess == "подсказка":
        points-= 1
        print("Вы потеряли 1 балл",correct[0:4])

        guess = input("Попробуйте угадать исходное слово: ")
print("Спасибо за игру. Вы набрали:", points, "баллов.")

