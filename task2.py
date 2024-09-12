from PIL import Image
import os

# Function to encrypt an image
def encrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert('RGB')
    except  FileNOtFoundError:
        print("image file not found. Please check the path.")
        return

    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

# Encrypt the image by altering pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    img.save(output_path)
    print("image encrypted and save as {output_path}")
# Function to decrypt an image
def decrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert('RGB')
    except FileNotFoundError:
        print("Image file not found. Please check the path.")
        return

    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
# Decrypt the image by reversing the encryption process
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    img.save(output_path)
    print("Image decrypted and saved as {output_path}")

# Main function to handle user input
def main():
  choice = input("Do you want to encrypt or decrypt the image? (e/d): ").lower()
  image_path = input("Enter the image file path (e.g., image.jpg): ")
  output_path = input("Enter the output file path (e.g., output.jpg): ")
  key = int(input("Enter the encryption/decryption key (number): "))
  if choice == 'e':
    encrypt_image(image_path, output_path, key)
  elif choice == 'd':
    decrypt_image(image_path, output_path, key)
  else:
    print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()




