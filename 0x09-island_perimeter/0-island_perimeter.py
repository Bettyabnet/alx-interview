#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    perimeter = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                perimeter += 4
                if i > 0 and grid[i-1][j]:
                    perimeter -= 2
                if j > 0 and row[j-1]:
                    perimeter -= 2
    return perimeter
