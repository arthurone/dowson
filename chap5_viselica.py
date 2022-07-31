import random
HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    0
    |    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
     ------
    |    |
    |    0     
    |    |
    |   -+-
    |
    |
    |
    |
    ----------
    """,
    """
        ------
       |    |
       |    0
       |    |
       |  /-+-
       |    
       |
       |
       |
       ----------
    """,
    """
           ------
          |    |
          |    0
          |  /-+-/
          |    
          |    
          |
          |
          |
          ----------
    """,
    """
           ------
          |    |
          |    0
          |  /-+-/
          |    |
          |    
          |   
          |   
          |
          ----------
    """,
    """
           ------
          |    |
          |    0
          |  /-+-/
          |    |
          |    |
          |   | 
          |   | 
          |
          ----------
    """,
    """
              ------
             |    |
             |    0
             |  /-+-/
             |    |
             |    |
             |   | |
             |   | |
             |
             ----------
       """,

)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")
word = random.choice(WORDS)
so_far = "_" * len(word)
wrong = 0
used = []
print("Welcome to game, GLHF")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou already take this char: \n", used)
    print("\nYou guess char look like:\n", so_far)
    guess = input("\n\n Enter your char")
    guess = guess.upper()
    while guess in used:
        print("You already use this char", guess)
        guess = input("\n\nEnter char: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYes char", guess, "in word")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                    new += guess
            else:
                    new += so_far[i]
        so_far = new
    else:
        print("\n Nope char", guess, "Not in word")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou was hang")
else:
    print("\n Your win")
print("\nWord is", word)
input("\n\nPress enter to exit")

