from vpython import *
canvas(background=color.purple)
donut = ring(radius=0.5, thinkness=0.25, color=vector(400, 100, 1))
choco = ring(radius=0.55, thinkness=0.25, color=vector(0.4, 0.2, 0))
rad = 0
while True:
    rate(10)
    donut.pos = vector(cos(rad), sin(rad), 0)
    choco.pos = vector(cos(rad), sin(rad), 0)
    rad = rad + 0.05
