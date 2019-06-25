# Cosertar na aula.
# usar duas funções pq são dois calendarios!
# Ñ é tão simples assim


def is_leap(year):
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            if year%400==0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap


def dayOfProgrammer(year):
    if is_leap(year):
        return '{}.09.{}'.format(12, year)
    else:
        return '{}.09.{}'.format(13, year)

if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
