alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choice = int(input("enter 1:Encryption, 2:Decryption "))
if choice == 1:
    word = input("enter word: ")
    pin = int(input("enter encryption pin: "))
    encrypt = ""
    for i in word:
        if i not in alphabet:
            encrypt += i
        else:
            j = alphabet.index(i)
            if j+pin >= len(alphabet):
                encrypt += alphabet[j + pin - len(alphabet)]
            else:
                encrypt += alphabet[j+pin]

    print(f"The Encrypted word: {encrypt}")
elif choice == 2:
    word = input("enter word: ")
    pin = int(input("enter decryption pin: "))
    decrypt = ""
    for i in word:
        if i not in alphabet:
            decrypt += i
        else:
            j = alphabet.index(i)
            if j-pin < 0:
                decrypt += alphabet[j-pin + len(alphabet)]
            else:
                decrypt += alphabet[j-pin]

    print(f"The Decrypted word: {decrypt}")
