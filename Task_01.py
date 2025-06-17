def encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  
            offset = 65 if char.isupper() else 97
            encrypted_character = chr((ord(char) - offset + shift) % 26 + offset)
            result = result+encrypted_character
        else:
            result += char 
    return result

def decryption(text, shift):
    return encryption(text, -shift)   
    
#user interface
print("This is basic Caesar Cipher Program ")
choice = input("Do you want to Encrypt or Decrypt? (E/D):").strip().upper()

if choice in ['E', 'D']:
    message = input("Enter The message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    
    if choice == 'E':
        encrypted = encryption(message, shift)
        print("Encrypted Message:", encrypted)
    else:
        decrypted = decryption(message, shift)
        print("Decrypted Message:", decrypted)
else:
    print("Invalid choice. Please enter E or D.")