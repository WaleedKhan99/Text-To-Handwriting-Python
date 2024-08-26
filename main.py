# 1st Method

from PIL import Image, ImageDraw, ImageFont

def text_to_handwritten(text, output_path, font_size=36):
    width, height = 800, 400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    
    # font Path and Styles
    font_path = ImageFont.truetype("C:/Users/Waleed/AppData/Local/Microsoft/Windows/Fonts/Dpdorkdiary-P267.ttf", font_size)
    # font_path = "C:/Users/Waleed/AppData/Local/Microsoft/Windows/Fonts/Rumi-Regular.ttf"
    
    
    
    font = ImageFont.truetype(font_path, font_size)
    
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill="black", font=font)
    image.save(output_path, "PNG")

if __name__ == "__main__":
    input_text = "Waleed Ahmed Khan!"
    output_file = "handwritten.png"
    
    text_to_handwritten(input_text, output_file)
    print(f"Handwritten image saved as '{output_file}'")



# # # =============================================================
# 2nd Method

# from PIL import Image, ImageDraw, ImageFont

# def create_handwritten_image(text, output_path):
#     width, height = 600, 600  # Set the dimensions of the image
#     bg_color = (255, 255, 255)  # Background color (white)
#     text_color = (10, 10, 10)      # Text color (black)

#     # Create a new image with the specified dimensions and background color
#     image = Image.new("RGB", (width, height), bg_color)
#     draw = ImageDraw.Draw(image)

#     # Load a handwriting-like font (you can provide the path to a font file)
#     font = ImageFont.load_default()

#     # Define the position and size of the text
#     x, y = 50, 50
#     font_size = 44

#     # Draw the text on the image
#     draw.text((x, y), text, font=font, fill=text_color)

#     # Save the image to the specified output path
#     image.save(output_path)

# # Call the function to create the handwritten-style image
# text = """Python is a general-purpose, interpreted, high-level programming language 
# popularly used for website development, data analytics and automation. Python is a 
# general-purpose language which means it is versatile and can be used to program many 
# different types of functions."""


# output_path = "Handwritten.png"

# create_handwritten_image(text, output_path)
# print("Handwriting image created successfully.")

# # # =============================================================
# 3rd Method

# import pywhatkit as pw

# pw.text_to_handwriting("Waleed Ahmed khan","Handwritten.png",[10,10,10])
# print("Done")


