def str2list(grid):
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    return grid


def list2str(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(grid[i])
    return grid


def plantBomb(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] ==  '.':
                grid[i][j] = 'O'
            elif grid[i][j] == 'O':
                grid[i][j] = 'X'
    return grid


def explosion(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                grid[i][j] = '.'
                if i - 1 >= 0 and grid[i-1][j] == 'O':
                    grid[i-1][j] = '.'
                if i + 1 < len(grid) and grid[i+1][j] == 'O':
                    grid[i+1][j] = '.'
                if j - 1 >= 0 and grid[i][j-1] == 'O':
                    grid[i][j-1] = '.'
                if j + 1 < len(grid[0]) and grid[i][j+1] == 'O':
                    grid[i][j+1] = '.'
    return grid

            
def bomberMan(n, grid):
    #n += 1
    passo = 1
    grid = str2list(grid)
    if n == 1:
        grid = list2str(grid)
        return grid
    else:
        while n > 0:
            if passo == 2:
                grid = plantBomb(grid)
            elif passo == 3:
                grid = explosion(grid)
            n -= 1
            passo += 1
            if passo > 3:
                passo = 1
        grid = list2str(grid)
        return grid


if __name__ == '__main__':
    rcn = input().split()
    r = int(rcn[0])
    c = int(rcn[1])
    n = int(rcn[2])
    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
