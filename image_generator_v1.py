from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap

def generate_card_with_art_and_text(image_url, card_name, card_type, card_cost, card_text, output_path='output_card.png'):
    # Download the image from the provided URL
    response = requests.get(image_url)
    original_image = Image.open(BytesIO(response.content))

    # Set the desired dimensions for the card
    new_width = 1024
    new_height = 1428

    # Create a new image with the desired dimensions and a black background
    new_image = Image.new("RGB", (new_width, new_height), "black")
    draw = ImageDraw.Draw(new_image)

    make_pic = 1
    # Create a drawing object for the new image
    if (make_pic!=0):
        response = requests.get(image_url)
        original_image = Image.open(BytesIO(response.content))

        new_image.paste(original_image, (0, 0))
        # print("adding image")


    overlay_image = Image.open("card_overlay.png")
    new_image.paste(overlay_image, (0, 0), overlay_image)


    # Set font parameters
    font_path = "path\\MAGIC.TTF"  # Replace with the path to a TTF font file
    font_size = 50
    font2_size = 60
    font = ImageFont.truetype(font_path, font_size)
    font2 = ImageFont.truetype(font_path, font2_size)

    body_path = "path\\Mplantin.ttf"  # Replace with the path to a TTF font file
    body_size = 40
    body_font = ImageFont.truetype(body_path, body_size)

    # Set text position
    text_position_name = (65, 45)
    text_position_type = (65, 784)
    text_position_cost = (1024-65-42*len(card_cost), 42)

    # Add text to the image
    draw.text(text_position_name, card_name, font=font, fill="white")
    draw.text(text_position_type, card_type, font=font, fill="white")
    draw.text(text_position_cost, card_cost, font=font2, fill="white")

    # Add the body text wrapped
    # max_text_width = new_width - text_position[0] - 10
    wrapped_text = textwrap.fill(card_text, width=35)  # Adjust the width as needed
    rulestext_position = (130, 859)
    line_spacing = 1.1

    # Add wrapped text to the new image
    for line in wrapped_text.split('\n'):
        draw.text(rulestext_position, line, font=body_font, fill="black")
        # Increase the vertical position for the next line based on line spacing
        rulestext_position = (rulestext_position[0], rulestext_position[1] + int(font_size * line_spacing))

    # Save the combined image with text
    new_image.save(output_path)

    print(f"Combined image saved at: {output_path}")

# Example usage:
card_name = "Flametongue Kavu"
card_type = "Creature"
image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-0WxqUe5jPU7LvfjuLUnB5qlb/user-ux7KFwhjWeqHleMkDLmGO3qt/img-NlYVa0VrHQ6O7qWGfqi8B2aK.png?st=2023-12-01T20%3A22%3A06Z&se=2023-12-01T22%3A22%3A06Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-12-01T03%3A32%3A24Z&ske=2023-12-02T03%3A32%3A24Z&sks=b&skv=2021-08-06&sig=lqXQtMMfvxG4%2BYmnW9e6oR7aDxDcFkjimuBwuz7T4mg%3D"  # Replace with the actual DALL·E image URL
card_text = "Flametongue Kavu deals 4 damage to target creature.\n\nWhen Flametongue Kavu enters the battlefield, target creature gets +2/+2 until end of turn."
card_cost = "<["

generate_card_with_art_and_text(image_url, card_name, card_type, card_cost, card_text)
