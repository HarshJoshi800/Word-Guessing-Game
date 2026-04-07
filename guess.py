import secert_word


word_chosen = secert_word.computer_chosen_word(secert_word.List_of_words).lower()
lenght_of_word = len(word_chosen)

display = ['_' for i in range(lenght_of_word)]
guessed_history = []
lives = lenght_of_word

print("---Welcome to the word guessing game !---")
print(f"The word contian {lenght_of_word} character")
print(display)

def update_display(guess):
    for i in range(lenght_of_word):
        if word_chosen[i] == guess:
            display[i] = guess

while lives > 0:
    print(f" The attempt remaining : {lives}")
    guess = input("Guess a character : ").lower()

    if  guess.isalpha() and len(guess) == 1:
        pass
    else:
        print("Enter the valid character between a and z")
        continue
    
    if guess in guessed_history:
        print(f"You already tried '{guess}'. Try something else!")
    else:
        guessed_history.append(guess)
    
    if guess in word_chosen:
        print(f"Yes! {guess} is in word")
        update_display(guess)
    else:
        print(f"Sorry , {guess} is  not in word")
        lives -= 1

    print("Current Progress:"," ".join(display))

    if '_' not in display:
        print("You ! Guessed the word")
        break

if lives == 0:
    print(" GAME OVER.")
    print(f"The computer wins! The word was: {word_chosen}")  


