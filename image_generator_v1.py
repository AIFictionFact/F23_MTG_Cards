from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap

def generate_card_png(image_url, card_name, card_type, card_text, make_pic, output_path='output_card.png'):
    # Download the image from the provided URL
    response = requests.get(image_url)
    original_image = Image.open(BytesIO(response.content))

    # Set the desired dimensions for the card
    new_width = 1024
    new_height = 1434

    # Create a new image with the desired dimensions and a black background
    new_image = Image.new("RGB", (new_width, new_height), "black")
    draw = ImageDraw.Draw(new_image)

    # Create a drawing object for the new image
    if (make_pic!=0):
        response = requests.get(image_url)
        original_image = Image.open(BytesIO(response.content))
        new_image.paste(original_image, (0, 0))
    else:
        art_position = (0, 0, 1024, 1024)  # (left, top, right, bottom)
        fill_color = (100, 100, 100)  # RGB values for tan color
        draw.rectangle(art_position, fill=fill_color)
        
    # draw = ImageDraw.Draw(new_image)
    # Draw rectangle for borders
    title_position = (0, 0, 1024, 124)  # (left, top, right, bottom)
    text_position = (0, 924, 1024, 1024)  # (left, top, right, bottom)
    bkg_color = (0, 0, 0)  # RGB values for tan color
    draw.rectangle(title_position, fill=bkg_color)
    draw.rectangle(text_position, fill=bkg_color)


    # Set font parameters
    font_path = "path//MAGIC.TFF"  # Replace with the path to a TTF font file
    font_size = 60
    font = ImageFont.truetype(font_path, font_size)

    # Set text position
    text_position_name = (10, 20)
    text_position_type = (10, 944)

    # Add text to the image
    draw.text(text_position_name, card_name, font=font, fill="white")
    draw.text(text_position_type, card_type, font=font, fill="white")

    # Add the body text wrapped
    max_text_width = new_width - text_position[0] - 10
    wrapped_text = textwrap.fill(card_text, width=38)  # Adjust the width as needed

    # Add wrapped text to the new image
    text_position_text = (10, 1044)
    draw.text(text_position_text, wrapped_text, font=font, fill="white")

    # Save the combined image with text
    new_image.save(output_path)

    print(f"Combined image saved at: {output_path}")

# Example usage:
card_name = "Fire Guy"
card_type = "Creature"
image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-0WxqUe5jPU7LvfjuLUnB5qlb/user-ux7KFwhjWeqHleMkDLmGO3qt/img-XrIob4af6m33wJmZbp9XJY8e.png?st=2023-11-27T18%3A41%3A16Z&se=2023-11-27T20%3A41%3A16Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-27T12%3A32%3A03Z&ske=2023-11-28T12%3A32%3A03Z&sks=b&skv=2021-08-06&sig=BlqYls3PUmUW3V1ygigDqfnlByrOgxe10F9eNrNK158%3D"  # Replace with the actual DALL·E image URL
card_text = "Mountain Drake enters the battlefield with two +1/+1 counters on it. Whenever Mountain Drake deals combat damage to a player, you may pay {R}. If you do, Mountain Drake deals 3 damage to any target."
include_pic = 1 # change to 0 to remove art from card

generate_card_png(image_url, card_name, card_type, card_text, include_pic)
