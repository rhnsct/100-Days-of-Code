
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = 'yes'   

def clear():
    os.system('clear')

def caeser(cipher_direction, cipher_text, cipher_shift):

    end_text = ""
    
    if cipher_direction == 'decode':
        cipher_shift *= -1

    
    for char in cipher_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + cipher_shift
            end_text += alphabet[new_position]
                
        else:
            end_text += char

    clear()    
    print(f'Your {cipher_direction} message is "{end_text}"')

        
    



while again == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
    if direction != 'encode' and direction != 'decode':
        clear()
        print("Invalid input!")
        continue
            
        
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
  
    
    caeser(cipher_direction = direction, cipher_text = text, cipher_shift = shift)
    
    again = input('Would you like to go again? "yes" or "no"?\n').lower()
    clear()