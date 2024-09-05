import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
game_over = False
matched_letters = []

for position in range(word_length):
    placeholder += "_"

print(logo + "\n")
print("Word to guess: " + placeholder)

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************\n")
    guess = input("Guess a letter: ").lower()

    if guess in matched_letters:
        print(f"You've already guessed {guess}")
        lives -= 1

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            matched_letters.append(guess)
        elif letter in matched_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"It was {chosen_word}! You lost :(")

    if "_" not in display:
        game_over = True
        print("****************************YOU WON :) ****************************")

    hangman_stage = stages[lives]
    print(hangman_stage)
