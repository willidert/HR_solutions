def catAndMouse(x, y, z):
    catA = z - x
    catB = z - y
    if catA < 0:
        catA *= -1
    if catB < 0:
        catB *= -1
    if catA< catB:
        return 'Cat A'
    elif catA == catB:
        return 'Mouse C'
    else:
        return 'Cat B'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)
