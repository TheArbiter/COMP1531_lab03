"""This function returns a new list that is created by shuffling the elements of the
provided list
:param li: The list to be shuffled
:return shuffled_list: The shuffled list
"""

#Step 1: import the random function, so we can randomly shuffle the list
#Step 2: input into list
#Step 3: call mixList
#Step 4: call random.shuffle to randomly shuffle list
#Step 5: print the list

import random

def main ():
    List = input("Put a few comma separated characters: ").split(',')
    mixList(List)
    print('Shuffled list is', List)

def mixList(List):
    random.shuffle(List)
    
main()
    



