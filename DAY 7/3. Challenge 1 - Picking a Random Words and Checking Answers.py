# import random

# World = ["SAIF", "ALI", "SANA", "ZAID"]
# chosen_world = random.choice(World)  
# print(f'PESST , THE SOLUTION IS {chosen_world}')
# display=[]
# for _ in range (len(chosen_world)):
#     display += "_"
#     print(display)
    
# guess = input("Guess a letter: ").lower()

# for latter in chosen_world:
#     if latter==guess:
#         print("RIGHT")
#     else:
#         print("WRONG")
import random

World = ["SAIF", "ALI", "SANA", "ZAID"]
chosen_world = random.choice(World).lower()  # Choose a random word and convert it to lowercase
print(f'PSSST, THE SOLUTION IS {chosen_world}')  # Debugging hint (you can remove this if needed)

# Create an empty display with underscores representing unguessed letters
display = ["_" for _ in range(len(chosen_world))]  
print(f"Current Word: {' '.join(display)}")  # Display the word as underscores initially

guess = input("Guess a letter: ").lower()

# Check the guessed letter and update the display accordingly
for index, letter in enumerate(chosen_world):
    if letter == guess:
        display[index] = letter  # Replace the underscore with the correctly guessed letter

# Display the updated word with correct guesses
print(f"Current Word: {' '.join(display)}")
