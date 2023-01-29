import random   #yes lmao this program uses random module
import pyperclip as pc

def enigma_encrypt():
    encrypt_range = 10

    en_msg = input("Enter string: ")
    sep = input('What is your seperator[leave blank to use an invisible seperator]: ')
    if sep == '':
        sep = '​'   #seperated by 'U+200B'
    
    en_lst = list(en_msg)
    ans = []
    for i in range(len(en_lst)):
        key = random.randint(1,encrypt_range) #selects a random number from 1 to 1B
        enc1 = ord(en_lst[i])+key #finds ascii value of letter and adds key to it
        enc2 = enc1 * key
        enc3 = enc2 - key
        h_k = (str(hex(key))).replace('0x','') #removes the '0x' that precedes every hex number  
        h_e = (str(hex(enc3))).replace('0x','')
        ans.append(str(h_k))
        ans.append(str(h_e))
    fin = sep.join(ans)
    print("Encrypted message is:",fin)
    pc.copy(fin)
    print('\n Copied to Clipboard! \n')


def enigma_decrypt():
    de_msg = input("\n \n \nEnter string: ")
    sep = input('What is your seperator[leave blank to use an invisible seperator]: ')
    if sep == '':
        sep = '​'#it is split by invisible character 'U+200B'
    de_lst = de_msg.split(sep)
    print("\n The Decrypted message is: ",end="")
    for i in range(1,len(de_lst),2):
        key = int('0x'+str(de_lst[i-1]),16)     #adds the '0x' and turns it into base-10 integer
        num = int('0x'+str(de_lst[i]),16)
        dec1 = num + key
        dec2 = dec1 // key
        dec3 = chr(dec2 - key) #finds the letter from the integer remaining
        print(dec3,end="")
    print('\n')


while True:
    ans = input("\n \n1.Encrypt your message. \n2.Decrypt your message.\n3.Exit\nEnter choice: ")
    if ans == '1':
        enigma_encrypt()
    elif ans == '2':
        enigma_decrypt()
    elif ans == '3':
        input('Exited.\n')
        break
    else:
        print("Invalid Input!!!")
