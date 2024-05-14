from turtle import *

BB = [[100, 0], [100, 100], [0, 100], [0, 0]]
BC = [[100, 0], [100, 100], [200, 100], [200, 200], [0, 200], [0, 0]]


def but(list):
    for i in list:
        goto(i[0], i[1])


but(BB)

clear()

but(BC)

done()
