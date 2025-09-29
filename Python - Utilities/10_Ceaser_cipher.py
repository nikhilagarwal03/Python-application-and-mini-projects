"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

import pyttsx3

def announce(message):
    engine = pyttsx3.init()
    print(message)
    engine.say(message)
    engine.runAndWait()
    
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

announce("Encrypter/Decrypter Program")
announce("For Encryption choose E and For Decryption choose D")
choice = input("E or D: ").strip().lower()

if choice == "e":
    text = input("enter the Message: \n")
    try:
        key = int(input("enter a number b/w 1 to 25: "))
        encrypted_text = encrypt(text,key)
        print(f"Encrypted Message: {encrypted_text}")
        announce("Message is Encrypted...")
    except ValueError:
        announce("Invalid key")

elif choice == "d":
    text = input("enter the Message: \n")
    try:
        key = int(input("enter a number b/w 1 to 25: "))
        decrypted_text = decrypt(text,key)
        print(f"Decrypted Message: {decrypted_text}")
        announce("Message is Decrypted...")
    except ValueError:
        announce("Invalid key")

else:
    announce("Invalid choice")