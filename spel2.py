import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

HASTIGHET = 2

spelare = Actor("fox")
myntlista = []

def flytta(sak):
    sak.x = randint(0, WIDTH - sak.width)
    sak.y = randint(0, HEIGHT - sak.height)

def skapa_mynt():
    global myntlista
    mynt = Actor("coin")
    myntlista.append(mynt)

def draw():
    screen.fill((0,128,0))
    spelare.draw()

    for mynt in myntlista:
        mynt.draw()

def update():
    global spelare
    if keyboard.right:
        spelare.x += HASTIGHET

    if keyboard.left:
        spelare.x -= HASTIGHET

    if keyboard.down:
        spelare.y += HASTIGHET

    if keyboard.up:
        spelare.y -= HASTIGHET

skapa_mynt()

pgzrun.go()
