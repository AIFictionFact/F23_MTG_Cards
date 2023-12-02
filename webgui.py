import PySimpleGUIWeb as sg
import csv  
from mtg_card_generator import generate_magic_card_name, generate_magic_card
import numpy
import random
import textwrap
# rating is the rating given to the card
# card_info is the list of features applied to the card
# hist is a list of cards drafted prior to this draft
# draft num is the number of drafts currently made
def store_rating(rating,card_info,filename,draft_num,hist):

    # number of zero values to pad the data
    zeroes = 9 - draft_num

    rnn_sample = []

    for i in range(zeroes):
        rnn_sample.append([0 for element in range(len(card_info) + 1)])

    for card in hist:
        rnn_sample.append(card)

    card_info.append(rating)
    rnn_sample.append(card_info)

    # rnn_sample now contains a zero padded list of draft history and the latest drafted card
    # something like this:
    #   feature x, feature y, feature z,  rating
    #   [0,0,0,0] # zero pad
    #   [0,0,0,0] # zero pad
    #   [0,0,0,0] # zero pad
    #   [0,0,0,0] # zero pad
    #   [1,2,3,2] # draft 1
    #   [4,1,4,4] # draft 2
    #   [3,9,2,3] # draft 3
    #   [8,2,8,1] # draft 4
    #   [6,7,8,2] # draft 5
    #   [5,4,5,4] # target variable (draft 6)
    # always a length of ten and a width of feature space + target variable
    # add all these rows to represent a sequence.

    with open(filename, 'a') as csvfile:  
        csvwriter = csv.writer(csvfile)   
        csvwriter.writerows(rnn_sample) 

    # add selected card to draft history and return
    hist.append(card_info)
    return hist

#display window for rating a card
#displays chosen card with rating buttond 1 through 5
#once a button is pressed store the rating and card info in a csv then go back to draft window or field card window
#or go to the end window if the draft or field card addition is completed
def rating_window(card_image,card_info,filename,draft_num,hist):
    
    #layout = [[sg.Image(card_image),sg.Text("How would you rate this card? [1 = terrible, 5 = perfect]"),],[sg.Button("1",size=(23,1)),sg.Button("2",size=(23,1)),sg.Button("3",size=(23,1)),sg.Button("4",size=(23,1)),sg.Button("5",size=(23,1))]]

    layout = [[sg.Text(card_image,size=(25, None)),sg.Text("How would you rate this card? [1 = terrible, 5 = perfect]"),],[sg.Button("1",size=(23,1)),sg.Button("2",size=(23,1)),sg.Button("3",size=(23,1)),sg.Button("4",size=(23,1)),sg.Button("5",size=(23,1))]]

    
    # layout = [[sg.Column(layout_column, element_justification='center')]]
    window = sg.Window("Rate card", layout)
    while True:
        event, values = window.read()
        if isinstance(event,str):
            hist = store_rating(int(event),card_info,filename,draft_num,hist)   
        break
        
    
    
    return hist

#display window for drafting card 
#displays 10 cards an buttons to draft each card
#once a button is clicked transitions to the the rating window
def draft_window(images,card_details,draft_num,hist):
    # images1 = [sg.Text(" "),sg.Text(" "),sg.Image(images[0],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[1],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[2],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[3],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[4],size=(200, None))]
    # images2 = [sg.Text(" "),sg.Text(" "),sg.Image(images[5],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[6],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[7],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[8],size=(200, None)),sg.Text(" "),sg.Text(" "),sg.Text(" "),sg.Image(images[9],size=(200, None))]
    
    images1 = [sg.Text(images[0],size=(25, None)),sg.Text(images[1],size=(25, None)),sg.Text(images[2],size=(25, None)),sg.Text(images[3],size=(25, None)),sg.Text(images[4],size=(25, None))]
    images2 = [sg.Text(images[5],size=(25, None)),sg.Text(images[6],size=(25, None)),sg.Text(images[7],size=(25, None)),sg.Text(images[8],size=(25, None)),sg.Text(images[9],size=(25, None))]
    buttons1 = [sg.Button("Draft First Card?",size=(23,1)),sg.Button("Draft Second Card?",size=(23,1)),sg.Button("Draft Third Card?",size=(23,1)),sg.Button("Draft Fourth Card?",size=(23,1)),sg.Button("Draft Fifth Card?",size=(23,1))]
    buttons2 = [sg.Button("Draft Sixith Card?",size=(23,1)),sg.Button("Draft Seventh Card?",size=(23,1)),sg.Button("Draft Eighth Card?",size=(23,1)),sg.Button("Draft Ninth Card?",size=(23,1)),sg.Button("Draft Tenth Card?",size=(23,1))]
    layout = [images1, buttons1,images2,buttons2]
    window = sg.Window("Draft cards", layout)
    while True:
        event, values = window.read()
        if event == "Draft First Card?":
            card = 0
        elif event == "Draft Second Card?":
            card = 1
        elif event == "Draft Third Card?":
            card = 2
        elif event == "Draft Fourth Card?":
            card = 3
        elif event == "Draft Fifth Card?":
            card = 4
        elif event == "Draft Sixith Card?":
            card = 5
        elif event == "Draft Seventh Card?":
            card = 6
        elif event == "Draft Eighth Card?":
            card = 7
        elif event == "Draft Ninth Card?":
            card = 8
        elif event == "Draft Tenth Card?":
            card = 9
            
        
        hist = rating_window(images[card],card_details[card],"ratings.csv",draft_num,hist)
        break

    return hist

