def timeInWords(h, m):
    hours = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'twenty one': 21,
        'twenty two': 22,
        'twenty three': 23,
        'twenty four': 24,
        'twenty five': 25,
        'twenty six': 26,
        'twenty seven': 27,
        'twenty eight': 28,
        'twenty nine': 29
        }
##    quarters são multiplos de 15
    if m == 00:
        return  ''.join([i for i  in hours.keys() if hours[i] == h]) + " o' clock"
    elif m in hours.values() and m == 1:
        return ''.join([i for i  in hours.keys() if hours[i] == m])+' minute past '+''.join(i for i  in hours.keys() if hours[i] == h)
    elif m in hours.values():
        return ''.join([i for i  in hours.keys() if hours[i] == m])+' minutes past '+''.join(i for i  in hours.keys() if hours[i] == h)
    elif m in [15, 45]:
        return 'quarter past '+''.join([i for i  in hours.keys() if hours[i] == h]) if m == 15 else 'quarter to ' + ''.join(i for i  in hours.keys() if hours[i] == h + 1)
    elif m == 30:
        return 'half past '+''.join([i for i  in hours.keys() if hours[i] == h])
    else:
        if m > 31:
            return ''.join([i for i  in hours.keys() if hours[i] == 60 - m])+' minutes to '+ ''.join(i for i  in hours.keys() if hours[i] == h + 1)
        else:
            return ''.join([i for i  in hours.keys() if hours[i] == 60 - m])+' minute to '+ ''.join(i for i  in hours.keys() if hours[i] == h + 1)
    

if __name__ == '__main__':
    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result)
