import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = nr_letters
password = []
count_letter = 0count_symbol = 0
count_number = 0
for i in range(0,total,1):
    choice = random.randint(1,3)
    if choice == 1 and count_letter <= nr_letters:
        choice2 = random.randint(0,len(letters)-1)
        password.append(letters[choice2])
        count_letter += 1
    elif choice == 2 and count_symbol <= nr_symbols:
        choice2 = random.randint(0,len(symbols)-1)
        password.append(symbols[choice2])
        count_symbol += 1
    elif choice == 3 and count_number <= nr_numbers:
        choice2 = random.randint(0,len(numbers)-1)
        password.append(numbers[choice2])
        count_number += 1
print("Your password is: ", end="")
for i in password:
    print(i, end="")

