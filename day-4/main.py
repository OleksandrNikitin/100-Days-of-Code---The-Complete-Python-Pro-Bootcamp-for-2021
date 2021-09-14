import secrets

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

options = [rock, paper, scissors]
computer_choice = secrets.choice(options)
user_choice = int(input("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

print(f"You chose:\n{options[user_choice]}\n")
print(f"Computer chose:\n{computer_choice}\n")

if user_choice == 0 and computer_choice is rock or user_choice == 1 and computer_choice is paper or user_choice == 2 \
        and computer_choice is scissors:
    print("No winner")
elif user_choice == 0 and computer_choice is paper or user_choice == 1 and computer_choice is scissors or \
        user_choice == 2 and computer_choice is rock:
    print("You lose")
elif user_choice == 0 and computer_choice is scissors or user_choice == 1 and computer_choice is rock or \
        user_choice == 2 and computer_choice is paper:
    print("You win")