#displays after a draft or field card addtion is completed 
#gives the user the option to go back to the main window or quit the program
def ending_window():
    layout = [[sg.Text("Done!")],[sg.Text("go back?")], [sg.Button("Yes")]]

    # Create the window
    window = sg.Window("MTG drafter", layout)

    # Create an event loop
    while True:
        event, values = window.read()

        if event == "Yes" or event == sg.WIN_CLOSED:
            
            break
        elif event == "No":
            
            main_window()
    
#display a single card
#then give the user the option to display another card
#or exit to the end window
#once the player has chosen display the rating window then take them
#to the window of their choice (field card window or ending window)
def field_card_window():
    # get info from model
    card_details = generate_random_card_features()
    # get cards using the info from the model
    name = generate_magic_card_name(card_details)
    card_text = generate_magic_card(name, card_details)
    
    # turn card text into image!!!!

    image = 'card.png'
    filename = "field_card.csv"
    #layout = [ [sg.Image(image)], [sg.Button("Next Card")],[sg.Button("Finish")]]
    layout = [ [sg.Text(image,size=(25, None))], [sg.Button("Next Card")],[sg.Button("Finish")]]
    window = sg.Window("MTG drafter", layout)

    while True:
        event, values = window.read()
        if event == "Next Card":
            
            rating_window(image,card_details,filename)
            field_card_window()
            break
        elif event == "Finish" or event == sg.WIN_CLOSED:
             
             rating_window(image,card_details,filename)
             ending_window()
             break


#give the player the option to either, start a draft, add a field card, or quit the program
def main_window():

    layout = [[sg.Text("Want to get drafting?")], [sg.Button("Start draft")],
              [sg.Text("Want to add a card to the field?")], [sg.Button("Add card")]
              ]

    window = sg.Window("MTG drafter", layout)

    contine = True
    while True:
        event, values = window.read()
        if event == "Start draft":
            
            hist = []
            for i in range(10):
                
                images = []
                card_detail_list = []
                for j in range(10): # MAKE 10 CARDS
                    # get info from model
                    card_details = generate_random_card_features()
                    # get cards using the info from the model
                    name = generate_magic_card_name(card_details)
                    card_text = generate_magic_card(name, card_details)

                    # card_text EXAMPLE: ["\n3 Red\n2 Colorless", "\n Creature", "\nMana Wurm\nWhenever you cast a spell, put a +1/+1 counter on Mana Wurm."]
                    # turn card_text into text!!!! <-------------------------------

                    card_detail_list.append(card_details)
                    images.append(card_text)

                hist = draft_window(images,card_detail_list,i,hist)
            ending_window()
            break
        elif event == "Exit" or event == sg.WIN_CLOSED:
             
             break
        elif event == "Add card":
            
            field_card_window()
            break

# generates a feature space based on distribution curves
def generate_random_card_features():

    features = []
    # card colors 0 thru 5
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])) # red
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])) # blue
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])) # green
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])) # white
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])) # black
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])) # colorless

    while(sum(features) == 0):                                                                         # keep going until a mana is shown
        features[0] = numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])
        features[1] = numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])
        features[2] = numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])
        features[3] = numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])
        features[4] = numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])
        features[5] = numpy.random.choice(numpy.arange(0, 6), p=[0.95, 0.02, 0.015, 0.01, 0.003, 0.002])

    # card type
    features.append(numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05])) # 5 percent chance its multitype
    features.append(numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05]))
    features.append(numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05]))
    features.append(numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05])) 
    features.append(numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05])) 
    
    type = numpy.random.choice(numpy.arange(0, 5), p=[0.2, 0.2, 0.2, 0.2, 0.2]) # which primary type?
    if type == 0:
        features[6] = 1 # creature
    elif type == 1:
        features[7] = 1 # instant
    elif type == 2:
        features[8] = 1 # sorcery
    elif type == 3:
        features[9] = 1 # artifact
    elif type == 4:
        features[10] = 1 # enchantment
    
    # specialization 
    features.append(random.uniform(0, 1)) 
    
    return features
        
main_window()



