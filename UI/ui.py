import numpy as np
# import pygame
w, h = 10, 10
m = [[" " for x in range(w)] for y in range(h)]

m[9][0] = "X"

print("  0 1 2 3 4 5 6 7 8 9")
for i in range(w):
    print(i, end=" ")
    for j in range(h):
        print(m[i][j], end=' ')
        if j == len(range(1, 11)): print()
    print()