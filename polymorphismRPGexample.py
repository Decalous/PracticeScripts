# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:31:57 2022

@author: Dan
"""
import random


class Enemy:
    def __init__(self,level):
        raise NotImplementedError("Subclass needs __init__ defined")
            
    def battlecry(self):
        raise NotImplementedError("Subclass needs battlecry defined")
    
    
class Slime(Enemy):
    def __init__(self,level):
        self.hp = level * 10
        self.str = level * 2
        self.spd = level * 2
    def battlecry(self):
        print("blblbl! (I'm a slime! DIE!)")
    
class Orc(Enemy):
    def __init__(self,level):
        self.hp = level * 3
        self.str = level * 10
        self.spd = level * 2
    def battlecry(self):
        print("Looks like meat's on the menu")
    
class Witch(Enemy):
    def __init__(self,level):
        self.hp = level * 2
        self.str = level * 2
        self.spd = level * 3
    def battlecry(self):
        print("Wahahahaha")

def dungeoncrawl(numEnemies):
    ## generate list of random enemies
    enemies = []
    for i in range(numEnemies):
        r = random.randint(0,2)
        if r == 0:
            enemies.append(Slime(i+1))
        elif (r == 1):
            enemies.append(Orc(i+1))
        else:
            enemies.append(Witch(i+1))
    for i in enemies:                       ## the reason to implement polymorphism
        i.battlecry()
        print(i.hp,i.str,i.spd)
        
dungeoncrawl(5)