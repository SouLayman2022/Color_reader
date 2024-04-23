import cv2
import os

def resize_and_rename_images(input_dir, output_dir, theme_name, width=1280, height=720):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of image files in input directory
    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Resize and rename images
    for i, image_file in enumerate(image_files):
        # Read image
        img_path = os.path.join(input_dir, image_file)
        img = cv2.imread(img_path)

        # Resize image
        resized_img = cv2.resize(img, (width, height))

        # Construct new filename
        new_filename = f"{theme_name}{i+1}.jpeg"
        output_path = os.path.join(output_dir, new_filename)

        # Save resized image
        cv2.imwrite(output_path, resized_img)
        print(f"Image {img_path} resized and saved as {output_path}")

# Example usage
input_directory = r"C:\Users\soula\Desktop\Projects\Color_reader"
output_directory = r"C:\Users\soula\Desktop\Projects\Color_reader\output"
theme_name = "Morocco"

resize_and_rename_images(input_directory, output_directory, theme_name)
