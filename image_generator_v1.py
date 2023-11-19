from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def generate_card_with_art_and_text(image_url, card_name, card_text, output_path='output_card.png'):
    # Download the image from the provided URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Set font parameters
    font_path = "fontpath.TTF"  # Replace with the path to a TTF font file
    font_size = 60
    font = ImageFont.truetype(font_path, font_size)

    # Set text position
    text_position_name = (10, 10)
    text_position_body = (10, 800)

    # Add text to the image
    draw.text(text_position_name, card_name, font=font, fill="white")
    draw.text(text_position_body, card_text, font=font, fill="white")

    # Save the combined image with text
    image.save(output_path)

    print(f"Combined image saved at: {output_path}")

# Example usage:
card_name = "Fire Guy"
image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-0WxqUe5jPU7LvfjuLUnB5qlb/user-ux7KFwhjWeqHleMkDLmGO3qt/img-CnFBskpHqlsnfC32a2KxGrXH.png?st=2023-11-19T20%3A02%3A07Z&se=2023-11-19T22%3A02%3A07Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-19T20%3A10%3A38Z&ske=2023-11-20T20%3A10%3A38Z&sks=b&skv=2021-08-06&sig=gqrZ2IWKaW2lQNK7gvr%2Bw4b9eAscsZxSBW7pl5TP8Rc%3D"  # Replace with the actual DALL·E image URL
card_text = "Fire guy do fire thing"

generate_card_with_art_and_text(image_url, card_name, card_text)
