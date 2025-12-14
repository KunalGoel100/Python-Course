import random



print('''
I8,        8        ,8I          88                                                       
`8b       d8b       d8'          88                                                       
 "8,     ,8"8,     ,8"           88                                                       
  Y8     8P Y8     8P  ,adPPYba, 88  ,adPPYba,  ,adPPYba,  88,dPYba,,adPYba,   ,adPPYba,  
  `8b   d8' `8b   d8' a8P_____88 88 a8"     "" a8"     "8a 88P'   "88"    "8a a8P_____88  
   `8a a8'   `8a a8'  8PP""""""" 88 8b         8b       d8 88      88      88 8PP"""""""  
    `8a8'     `8a8'   "8b,   ,aa 88 "8a,   ,aa "8a,   ,a8" 88      88      88 "8b,   ,aa  
     `8'       `8'     `"Ybbd8"' 88  `"Ybbd8"'  `"YbbdP"'  88      88      88  `"Ybbd8"' 
     ''')
total1 = 0
kill1 = 0
total2 = 0
kill2 = 0
count1 = 0
count2 = 0
i = 1
while (i == 1 or i == 2) and (count1 <=10 or count2 <=10):
    i = int(input("Player: "))
    if i == 1 and kill1 != 10:
        rand = random.randrange(1, 7)
        count1 += 1
        if rand == 5 or rand == 7:
            print("\t", rand)
            print("Player1 Out")
            kill1 = 10
        else:
            print("\t", rand)
            total1 += rand
    elif i == 2 and kill2 != 10:
        rand = random.randrange(1,7)
        count2 += 1
        if rand == 5 or rand == 7:
            print("\t", rand)
            print("Player2 Out")
            kill2 = 10
        else:
            print("\t", rand)
            total2 += rand
    else:
        print("Wrong choice")
        i = 1
    if kill1 == 10 and kill2 == 10:
        break
print(f"Player1 Total = {total1}\n")
print(f"Player2 Total = {total2}")

