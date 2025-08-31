from PIL import Image


def xor_encrypt_decrypt(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Saved encrypted image to {output_path}")


# Example usage
if __name__ == "__main__":
    input_path = r"D:\img1.avif"  # Replace with your image path
    output_path = r"D:\img2.webp"  # Output file name
    key = 123  # Any integer key

    xor_encrypt_decrypt(input_path, output_path, key)