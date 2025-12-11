def caesar_cipher(text, shift, mode):
    result = ""
    # If decrypting, reverse the shift
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            # Shift within alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces, numbers, punctuation same

    return result

# ---- Main Program ----
print("==== Caesar Cipher Program ====")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()
if mode not in ["encrypt", "decrypt"]:
    print("Invalid option! Please choose 'encrypt' or 'decrypt'.")
else:
    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed message): {output}")
