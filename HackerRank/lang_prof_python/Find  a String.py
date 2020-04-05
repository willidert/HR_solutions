def count_substring(string, sub_string):
    cont = 0
    st = 0
    end = len(sub_string)
    while end <= len(string):
        if string[st:end] == sub_string:
            cont += 1
        st += 1
        end += 1
    return cont

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
