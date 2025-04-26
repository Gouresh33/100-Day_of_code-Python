import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock,paper,scissors]
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choise >= 0 or user_choise <= 2:
    print(game_img[user_choise])

computer_choise = random.randint(0,2)
print("computer choise:")
print(game_img[computer_choise])
if user_choise >= 3 or user_choise < 0:
    print("You typed an invalid number, you lose!")
elif user_choise == 0 and computer_choise == 2:
    print("You Win!")
elif computer_choise == 0 and user_choise == 2:
    print("You lose!")
elif computer_choise > user_choise:
    print("computer wins!")
elif user_choise > computer_choise:
    print("You Win!")
elif user_choise == computer_choise:
    print("It's a draw")
