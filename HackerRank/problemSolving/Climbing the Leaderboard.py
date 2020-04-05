def climbingLeaderboard(scores, alice):
    conj = sorted(set(scores), reverse=True)
    p = len(conj)
    res = []
    for i in alice:
        print(i)
        while p > 0 and i >= conj[p-1]:
            print(conj[p-1], p)
            p -= 1
        res.append(p+1)
    return res


if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print(result)
