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
task = [rock,paper,scissors]
compchoice = random.randint(0,2)
choice = int(input("enter 0-Rock, 1-Paper, 2-Scissor\n"))
print(f"{task[choice]}\nComputer choice:\n{task[compchoice]}\n")
if choice == 0 and compchoice == 1:
    print("You Lose")
elif choice == 0 and compchoice == 2:
    print("You Win")
elif choice == 1 and compchoice == 0:
    print("You Win")
elif choice == 1 and compchoice == 2:
    print("You Lose")
elif choice == 2 and compchoice == 0:
    print("You Lose")
elif choice == 2 and compchoice == 1:
    print("You Lose")
else:
    print("Draw")
