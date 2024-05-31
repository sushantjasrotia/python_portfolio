import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


class WatermarkApp:
    """A simple desktop application to upload images and add a watermark."""

    def __init__(self, root):
        """Initialize the application."""
        self.photo = None
        self.root = root
        self.root.title("Image Watermarking Desktop App")

        # Create a canvas to display the image
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Button to upload image
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        # Button to add watermark
        self.watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()

        # Initialize image and watermark text
        self.image = None
        self.watermark_text = "Hi Watermark :)"

    def upload_image(self):
        """Open a file dialog to select an image file and display it on the canvas."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((400, 300))  # Resize image to fit canvas
            self.render_image()

    def render_image(self):
        """Render the uploaded image on the canvas."""
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(200, 150, image=self.photo)

    def add_watermark(self):
        """Add a watermark to the image."""
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype("arial.ttf", 40)  # Use arial font with size 40
            # Draw the watermark text at position (50, 50) with white color and semi-transparent
            draw.text((50, 50), self.watermark_text, fill=(255, 255, 255, 128), font=font)
            self.render_image()


root = tk.Tk()
app = WatermarkApp(root)
root.mainloop()