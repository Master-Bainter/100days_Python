

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        position = letters.index(char) + shift_amount
        position %= len(letters)
        encrypted_text += letters[position]
    return encrypted_text
    #print(f"Your encrypted text is: {encrypted_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for char in original_text:
        position = letters.index(char) - shift_amount
        position %= len(letters)
        decrypted_text += letters[position]
    return decrypted_text
    #print(decrypted_text)

def caesar(choice, original_text, shift_amount):
    if choice == "encode":
        return f"Your encrypted text is {encrypt(original_text, shift_amount)}"
    elif choice == "decode":
        return f"Your decrypted text is {decrypt(original_text, shift_amount)}"
    else:
        print("Your choice was invalid")

result = caesar(direction, text, shift)

print(result)
# print(encrypt())
# print(decrypt())
#print(f"Your encrypted text is {encrypt()}")
#print(f"Your decrypted text is {decrypt()}")

