import random   #yes lmao this program uses random module
import pyperclip as pc

def start():
    print("\n \nEnter 1 to encrypt your message. \nEnter 2 to decrypt your message.")
    ans = int(input("Enter choice: "))
    if ans == 1:
        enigma_encrypt()
    elif ans == 2:
        enigma_decrypt()
    else:
        print("Invalid Input!!!")
        start()


def repeat():
    ans = input("\n \nWould you like to encrypt/decrypt again?[yes/no]: ")
    if ans.lower() == "yes":
        start()
    elif ans.lower() == "no":
        rly = input("Are you sure you want to exit?[yes/no]: ")
        if rly.lower() == "yes":
            exit()
        elif rly.lower() == "no":
            start()
        else:
            repeat()
    else:
        print("Invalid Input!!!")
        repeat()


def enigma_encrypt():
    en_msg = input("Enter string: ")
    en_lst = list(en_msg)
    ans = []
    for i in range(len(en_lst)):
        key = random.randint(1,1_000_000_000) #selects a random number from 1 to 1B
        enc1 = ord(en_lst[i])+key #finds ascii value of letter and adds key to it
        enc2 = enc1 * key
        enc3 = enc2 - key
        h_k = (str(hex(key))).replace('0x','') #removes the '0x' that precedes every hex number  
        h_e = (str(hex(enc3))).replace('0x','')
        ans.append(str(h_k))
        ans.append(str(h_e))
    fin = '​'.join(ans)                 #seperated by 'U+200B'
    print("Encrypted message is:",fin,)
    pc.copy(fin)
    print('\n Copied to Clipboard! \n')
    repeat()


def enigma_decrypt():
    de_msg = input("\n \n \nEnter string: ")
    de_lst = de_msg.split('​')  #it is split by invisible character 'U+200B'
    print("\n The Decrypted message is: ",end="")
    for i in range(1,len(de_lst),2):

        key = int('0x'+str(de_lst[i-1]),16)     #adds the '0x' and turns it into base-10 integer
        num = int('0x'+str(de_lst[i]),16)
        dec1 = num + key
        dec2 = dec1 // key
        dec3 = chr(dec2 - key) #finds the letter from the integer remaining
        print(dec3,end="")
    repeat()


start()
