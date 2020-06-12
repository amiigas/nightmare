import numpy as np


bound = range(0,4)
route = []

def moves(grid,node):
    i = np.where(grid == node)[0][0]
    j = np.where(grid == node)[1][0]

    moves = []

    for x in [-1, 1]:
        for y in [-2, 2]:
            if i + x in bound and j + y in bound:
                moves.append(grid[i + x][j + y])
            if i + y in bound and j + x in bound:
                moves.append(grid[i + y][j + x])

    return moves


def dfs(grid,node,stop):

    ### droga jest tutaj tożsama z listą odwiedzonych ###

    # czy został odnaleziony wierzchołek końcowy
    if node == stop:
        route.append(node) # wierzchołek celu
        print(route)
        return True

    # dodaj do odwiedzonych
    route.append(node)
    # sąsiadujące wierzchołki (ruchy)
    adjacent = moves(grid,node)

    for move in adjacent:
        if not route.__contains__(move):
            if dfs(grid,move,stop):
                return True

    # nie znaleziono, powrót
    route.pop(len(route) - 1)
    return False
