def bigSorting(unsorted):
    return sorted(unsorted)

if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = int(input())
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print(result)
