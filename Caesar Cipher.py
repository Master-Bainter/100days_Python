

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(original_text = text, shift_amount = shift):
    encrypted_text = "".lower()
    for char in original_text:
        position = letters.index(char) + shift_amount
        position %= len(letters)
        encrypted_text += letters[position]
    return encrypted_text
    #print(f"Your encrypted text is: {encrypted_text}")


def decrypt(original_text = text, shift_amount = shift):
    decrypted_text = "".lower()
    for char in original_text:
        position = letters.index(char) - shift_amount
        position %= len(letters)
        decrypted_text += letters[position]
    return decrypted_text
    #print(decrypted_text)

def caesar(choice = direction):
    if choice == "encode":
        return f"Your encrypted text is {encrypt()}"
    elif choice == "decode":
        return f"Your decrypted text is {decrypt()}"
    else:
        print("Your choice was invalid")


print(caesar())
# print(encrypt())
# print(decrypt())
#print(f"Your encrypted text is {encrypt()}")
#print(f"Your decrypted text is {decrypt()}")

