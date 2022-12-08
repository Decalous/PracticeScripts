# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:58:42 2022

Drawing names for a gift exchange as a family and was casually interested in
what the odds were that someone picked their own name and we had to draw again

@author: piano
"""

import random, time

def name_sharing_sim(num_names):
    ## I was going to actually simulate the draws but https://docs.python.org/3/library/random.html made my job easier
    hands = random.sample(range(num_names), num_names)
    for i in range(num_names):
        if hands[i] == i:
            return False
    return True
        
def main():
    NUM_SIMS = 1000000
    NUM_NAMES = 5
    count_true = 0
    
    print("Simulating", NUM_SIMS, "gift exchanges with", NUM_NAMES, "people")
    
    start_time = time.time()
    
    for i in range(NUM_SIMS):
        if name_sharing_sim(NUM_NAMES):
            count_true += 1
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    odds = count_true / NUM_SIMS * 100
    print("Odds of successful draw:", odds, "\nThat is", count_true, "out of", NUM_SIMS,
          "\nThis simulation took", elapsed_time, "seconds")
    
if __name__ == '__main__':
    main()