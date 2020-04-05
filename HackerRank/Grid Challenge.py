##errado

def gridChallenge(grid):
    if len(set(grid)) == 1:
        return 'YES'
    j = len(grid[0]) - 1
    for i in range(len(grid )):
        str1 = list(grid[i])
        str1.sort()
        grid[i] = ''.join(str1)
        while j >= 0 and i > 0:
            if grid[i][j] < grid[i-1][j]:
                return 'NO'
            j -= 1
    return 'YES'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []
        
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        if t_itr == 73:
            for i in grid:
                print(i)
        result = gridChallenge(grid)
        if t_itr == 73:
            for i in grid:
                print(i)
        
        print(result)
