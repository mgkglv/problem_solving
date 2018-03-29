#!/bin/python3

import sys

def gridSearch(G, P):    
    g = [list(w) for w in G]
    p = [list(s) for s in P]
    height_p = len(p)
    width_p = len(p[0])
    
    height_g = len(g)
    width_g = len(g[0])
    
    for i in range(height_g):
        for j in range(width_g):
            if (g[i][j] == p[0][0] 
                and height_g - i >= height_p 
                and width_g - j >= width_p):                      
                    res = True
                    for k in range(i, i + height_p):
                        if res == False:
                            break
                        for l in range(j, j + width_p):                             
                            if g[k][l] != p[k-i][l-j]:
                                res = False   
                                break
                    if res:
                        return "YES"
    return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r, c = input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)
        result = gridSearch(G, P)
        print(result)


