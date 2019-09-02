# @Time: 19,8,18
# @Author: CZ



import time as Time
import math as Math
import numpy as Np


def PlaceQueen(FlatBoard,row):
    scale = int(Math.sqrt(len(FlatBoard)))
    if(row == scale):
        ShowBoard(FlatBoard)
    else:
        # ergodic all possible position
        for i in range(row*scale,(row+1)*scale):# @i: position
            place = True
            r1 = i // scale
            c1 = i % scale
            # check position whether OK
            for j in range(0,row):# @note: FlatBoard[0:row]'s ele is the position where placing queen.
                r2 = FlatBoard[j]//scale
                c2 = FlatBoard[j]%scale
                if(r1==r2 or c1==c2 or abs(c1-c2)==row-j):
                    place = False
            if(place):
                FlatBoard[row]=i
                PlaceQueen(FlatBoard,row+1)


def ShowBoard(Board):
    scale = int(Math.sqrt(len(Board)))
    for i in range(0,scale):
        # get Board[i]'s info
        queen = Board[i] - i*scale
        row_shape = ""
        for j in range(0,scale):
            if(j==queen):
                row_shape+="@ "
            else:
                row_shape+="- "
        print(row_shape)
    print("\n")


def Main():
    print("Board size:")
    print("width:")
    width = int(input())
    print("height:")
    height = int(input())
    Board = []
    for i in range(0,height):
        for j in range(0,width):
            Board.append(-1)
    orig = Time.process_time()
    PlaceQueen(Board,0)
    end = Time.process_time()
    print("Algorithm time:",end-orig)


Main()

