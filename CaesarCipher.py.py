from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Function cipher

def cipher(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
   
    else:
      end_text += char
        
  print(f"Here's the {(cipher_direction).lower()}d result: {end_text}")

print(logo)

#While loop to continue the program till the user wants to exit.

should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  
  text = input("Type your message:\n").lower()
  
  shift = int(input("Type the shift number:\n"))

  #If user enters shift value greater than 26
  shift = shift % 25
  
  #Calling cipher function
  cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Do you want to continue? Yes or No\n ").lower()

  #To exit the while loop, check if the user has entered NO.
  if restart == "no":
    should_continue = False
    print("Goodbye. Have a great day!")

