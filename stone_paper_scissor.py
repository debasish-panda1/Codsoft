import random
rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_jpgs = [rock,paper,scissor]
user_choice = int(input("enter your choice: 0 for ROCK,1 for PAPER,2 for SCISSOR"))
if user_choice >=3 or user_choice < 0:
    print("you entered invaild number,you lose.")
else:  
    print("YOU CHOOSE:")
    print(game_jpgs[user_choice])
    computer_choice = random.randint(0,2)
    print("COMPUTER CHOOSE:")
    print(game_jpgs[computer_choice])
    if computer_choice == user_choice:
      print("it is a draw")
    elif computer_choice ==0 and user_choice==2:
      print("you lose")
    elif user_choice ==0 and computer_choice==2:
      print("you win")    
    elif computer_choice > user_choice:
      print("you losse")
    elif user_choice > computer_choice:
      print("you win") 
           