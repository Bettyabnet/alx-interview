#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the input grid.

    Args:
        grid (list): A 2D list of integers representing the grid.
                    0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the top cell
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the bottom cell
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the left cell
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the right cell
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
