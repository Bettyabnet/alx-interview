#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):

    # Create a set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # Add the first box as opened

    # Create a stack to perform DFS
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:

            if key < len(boxes) and key not in opened_boxes:
                stack.append(key)
                opened_boxes.add(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
