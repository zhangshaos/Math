# @Time: 19,8,19
# @Author: CZ



import time as Time
import math as Math
import numpy as Np


queen_tracks = []


def NQueens(width_or_lenth):
    scale = width_or_lenth
    for t in range(0, scale):
        queen_tracks.append(-1)

    cur_row = 0
    # try all possible
    while(cur_row != -1):
        # place all rows' pos
        # queen_tracks[0] -= 1# Purpose is make sure the index-0-queen not change after row0:pos = queen[0]+1 below.
        # for i in range(1, scale):
        #     queen_tracks[i] = -1
        while (cur_row > -1 and cur_row < scale):
            # ergodic all possible pos
            pos = queen_tracks[cur_row] + 1
            pos_ok = False
            while(pos < scale):
                # Judeg pos is whether OK?
                if(cur_row == 0):
                    pos_ok = True
                    break
                for pre_row in range(0, cur_row):
                    if (pos == queen_tracks[pre_row] or abs(pos-queen_tracks[pre_row]) == cur_row - pre_row):
                        pos_ok = False
                        break
                    pos_ok = True
                if (pos_ok):
                    break
                else:
                    pos += 1
            # all positions are wrong.
            if (pos_ok == False):
                queen_tracks[cur_row] = -1
                cur_row -= 1
            else:
                # pos is OK.
                queen_tracks[cur_row] = pos
                cur_row += 1
        if(cur_row == scale):
            ShowBoard(queen_tracks)
            # After Print a solution, come here.
            # We should continue the former solution's tail.
            cur_row = scale - 1



def ShowBoard(tracks):
    scale = len(tracks)
    for i in range(0,scale):
        pos = tracks[i]
        assert (pos!=-1)
        row_shape = ""
        for j in range(0,scale):
            if(j==pos):
                row_shape+="@ "
            else:
                row_shape+="- "
        print(row_shape)
    print('\n')





def Main():
    print("Board size:")
    print("width:")
    width = int(input())
    print("height:")
    height = int(input())
    orig = Time.process_time()
    NQueens(min(height,width))
    end = Time.process_time()
    print("Algorithm time:",end-orig)


Main()

