import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)

global random_word

chances = len(stages)

random_word = random.choice(word_list)

answer_lst = list(random_word)

random_word_length = len(random_word)
lst = ['_']*random_word_length


def print_list(lst: list):
    for i in lst:
        print(i, end=' ')
    print()




def contains_char(answer_list: list, player_list: list, guesses: int):
    remaining_guesses = guesses
    while remaining_guesses > 0:
        letter = input("Enter a character: ").lower()

        if letter in answer_list:
            for index, value in enumerate(answer_list):
                if value == letter:
                    player_list[index] = value
        else:
            print(f"You guessed {letter}, that's not in the word")
            remaining_guesses -= 1
            print(stages[remaining_guesses])

        print_list(player_list)

        if answer_list == player_list:
            print("Congratulations! You've guessed the word. The word was {}".format(random_word))
            return

    print(f"Sorry, you've run out of guesses. The word was '{random_word}'.")

contains_char(answer_lst,lst,chances)