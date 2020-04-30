from math import sqrt


def solve (a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print("Нет решения")
    elif d == 0:
        x = -b / (2*a)
        print("Один корень " + str(x))
    elif d > 0 :
        x1 = (-b +  sqrt (d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("Два корня х1 = " + str(x1) +  ", х2 = " + str(x2))
    else:
        print("Как ты тут оказался?")




solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)