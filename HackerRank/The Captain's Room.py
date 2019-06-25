##def searchCap(arr):
##    for i in set(arr):
##        if arr.count(i) == 1:
##            return i
##
##k = int(input())
##
##arr = list(map(int, input().split()))
##        
##print(searchCap(arr))


k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)
possible_groups = sum(myset)*k
total = sum(arr)
print((possible_groups - total)//(k-1))
