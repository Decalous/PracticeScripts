# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:19:01 2022

Solves problem from: https://open.kattis.com/problems/nineknights
@author: Dan
"""

import sys

def checkattack(row,col,board):
    if row + 1 < numrows and col + 2 < numcol:
        if board[row+1][col+2] == 'k':
            #print(row, col," attacks ",row+1,col+2)
            return True
    if row + 2 < numrows and col + 1 < numcol:
        if board[row+2][col+1] == 'k':
            #print(row, col," attacks ",row+2,col+1)
            return True
    if row + 2 < numrows and col - 1 >= 0:
        if board[row+2][col-1] == 'k':
            #print(row, col," attacks ",row+2,col+1)
            return True
    if row + 1 < numrows and col - 2 >= 0:
        if board[row+1][col-2] == 'k':
            #print(row, col," attacks ",row+1,col-2)
            return True
    return False

board = []
kcount = 0
numrows = 5
numcol = 5
valid = True
for i in range(numrows):
    board.append(sys.stdin.readline().strip()) ## split to remove \n at end
#print(board)
for row in range(numrows - 1): ## don't need to check the knights in the last row
    #print(board[i])
    for col in range(len(board[row])): 
        #print(board[i][j])
        if board[row][col] == 'k':
            #print(row,col)
            kcount += 1
            if checkattack(row,col,board):
                valid = False
for col in range(len(board[numrows-1])): ## don't need to check knights in last row but do need to count
    if board[numrows-1][col] == 'k':
        #print(row,col)
        kcount += 1
    
if valid and kcount == 9:
    print('valid')
else:
    print('invalid')
            



