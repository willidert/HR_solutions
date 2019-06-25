def hackerrankInString(s):
    Hr = list('hackerrank')
    res = []
    for i in range(10):
        if s.find(Hr[i]) != -1:
            if Hr[i] not in list('akr'):
                res.append(list(s).index(Hr[i]))
            else:
                try:
                    while list(s).index(Hr[i]) < list(s).index(Hr[i-1]):
                        ctrl = list(s)
                        ctrl[list(s).index(Hr[i])] = ctrl[list(s).index(Hr[i])].upper() 
                        s = ''.join(ctrl)
                    res.append(list(s).index(Hr[i]))
                except ValueError:
                    return 'NO3'
        else:
            return 'NO1'
    print(res)
    for i in range(1, 10):
        if res[i] < res[i-1]:
            return 'NO2'
    return 'YES'


    
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)
