def is_three_of_a_kind(dice):

    unique = list(set(dice))

    for i in unique:
        if dice.count(i) == 3:
            return True

    return False

def is_four_of_a_kind(dice):

    for i in unique:
        if dice.count(i) == 4:
            return True

    return False

def is_full_house(dice):

    unique = list(set(dice))

    if len(unique) == 2:
        if (dice.count(unique[0]) == 2 and dice.count(unique[1]) == 3) or \
            (dice.count(unique[0]) == 3 and dice.count(unique[1]) == 2):
                return True        
    
    return False

def is_small_straight(dice):
    dice_sorted = sorted(dice)
    count = 0
    for i in range(0, len(dice) - 1):
        if dice_sorted[i + 1] == dice_sorted[i] + 1:
            count += 1

    if count == 3:
        return True
    else:
        return False

def is_large_straight(dice):

    dice_sorted = sorted(dice)
    count = 0
    for i in range(0, len(dice) - 1):
        if dice_sorted[i + 1] == dice_sorted[i] + 1:
            count += 1

    if count == 4:
        return True
    else:
        return False 
        

def is_yahtzee(dice):
    if dice.count(dice[1]) == 5:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_full_house([1,1,1,2,2]))
    print(is_full_house([1,3,1,2,2]))

    print(is_yahtzee([1,1,1,1,1]))
    print(is_yahtzee([1,3,1,2,2]))

    print(is_large_straight([1,2,3,4,5]))
    print(is_large_straight([1,1,3,4,5]))

    print(is_small_straight([1,2,3,4,6]))
    print(is_small_straight([6,1,2,3,4]))
    print(is_small_straight([1,1,1,4,5]))
    print(is_small_straight([1,1,6,4,5]))
    
