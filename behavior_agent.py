import numpy
import random
import csv

# Stores draft history into a csv
def store_rating_autogen(card_info,filename,draft_num,hist,choice):

    # number of zero values to pad the data
    zeroes = 9 - draft_num

    if(draft_num == choice):
        rnn_sample = []

        for i in range(zeroes):
            rnn_sample.append([0 for element in range(len(card_info))])

        for card in hist:
            rnn_sample.append(card)

        rnn_sample.append(card_info)

            # rnn_sample now contains a zero padded list of draft history and the latest drafted card
            # something like this:
            #   feature x, feature y, feature z
            #   [0,0,0] # zero pad
            #   [0,0,0] # zero pad
            #   [0,0,0] # zero pad
            #   [0,0,0] # zero pad
            #   [1,2,3] # draft 1
            #   [4,1,4] # draft 2
            #   [3,9,2] # draft 3
            #   [8,2,8] # draft 4
            #   [6,7,8] # draft 5
            #   [5,4,5] # target variable (draft 6)
            # always a length of ten and a width of feature space
            # add all these rows to represent a sequence.

        with open(filename, 'a') as csvfile:  
            csvwriter = csv.writer(csvfile)   
            csvwriter.writerows(rnn_sample) 

    # add selected card to draft history and return
    hist.append(card_info)
    return hist

# Gathers statistics from history
def get_stats_hist(hist):
    
    hist_data = [0 for element in range(12)]

    for drafted in hist:
        for i in range(len(drafted)):
            hist_data[i] += drafted[i]

    return hist_data

# Algorithm to choose a card from the list of cards
def select_card(card_list,hist):
    
    score = [0 for element in range(len(card_list))]
    
    hist_data = get_stats_hist(hist)

    tot_mana = 1
    tot_types = 1
    for i in range(len(hist_data)):
        if(i < 6):
            tot_mana += hist_data[i]
        elif(i < 10):
            tot_types += hist_data[i]

    for j in range(len(card_list)):

        for i in range(len(card_list[j])):
            
            if(i < 5):
                score[j] += 4 * tot_mana * (hist_data[i] / tot_mana) * card_list[j][i]
            elif(i == 5):
                score[j] += 0
            elif(i < 11):
                score[j] -= tot_types * (hist_data[i] / tot_types) * card_list[j][i]
            else:
                if(hist_data[i] < 1.5):
                    score[j] += card_list[j][i] # 40
                elif(hist_data[i] > 3.5):
                    score[j] -= card_list[j][i]
                else:
                    score[j] -= abs(0.5 - card_list[j][i])

    return score.index(max(score))

# Draft card and store in history
def draft(card_list,draft_num,hist,choice):

    card = select_card(card_list,hist)
    
    hist = store_rating_autogen(card_list[card],"testing.csv",draft_num,hist,choice)

    return hist

def main_window():

    # get random number. this will be the point in the draft saved to csv
    choice = numpy.random.randint(0, 10)

    hist = []
    for i in range(10):
        
        
        card_list = []
        for j in range(10): # MAKE 10 CARDS
            # get info from model
            card_details = generate_random_card_features()

            card_list.append(card_details)

        hist = draft(card_list,i,hist,choice)

# generates a feature space based on distribution curves
def generate_random_card_features():

    features = []
    # card colors 0 thru 5
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])) # red
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])) # blue
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])) # green
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])) # white
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])) # black
    features.append(numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])) # colorless

    while(sum(features) == 0):                                                                         # keep going until a mana is shown
        features[0] = numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])
        features[1] = numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])
        features[2] = numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])
        features[3] = numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])
        features[4] = numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])
        features[5] = numpy.random.choice(numpy.arange(0, 6), p=[0.90, 0.07, 0.025, 0.0025, 0.0015, 0.001])

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

for i in range(100000):
    main_window()