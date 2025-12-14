import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

word = word_list[random.randint(0,len(word_list)-1)]
temp = []
wrong = len(word) + 1
for i in word:
    temp += ["_"]
count = 1
print(f"You have {wrong} attempts to guess the word")
while count != 0 and wrong > 0:
    choice = input("Enter a character:  ")
    hit = 0
    for i in range(0,len(word)):
        if choice == word[i] and temp[i] == "_":
            temp[i] = choice
            print("Correct")
            hit = 1
    if hit == 0:
        print(f"{choice} is wrong Choice")
        wrong -= 1
        print(f"You have {wrong} attempts left")
    print(temp)
    count = 0
    for i in temp:
        if i == "_":
            count += 1
print("Completed")
print(f"The word is {word}")
