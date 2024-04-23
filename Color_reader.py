import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import pandas as pd

# choose an image file
def choose_image():
    file_path = filedialog.askopenfilename()
    return file_path

# match colors with CSV data
def getColorName(R, G, B, csv_data):
    minimum_distance = float('inf')
    closest_color = None

    for i, row in csv_data.iterrows():
        d = abs(R - row.iloc[3]) + abs(G - row.iloc[4]) + abs(B - row.iloc[5])
        if d < minimum_distance:
            minimum_distance = d
            closest_color = row[1]

    return closest_color

# match colors from the image with colors from the CSV file
def match_colors(image_path, csv_path):
    # Read pic
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Unable to read the image.")
        return

    # Read CSV
    csv_data = pd.read_csv(csv_path)

    # Function to handle mouse click events
    def on_mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Get the RGB values of the clicked pixel
            b, g, r = img[y, x]

            # Compare the RGB values with colors from the CSV file
            color_name = getColorName(r, g, b, csv_data)
            messagebox.showinfo("Color", f"The color is {color_name}")

    # Display pic
    cv2.imshow("Image", img)
    
    # mouse callback
    cv2.setMouseCallback("Image", on_mouse_click)

    # Wait for a key press to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to handle button click event
def on_button_click():
    # Choose a pic
    image_path = choose_image()
    if image_path:
        # Match colors from the image with colors from the CSV file
        match_colors(image_path, "colors.csv")

# Create the GUI
root = tk.Tk()
root.title("Color Matcher by Soulayman")
root.geometry("400x200")  # Set a fixed size for the window

# Button
button = tk.Button(root, text="Choose Image", command=on_button_click)
button.pack()

# Start the GUI event loop
root.mainloop()
