import pandas

file = pandas.read_csv("french_words.csv")
data = file.to_dict()
data["French"].pop(0)
print(len(data["French"]))