def countSort(arr,c,s):
    for i in arr:
        c[i[0]]+=1
    for j in range (1,len(c)):
        c[j]=c[j]+c[j-1]
    

    for i in reversed(arr):
        N=c[i[0]]
        s[N-1][1]=i[1]
        s[N-1][0]=i[0]
        c[i[0]]-=1

    for i in s:
        print(i[1],end=" ")



if __name__ == '__main__':
    n = int(input().strip())

    arr = []## list which will contain inputs
    
    s=[]#final sorted list
    c=[]#counter

    #initializing each list(count list is 1D)
    for i in range (0,n):
        arr.append([0,0])
        c.append(0)
        s.append([0,0])
    
    #assigning the input to the list according to the question
    for i in range (0,n):

        x=input().strip().split()

        m=int(x[0])
        n1=str(x[1])
        if i<n/2:

            arr[i][0]=m
            arr[i][1]="-"
        else:
           arr[i][0]=m
           arr[i][1]=n1
    
    countSort(arr,c,s)

