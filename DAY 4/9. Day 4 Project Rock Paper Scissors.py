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
---'    ____)____
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
print(rock)
game_image=[rock,paper,scissors]
user_choice = int(input("WHAT DO YOU CHOOSE? 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer Choice: {computer_choice}")
if user_choice < 0 or user_choice > 2:
    print("YOU ENTERED AN INVALID NUMBER! YOU LOSE 😥")
elif user_choice == computer_choice:
    print("IT'S A DRAW!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
    print("YOU WIN 😀")
else:
    print("YOU LOSE 😥")
