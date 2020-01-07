import random

def roll_all(dice):

    random.seed()

    for i in range(0,len(dice)):
        dice[i] = random.randint(1,6)

def roll_selected(dice, to_roll):

    random.seed()

    for selected in to_roll:
        dice[selected - 1] = random.randint(1,6)

if __name__ == "__main__":

    d = [0 for i in range(0,5)]
    roll_all(d)
    print(d)
