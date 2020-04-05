def timeConversion(s):
    arr=list(s)
    if arr[8] == 'P':
        if arr[0] == '0':
            del(arr[8:])
            del(arr[0])
            arr[0] = str(int(arr[0]) + 12)
        else:
            if arr[1] == '2':
                del(arr[8:])
            else:
                del(arr[8:])
                del(arr[0])
                arr[0] = str(int(arr[0]) + 22)
    else:
        if arr[1] == '2':
            arr[1] = '0'
            arr[0] = '0'
            del(arr[8:])
        else:
            del(arr[8:])
    return ''.join(arr)
            
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
