import numpy as np

def rock_paper_scissors():
    hand = ["Rock","Paper","Scissors"]
    hand = np.array(hand).reshape(1,np.array(hand).shape[0])

    order = np.random.permutation(hand.shape[1])
    hand = hand[:,order]
    return hand[0,0]

