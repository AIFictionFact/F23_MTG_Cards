
# **Title** 
## MTG Cards
	Michael Lenyszyn: Lenysm
	Eric Rodriguez: Rodrie10
	Ethan Cruz: Cruze6
#
#   **Project Overview**: 
-   To use AI to create original cards which would adhere to the format of a standard MTG card
-   Create a new draft and gamemode
	- Will have a malicious AI introduce cards to the battlefield
-   AI will generate a set of cards from players to choose from.
	- This continues until all players have a complete deck.
-   AI will learn what additions make the game more fun.
-   This feedback allows the card creation AI to create more balanced cards.
#
#   **Related AI Projects:** 
## Current Tech
- GPT 3.5 - will be used to generate card flavor text, abilities, and stats
- DALL·E - Will be used to generate art for the cards
## Methodologies
- Supervised Learning - The AI will learn what cards bring the most entertainment to the players, adjusting it’s model after games
- Recommender Systems - Netflix & Youtube’s algorithms for recommending videos can be used to generate cards for draft. Draft cards compete to be selected over each other
#
#   **Functional Requirements:** 
-   AI will interact with humans by creating ten MTG cards for each draft turn.
-   The AI will control parameters such as the card’s mana cost, card type, mana colors, etc. And send a prompt to GPT-3 to develop the card
-   The AI’s input features will be the draft history (currently drafted cards’ mana costs, colors, etc)
-   The Human will have 10 cards to choose from, the card which is selected is given a positive value, while the cards not selected are given a negative or zero value.
-   Over hundreds of drafts, the AI will learn which card parameters lead to being drafted more often based on the user’s draft history
#
#   **Non-functional Requirements:**
## Performance Criteria
- Being selected in draft or not (did the user pick your card during draft or not?)
- Drafted cards rating (How would you rate the cards you drafted?)
## Usability
-   Functional & Simple to use user interface
-   Quick development & visualization of cards between draft rounds
## Reliability
-   Consistent & Coherent cards developed from GPT & Dall-E prompting
#
#   **System Architecture:**
-   Create cards in the format of an MTG card
-   Including all criteria seen in diagram
-   Take data from preexisting MTG cards to generate info
-   Receive user feedback

    **![](https://lh7-us.googleusercontent.com/sIyFAbFDnPci6tLaialQfuwvHt_ftPcZj1fP6h7zMVCDzoVyXHgYiTXWp5N5NlilqOBvIWDYikzMLfpc4Mo9URPtT_gk9RlekxLhhvakT4YoWpqkzY-N6864_ce-5yM7wB59_BaPsSKZptlMtbhFwzguTw=s2048)**
#
-   Through which card they choose
#  **Technologies to be Used:** 
##   Python
**![](https://lh7-us.googleusercontent.com/eLjnsKn2sJhaBXtzqoWANwzxQlVZXzjRkZtG3kRDHbJhl4TIFYolPASXq2Eg-74UtGu13v0pSt7hFDbu_NuWgmGjPUj4jp2y2tbZES72Q7Ga5J0uVUlJONK5VUdnMgmdkwCsSs7UXYVTbyFMZVU5bgx8fA=s2048)**
## ChatGPT
**![](https://lh7-us.googleusercontent.com/SYMvz7xdJJc9K6ZwdabUFtBIEiEMfA-Z64DqLvLFiktv_zesSOnpam-6wZsMpxFeWWHCfFolE-NlQicHp8DnxKE_7tZDrmxeRm2xREMq33PKtz5nOIm5sZ4ME0v7XpMrOgb9UhJN8eG_7ZXnESatrWSPOA=s2048)**
## DALL·E 2
**![](https://lh7-us.googleusercontent.com/xamkLCOSs7TVpxCq05omegmQdK-VmJ1ZQbYnoE6gAyAvWvHujnEo8QduiRM9L_8i7rapIUKK1tSkysyAXopRQSQdJUAIxqE4c3AgQUxR0u59HraHAgIrTRq2l62wL63_8CERSWeEP1esThbOxDFJeBq8pg=s2048)**
##
#  **User Profiles:**
-   MTG players may use this tool for a fun and unique MTG experience.
-   Provides an interesting alternative to physical drafting at a greatly reduced cost
#
#   **User Interface (UI)/User Experience (UX) Design:** 
-   Begin with starting button “start draft?”
-   Clicking the button will display 10 cards
-   The cards will have associated buttons
-   clicking the button will draft the card
-   Once a card is chosen, a new set of 10 will be displayed
-   Continues until 20 cards are drafted
-  Ends with ending screen “draft done!”
    **![](https://lh7-us.googleusercontent.com/1L0WL8FGfb-9vWCrQd9naFasHdZMPpKsdhJOlo3xFNwUxYPqeyRc2a3v9Dwng-azTXiUqoSiJwTVjr3sd_RDX2vDRETcWxo5O9aDdF4ILdjgegsHXmbiFGBs3lYJEl_WQ4sF1VS29gIYOVMWD3SMTWfy8w=s2048)**
-   Repeats from there
#
#   **Team Roles and Responsibilities:** 
##  Michael:
-   User interface design
##  Eric:
-   Card generation through GPT and Dalle
##   Ethan:
-   Recommender System Modelling
#
#   **Technical Limitations:**
## Limit on feature space 
- MTG cards can have numerous and complex abilities that would be difficult to describe in our model so we will likely have to leave out the cards’ abilities from the features we consider
## Limit on drafts made
- Lack of drafts will decrease number of datapoints to train the model off of. Depends on how many games the group plays during training phase

## How to Guide

#Step 1
#
make sure you have python 3 and have installed the packages listed in "requirements.txt"
#Step 2
edit "mtg_card_generator.py" and put your openai api key at the top of the file in place of 'insert_key_here'
#
#Step 3
simply run `python gui.py`


