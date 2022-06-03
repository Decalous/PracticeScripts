# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:58:00 2022

@author: Dan
"""

class Storynode:
    def __init__(self, text=None, prompts=[]):
        self.text = text
        self.prompts = prompts
        self.possiblebranches = []
    
    def branch(self):
        branchto = None
        if (len(self.prompts) == 1):
            print("0: ", self.prompts[0])
            return 0
        for i in range(len(self.prompts)):
            print(i, ": ", self.prompts[i])
        while True:
            branchto = input("Input the number of your choice:\n")
            if int(branchto) in range(len(self.prompts)):
                return int(branchto)
                
    def read(self):
        if (self.text != None):
            print(self.text)
        if (len(self.prompts) != 0 and len(self.possiblebranches) != 0):
            #branchto = self.branch()
            self.possiblebranches[self.branch()].read()

## Story class that holds the Storynodes in their tree and varables that the nodes may want to access like
## relationship points, inventory, memory of important decisions, etc

## character class?

def writestory():            
    first = Storynode("One day, Bob woke up to find himself alone in his house", 
                      ["Go outside and look for neighbors", "Stay home and do some gaming"])
    option1 = Storynode("There was no one outside. No cars, no people.", 
                        ["Go back inside and do some gaming", "Try calling a friend"])
    option2 = Storynode("Bob booted up his PC and started queued up for an ARAM. He waited for 5, 10 minutes and found no matches.", ["Maybe TFT will have a shorter queue time", "Try calling a friend"])
    option3 = Storynode("Bob tried calling his best friend Bill but there was no response.")
    option4 = Storynode("Unsurprisingly, TFT also seemed to have an infinite queue time. Bob could think of only one thing to do", ["Try calling a friend"])
    
    first.possiblebranches = [option1, option2]
    option1.possiblebranches = [option2, option3]
    option2.possiblebranches = [option4, option3]
    option4.possiblebranches = [option3]
    return first

def main():
    start = None
    start = writestory()
    start.read()
    
if __name__ == '__main__':
    main()
