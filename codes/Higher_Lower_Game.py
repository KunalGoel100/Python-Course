from game_data import data
import random

def calculate(choice, score, id, id2):
    if data[id]["follower_count"] > data[id2]["follower_count"]:
        actual = 1
    else:
        actual = 2
    if choice == actual:
        print("Correct")
        score += 1
        return [score, 0]
    else:
        print("Wrong")
        return [score, 1]

def game():
    print("Who has more followers\n")
    print(f"1: {data[id]["name"]} {data[id]["description"]}")
    print("OR")
    print(f"2: {data[id2]["name"]} {data[id2]["description"]}")

id = random.randint(0,len(data)-1)
id2 = random.randint(0,len(data)-1)

score = 0
hit = 0
while hit != 1:
    game()
    choice = int(input())
    [score, hit] = calculate(choice, score, id, id2)
    id = id2
    id2 = random.randint(0,len(data)-1)
    print(f"Score: {score}")




