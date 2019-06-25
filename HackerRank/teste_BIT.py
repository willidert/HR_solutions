def Sum(bit_arr,idx):
    result=0
    while idx:
        result += bit_arr[idx]
        idx -= idx & -idx
    return result

def add(bit_arr,idx,val):
    while idx<len(bit_arr):
        print(bit_arr,idx)
        bit_arr[idx] += val
        idx += idx & -idx
