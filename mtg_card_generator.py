import openai

# Set API key
openai.api_key = 'api_key'

def generate_magic_card_name(card_type, color_identity, mana_value, specialization):
    # Define a prompt
    prompt = f"Create only the name of a new Magic: The Gathering card that has the following attributes:\n\nType: {card_type}\nColor Identity: {color_identity}\nMana Value: {mana_value}"

    # Generate card text using the GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,  # Adjust card text length
        temperature=0.7,  # Adjust randomness
        n=1  # Number of cards
    )

    # Extract card text
    card_text = response.choices[0].text.strip()

    # Print
    print(card_text)
    return card_text


def generate_magic_card(card_name, card_type, color_identity, mana_value, specialization):
    # Define a prompt
    prompt = f"Create the abilities of a new Magic: The Gathering card named {card_name} that has the following attributes:\n\nType: {card_type}\nColor Identity: {color_identity}\nMana Value: {mana_value}\nSpecialization: {specialization}\n\nCard Text:"

    # Generate card text using the GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,  # Adjust card text length
        temperature=0.7,  # Adjust randomness
        n=1  # Number of cards
    )

    # Extract card text
    card_text = response.choices[0].text.strip()

    # Print
    print(card_text)


def generate_card_art(card_name):

    # Construct a prompt for DALL·E
    desc = f"Create art for a Magic: The Gathering card named '{card_name}'."

    response = openai.Image.create(
        model="dall-e-2",
        prompt=desc,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url

    print(f"Card Art for '{card_name}': {image_url}")


# Exaple usage
name = generate_magic_card_name("Creature", "Red", "3", "Aggressive")
generate_magic_card(name, "Creature", "Red", "3", "Aggressive")
generate_card_art(name)
