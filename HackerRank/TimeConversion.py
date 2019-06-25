import os


def timeConversion(s):

    if "PM" in s:
        r = s.find("PM")
        s = s[0:r]
        s.split(":")
        print(s)
        r = [int(num) for num in s]
        print(r)     
        r[0] += 12
        return ''.join(r)
    elif "AM" in s:
        r = s.find("AM")
        s = s[0:r]
        return s


s = input()

result = timeConversion(s)

print(result)
