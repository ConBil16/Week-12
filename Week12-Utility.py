# https://github.com/ConBil16/Week-12.git
# Connor Bilgrave
# CSCI 102 - Section E
# Week 12 - Part B

def PrintOutput(Word):
    print('OUTPUT', Word)


def LoadFile(x):
    with open(x, 'r') as file:
        read_file = file.read().splitline()
        print('Output', read_file)

def UpdateString(word, letter, number):
    num = int(number)
    new_word = word.replace(word[num], letter, 1)
    print(new_word)

def FindWordCount(x, y):
    for word in x:
        count = 0
        if x == y:
            count += 1
    return count

def ScoreFinder(players, scores, name):
    players_lower = [item.lower() for item in players]
    name_lower = name.lower()
    
    if name_lower in players_lower:
        player_number = players_lower.index(name_lower)
        score = scores[player_number]
        print('OUTPUT', players[player_number], 'got a score of', score)

    else:
        print('OUTPUT player not found')


def Union(scores, player2):
    combination = scores + player2
    return combination
    #Should I print this here or have the user put in the print function

def Intersection(x, y):
    inner = set(x)&set(y)
    return inner

def NotIn(list_1, list_2):
    empty = []
    for i in list_1:
        if i not in list_2:
            empty.append(i)
    return empty 
    


        
        

