import random
import string

characters = " " + string.punctuation + string.ascii_letters + string.digits
characters = list(characters) 

shuffled = characters.copy()
random.shuffle(shuffled)

def encryption():

    text = input("Enter a message : ")
    cipher = ""

    for i in text:

        index = characters.index(i)
        cipher += shuffled[index]

    print(f"\nOriginal message : {text}")
    print(f"Encrypted message : {cipher}\n")

def decryption():

    cipher = input("Enter a message : ")
    text = ""
    
    for i in cipher:
        index = shuffled.index(i)
        text += characters[index]

    print(f"\nEncrypted message : {cipher}")
    print(f"Original message : {text}\n")

encryption()
decryption()
