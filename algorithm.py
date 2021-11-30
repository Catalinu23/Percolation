from ui import cells

queue = []
track = [[0 for i in range(1000)] for j in range(1000)]
di = [0 , 0 , 1 , -1]
dj = [1 , -1 , 0 , 0]

def inMatrix(i : int , j : int):
    if i >= 0 and i < 50 and j >= 0 and j < 100:
        return 1
    return 0;

def Lee():
    for col in range(101):
        if cells[0][col] == 0:
            queue.append((0 , col))
            track[0][col] = 1
    while len(queue) > 0:
        i = queue[0][0] , j = queue[0][1]
        for k in range(4):
            newI = i + di[k]
            newJ = j + dj[k]
            if inMatrix(newI , newJ) and cells[newI][newJ] == 0 and track[newI][newJ] == 0:
                queue.append((newI , newJ))
                track[newI][newJ] = track[i][j] + 1

def _cout():
     for lin in range(50):
       for col in range(100):
           print(track[lin][col] , end = " ")
       print()
        
            

