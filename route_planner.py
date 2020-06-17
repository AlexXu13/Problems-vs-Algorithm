# -*- coding: utf-8 -*-
import math
from queue import PriorityQueue
def dist(x,y):
    return math.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)

def newPath(lastpath, start, goal):
    newpath = []
    cur_point  = goal
    newpath.append(cur_point)
    while cur_point != start:
        cur_point = lastpath[cur_point]
        newpath.append(cur_point)
    newpath.reverse()
    return newpath

def shortest_path(M, start, goal):
    path = PriorityQueue()
    path.put(start, 0)
    lastpath = {start:None}
    dist_rec = {start:0}

    while not path.empty():
        cur_point = path.get()
        if cur_point == goal:
            newPath(lastpath, start, goal)
        for pos in M.roads[cur_point]:
            newdist = dist_rec[cur_point] + dist(M.intersections[cur_point], M.intersections[pos])
            if (pos not in dist_rec) or newdist < dist_rec[pos]:
                dist_rec[pos] = newdist
                sumdist = newdist + dist(M.intersections[cur_point], M.intersections[pos])
                path.put(pos, sumdist)
                lastpath[pos] = cur_point
    return  newPath(lastpath, start, goal)


