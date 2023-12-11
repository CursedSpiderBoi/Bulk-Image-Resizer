from PIL import Image
import os

def resize_images(path, width, height):
    try:
        if not os.path.exists(path):
            print(f"Error: The specified path '{path}' does not exist.")
            return

        if not isinstance(width, int) or not isinstance(height, int) or width <= 0 or height <= 0:
            print("Error: Please enter valid positive integers for width and height.")
            return

        backup_path = os.path.join(path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)

            if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                img = Image.open(filepath)

                resized_img = img.resize((width, height), Image.ANTIALIAS)

                # Backup the original image
                img.save(os.path.join(backup_path, filename))

                resized_img.save(filepath)

                print(f"Resized: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input("Enter the path of the images: ")
    width = int(input("Enter the desired width in pixels: "))
    height = int(input("Enter the desired height in pixels: "))

    resize_images(path, width, height)

    print("Resize complete.")
