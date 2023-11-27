import PySimpleGUI as sg
import csv  

def store_rating(rating,card_info,filename):

    
    with open(filename, 'a') as csvfile:  
        csvwriter = csv.writer(csvfile)   
        csvwriter.writerows([[rating]+card_info]) 



def rating_window(card_image,card_info,filename):
    
    layout = [[sg.Image(card_image),sg.Text("How would you rate this card?"),],[sg.Button("1",size=(23,1)),sg.Button("2",size=(23,1)),sg.Button("3",size=(23,1)),sg.Button("4",size=(23,1)),sg.Button("5",size=(23,1))]]

    
    # layout = [[sg.Column(layout_column, element_justification='center')]]
    window = sg.Window("Rate card", layout)
    while True:
        event, values = window.read()
        if isinstance(event,str):
            store_rating(int(event),card_info,filename)   
        break
        
    window.close()
    
def draft_window(images,card_details):
    images1 = [sg.Image(images[0]),sg.Image(images[1]),sg.Image(images[2]),sg.Image(images[3]),sg.Image(images[4])]
    images2 = [sg.Image(images[5]),sg.Image(images[6]),sg.Image(images[7]),sg.Image(images[8]),sg.Image(images[9])]
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
            
        window.close()
        rating_window(images[card],card_details[card],"ratings.csv")
        break

    return True


def ending_window():
    layout = [[sg.Text("Done!")],[sg.Text("Exit?")], [sg.Button("Yes")], [sg.Button("No")]]

    # Create the window
    window = sg.Window("MTG drafter", layout)

    # Create an event loop
    while True:
        event, values = window.read()

        if event == "Yes" or event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "No":
            window.close()
            main_window()
    

def field_card_window():
    #get info from model
    #card_details = get_card_featrures(1)
    #get cards using the info from the model
    #image = get_cards(card_details,1)
    image = 'card.png'
    card_info = ["blah"]
    filename = "field_card.csv"
    layout = [ [sg.Image(image)], [sg.Button("Next Card")],[sg.Button("Finish")]]

    window = sg.Window("MTG drafter", layout)

    while True:
        event, values = window.read()
        if event == "Next Card":
            window.close()
            rating_window(image,card_info,filename)
            field_card_window()
            break
        elif event == "Finish" or event == sg.WIN_CLOSED:
             window.close()
             rating_window(image,card_info,filename)
             ending_window()
             break



def main_window():

    layout = [[sg.Text("Want to get drafting?")], [sg.Button("Start draft")],
              [sg.Text("Want to add a card to the field?")], [sg.Button("Add card")],
               [sg.Text("Want to leave?")], [sg.Button("Exit")]
              ]

    window = sg.Window("MTG drafter", layout)

    contine = True
    while True:
        event, values = window.read()
        if event == "Start draft":
            window.close()
            images = ['card.png','card.png','card.png','card.png','card.png','card.png','card.png','card.png','card.png','card.png']
            card_details = [["blah"],["blah"],["blah"],["blah"],["blah"],["blah"],["blah"],["blah"],["blah"],["blah"]]
            for i in range(10):
                #get info from model
                #card_details = get_card_featrures()
                #get cards using the info from the model
                #images = get_cards(card_details)
                draft_window(images,card_details)
            ending_window()
            break
        elif event == "Exit" or event == sg.WIN_CLOSED:
             window.close()
             break
        elif event == "Add card":
            window.close()
            field_card_window()
            break

    
    
    
    
        
main_window()



