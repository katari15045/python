from copy import deepcopy

class node:
    def __init__(self):
        self.grid = []

lst = [[1, 2, 3], [4, 5, 6]]
n = node()
n.grid.append(deepcopy(lst))
lst[1][2] = 0
print(lst)
print(n.grid)
