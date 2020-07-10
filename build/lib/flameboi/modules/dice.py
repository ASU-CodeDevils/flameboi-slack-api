'''
TODO: implement this using the newly modular setup
'''

import os
import random
import time


def roll(limit):
    
    random.seed(time.time())

    output = 0

    if limit:
        
        stripped = limit.split(' ', 1)

        try:
            tmp = int(stripped[0])
        except:
            return ", a %s is not an integer..." % stripped[0]
        
        output = random.randint(0,tmp)

    else:
        output = random.randint(0,100)

    return " rolled a %d" % output