from turtle import *


SCALE = 20
letter_p = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 7},
    {"x": 5, "y": 7},
    {"x": 5, "y": 0},
    {"x": 4, "y": 0},
    {"x": 4, "y": 6},
    {"x": 1, "y": 6},
    {"x": 1, "y": 0},
    {"x": 0, "y": 0},
]

letter_g = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 7},
    {"x": 5, "y": 7},
    {"x": 5, "y": 6},
    {"x": 1, "y": 6},
    {"x": 1, "y": 0},
    {"x": 0, "y": 0},
]

letter_l = [
    {"x": 0, "y": 0},
    {"x": 2, "y": 7},
    {"x": 3, "y": 7},
    {"x": 5, "y": 0},
    {"x": 4, "y": 0},
    {"x": 2.5, "y":6},
    {"x": 1, "y": 0},
    {"x": 0, "y": 0},

]

letter_e = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 7},
    {"x": 5, "y": 7},
    {"x": 5, "y": 6},
    {"x": 1, "y": 6},
    {"x": 1, "y": 4},
    {"x": 4, "y": 4},
    {"x": 4, "y": 3},
    {"x": 1, "y": 3},
    {"x": 1, "y": 1},
    {"x": 5, "y": 1},
    {"x": 5, "y": 0},
    {"x": 0, "y": 0},
]
def letter_width(letter_points):
    x_min =
def draw_letter(place,letter_points):
    penup()
    x0 = letter_points[0]['x']
    y0 = letter_points[0]["y"]
    goto((x0 + place * 6) * SCALE, y0 * SCALE)
    pendown()
    for point in letter_points:
        goto((point["x"]+place * 6) * SCALE, point["y"] * SCALE)


draw_letter(0,letter_l)
draw_letter(1,letter_p)
draw_letter(2,letter_e)
draw_letter(3,letter_g)

done()