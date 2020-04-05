import string
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    alpha = string.ascii_lowercase

    dic = {}

    for i in range(26):
        dic[alpha[i]] = h[i]

    highletter = 0
    for i in word:
        if dic[i] > highletter:
            highletter = dic[i]

    return highletter * len(word)


if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    print(result)

    
    
