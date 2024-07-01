def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")#parth
        return
    
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return

    if choice == 'encrypt':
        result = encrypt(message, shift)
    elif choice == 'decrypt':
        result = decrypt(message, shift)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    # Parth