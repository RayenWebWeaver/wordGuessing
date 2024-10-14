import random 

words = [
    "read",
    "sleep",
    "code",
    "eat",
    "repet"
]
random_word = random.choice(words)
dispaly = ["-"] * len(random_word)
print (" ".join(dispaly))


lives = 12 
guessed_letters = []
while "-" in dispaly and lives > 0:
    guess = input ("Plese guess a letter: ")
    guessed_letters.append(guess)

    if guess not in random_word: 
        lives -= 1
        print(f"""
        opps !
        steel posible {lives} more lives""")
        print (" ".join(dispaly))
        continue

    if guess in  guessed_letters:
        lives = lives
        print ("you are all ready choice this letter")
        print (f"you steel have {lives} lives .")
        

    for poistion in range(len(random_word)):
        if random_word[poistion] == guess:
             dispaly[poistion] = guess

    print (" ".join(dispaly))


if lives == 0 : 
    print ("you lose")
else:
    print ("you Win")