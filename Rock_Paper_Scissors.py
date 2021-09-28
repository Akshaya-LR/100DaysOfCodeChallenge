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
#Save the above three variables in a list

choices = [rock,paper,scissors]

#Greetings to the user
print("Welcome to the Rock, Paper and Scissors Challenge!\n")

#Ask the user to choose between Rock, Paper and Scissors and save it in variable choice_of_user

choice_of_user = int(input("Choose\n '0' - Rock\n '1' - Paper\n '2' - Scissors\n"))

#Use Ramdom() module to allow the computer to choose an integer from 0, 1, 2 and save it in a variable named random_choice

random_choice = random.randint(0,2)

#Print the choice made by the user and the computer. Check the below condition to see if the user enters 0-2 to avoid Index Error

if choice_of_user >= 3:
  print("Please enter a valid number")
   
else:
  print(f"You choose:\n {choices[choice_of_user]}")
  print(f"Computer chose:\n {choices[random_choice]}\n\n")  

  #Specify the rules of Rock, Papers and Scissors game using If- Else conditions.

  #Condition - 1 : Rock beats scissors
  #Condition - 2 : Paper beats rock  
  #Condition - 3 : Scissors beats paper


  if (choice_of_user == 0 and random_choice == 0) or (choice_of_user == 1 and random_choice == 1) or (choice_of_user == 2 and random_choice == 2):
    print("\n\nIt's a draw.. :o\n\n")

  if (choice_of_user == 0 and random_choice == 2) or (choice_of_user == 1 and random_choice == 0) or (choice_of_user == 2 and random_choice == 1):
    print("\n\nYou won! :-)\n\n")

  if (choice_of_user == 0 and random_choice == 1) or (choice_of_user == 1 and random_choice == 2) or (choice_of_user == 2 and random_choice == 0):
    print("\n\nYou lose! :-/\n\n")
