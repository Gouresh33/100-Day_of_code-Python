from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
print(logo)

def cheak_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

def difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_num = randint(0, 100)

    turns = difficulty()

    guess = 0
    while guess != random_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = cheak_answer(guess, random_num, turns)
        if turns == 0:
            print(f"You've run out of guesses. You lose! The number was {random_num}")
            return
        elif guess != random_num:
            print("Guess again.")

game()