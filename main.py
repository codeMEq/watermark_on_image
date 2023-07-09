from tkinter import Tk, Button, Label
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(image_path, watermark_text):
    # Open the image
    image = Image.open(image_path)

    # Create a transparent layer for the watermark
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Set the font, size, and color of the watermark text
    font = ImageFont.truetype(r"C:\Users\reech\Downloads\arial\arial.ttf", size=50)
    text_color = (255, 255, 255)  # White

    # Create a drawing object for the watermark
    draw = ImageDraw.Draw(watermark)

    # Get the bounding box of the watermark text
    bbox = draw.textbbox((0, 0), watermark_text, font=font)

    # Extract the width and height from the bounding box
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate the position to place the watermark
    x = image.width - text_width - 10
    y = image.height - text_height - 10

    # Draw the watermark text on the transparent layer
    draw.text((x, y), watermark_text, font=font, fill=text_color)

    # Combine the original image and the watermark
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

    # Save the watermarked image
    watermarked_image_path = r"C:\Users\reech\watermarked_image.png"
    watermarked_image.save(watermarked_image_path)

    # Open the watermarked image using the default image viewer
    os.startfile(watermarked_image_path)

def upload_image():
    # Open a file dialog to select an image file
    file_path = askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    # Add a watermark to the selected image
    if file_path:
        watermark_text = "Happiness Dude"
        add_watermark(file_path, watermark_text)
        status_label.configure(text="Watermark added successfully.")

# Create the main window
window = Tk()

# Create and configure the upload button
upload_button = Button(window, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Create a label to display status
status_label = Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()
