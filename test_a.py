# Given a list of tuples A = (x, y), where x is an integer from 0 to 13 and y is an integer from 0 to 3, 
# with all possible values of A without repetition and sorted by y then x in ascending order, write a pseudocode to shuffle A.

import random
from typing import List, Tuple

def shuffle_tuples(tuples_list: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    shuffled = tuples_list.copy()
    
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled
   