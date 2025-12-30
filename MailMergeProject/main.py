file = open(r"C:\KunalGoel\Python_Course\MailMergeProject\Input\Letters\starting_letter.txt","r")
letter = file.read()
file.close()

file = open(r"C:\KunalGoel\Python_Course\MailMergeProject\Input\Names\invited_names.txt","r")
names = file.readlines()
file.close()
for i in range(0,len(names)-1,1):
    # print(names[1])
    names[i] = names[i][:len(names[i])-1]
    print(names[i])

    temp_letter = letter.replace("[name]",names[i])
    print(temp_letter)

    file = open(rf"C:\KunalGoel\Python_Course\MailMergeProject\Output\ReadyToSend\{names[i]}.txt","w")
    file.write(temp_letter)
    file.close()

temp_letter = letter.replace("[name]",names[len(names)-1])
print(temp_letter)

file = open(rf"C:\KunalGoel\Python_Course\MailMergeProject\Output\ReadyToSend\{names[i]}.txt","w")
file.write(temp_letter)
file.close()
