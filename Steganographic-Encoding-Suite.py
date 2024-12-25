from PIL import Image
import numpy as np

def encode_message(image_path, message, output_path):
    """Encodes a message into an image using LSB steganography."""
    try:
        img = Image.open(image_path).convert("RGB")  # Ensure RGB format
        img_array = np.array(img)
        message += "\0\0\0"  # Add delimiter to mark the end of the message

        binary_message = ''.join(format(ord(char), '08b') for char in message)
        message_len = len(binary_message)

        if message_len > img_array.size:
            raise ValueError("Message is too long to be encoded in this image.")

        index = 0
        for row in range(img_array.shape[0]):
            for col in range(img_array.shape[1]):
                for channel in range(3):  # Iterate through R, G, B channels
                    if index < message_len:
                        # Get the LSB of the pixel value
                        pixel_lsb = img_array[row, col, channel] & 1

                        # Get the current message bit
                        message_bit = int(binary_message[index])

                        # Modify the LSB if it's different from the message bit
                        if pixel_lsb != message_bit:
                            if message_bit == 0:
                                img_array[row, col, channel] &= ~1  # Set LSB to 0
                            else:
                                img_array[row, col, channel] |= 1   # Set LSB to 1
                        index += 1
                    else:
                        break
                else:
                    continue
                break
            else:
                continue
            break


        encoded_image = Image.fromarray(img_array)
        encoded_image.save(output_path)
        print(f"Message successfully encoded and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred during encoding: {e}")

def decode_message(image_path):
    """Decodes a hidden message from an image."""
    try:
        img = Image.open(image_path).convert("RGB")
        img_array = np.array(img)

        binary_message = ""
        decoded_message = ""

        for row in range(img_array.shape[0]):
            for col in range(img_array.shape[1]):
                for channel in range(3):
                    binary_message += str(img_array[row, col, channel] & 1)
                    if len(binary_message) % 8 == 0: #check if we have a complete byte
                        byte = binary_message[-8:]
                        char_code = int(byte, 2)
                        if char_code == 0: #check for delimiter
                            return decoded_message
                        decoded_message += chr(char_code)

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred during decoding: {e}")
        return None

if __name__ == "__main__":
    while True:
        print("\nSteganography Tool")
        print("1. Encode message")
        print("2. Decode message")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("Enter path to image file: ")
            message = input("Enter message to encode: ")
            output_path = input("Enter path to save encoded image: ")
            encode_message(image_path, message, output_path)
        elif choice == "2":
            image_path = input("Enter path to encoded image file: ")
            decoded_message = decode_message(image_path)
            if decoded_message:
                print("Decoded message:", decoded_message)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")