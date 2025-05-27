def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            elif mode == 'decrypt':
                shifted = (ord(char) - shift_base - shift) % 26 + shift_base
            result += chr(shifted)
        else:
            # Keep non-alphabet characters unchanged
            result += char

    return result


def main():
    print("Caesar Cipher Program (Shift: 2)")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the text: ")
    shift = 2

    result = caesar_cipher(text, shift, mode=choice)
    print(f"\nResult ({choice.title()}ed): {result}")


if __name__ == "__main__":
    main()
