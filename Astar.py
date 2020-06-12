import numpy as np
from queue import PriorityQueue


bound = range(0,4)
route = []

def moves(grid, node):
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


def manhattan(grid, a, b):
    a = np.where(grid == a)
    b = np.where(grid == b)

    return abs(a[0]-b[0])+abs(a[1]-b[1])


def a_star(grid, start, stop):
    
    knight_cost = 1
    frontier = PriorityQueue()
    frontier.put(start,0)

    # słownik kosztu drogi
    f = {}
    f[start] = 0

    # słownik poprzedników
    previous_of = {}
    previous_of[start] = None

    # dopóki lista nie jest pusta
    while not frontier.empty():
        current = frontier.get()

        if current == stop:
            # śledzenie tak aby wypisać drogę od początku
            route.append(current)
            while previous_of[current] is not None:
                route.append(previous_of[current])
                current = previous_of[current]
            route.reverse()
            print(route)
            # koniec działania
            break

        # koszt ruchu (dotychczasowy + koszt ruchu skoczka)
        cost = f[current] + knight_cost

        for move in moves(grid,current):
            # jeśli ruch nierozważony lub koszt dotarcia mniejszy niż inną drogą
            if not f.__contains__(move) or cost < f[move]:
                f[move] = cost # nowy koszt
                priority = cost + manhattan(grid, move, stop) # g(n)+h(n)
                frontier.put(move, priority) # dodaj do kolejki
                previous_of[move] = current # ustaw poprzednika
