import pandas
file = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(file)
dict = {k.letter:k.code for (u,k) in file.iterrows()}
# print(dict)
def Word():
    try:
        word = input("Enter any string")
        ph = [dict[u.upper()] for u in word]
        ph = [dict[u.upper()] for u in word if u.isalpha()]
        print(ph)
    except:
        print("Enter Characters in Alphabets only")
        Word()
Word()