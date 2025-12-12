from PIL import Image

def xor_encrypt_decrypt(input_path, output_path, key):
    """
    Encrypt or decrypt an image using XOR pixel manipulation.
    Using the same key will reverse the operation (XOR is reversible).
    """
    img = Image.open(input_path)
    pixels = img.load()
    
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # XOR operation
            r ^= key
            g ^= key
            b ^= key

            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print(f"Saved: {output_path}")


# ----- User Interface -----
if __name__ == "__main__":
    print("=== Image Encryption Tool (XOR Pixel Manipulation) ===")

    mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter numeric key (0–255): "))

    xor_encrypt_decrypt(input_path, output_path, key)

    print("Operation completed.")