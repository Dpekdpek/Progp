from turtle import *
CA = [[0,100],[-10,90],[50,150],[110,90],[100,100],[100,0],[0,0]]




def but(list):
    for i in list:
        goto(i[0], i[1])


but(CA)
done()