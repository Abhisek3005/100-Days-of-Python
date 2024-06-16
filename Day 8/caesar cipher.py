alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Direction=input("Type encode to encrypt,type decod to decrypt \n")
text=input("Enter a message \n")
shift=int(input("ENter the shift amount \n"))
def encrypt(text_input,shift_amount):
    cipher_text=""
    for position in text_input:
        value=alphabet.index(position)
        new_position=value+shift_amount
        new_letter=alphabet[new_position]
        #print(new_letter)
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")   


def decrypt(cipher_text,shift_amount):
    new_text=""
    for i in cipher_text:
        value1=alphabet.index(i)
        new_position1=value1-shift_amount
        new_text+=alphabet[new_position1]
    
    print(f"The decoded text is {new_text}") 



if Direction=="encrypt" :
    encrypt(text_input=text,shift_amount=shift)   
 
elif Direction=="decrypt":
    decrypt(cipher_text=text,shift_amount=shift) 

else:
    print("Go to google and search the spelling of encrypt or decrypt and then come back to run the code 😇")
    