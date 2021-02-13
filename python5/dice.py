# this program is to  dispaly
# a dice rolling statistics

import random

#global constant
MIN =1
MAX = 6

def main():
    roll = 'y'

    while roll == 'y' or roll == 'Y':
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # ask again if the user want to roll
        roll = input('do you want to roll again: ')
main()        
