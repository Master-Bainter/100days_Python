

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

    print(f"Your encrypted text is: {encrypted_text}")



        #print(letters.index(char))
        #print(letters.index(char) + shift_amount)
        #print(char)


encrypt(text, shift)