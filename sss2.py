import pygame as pg
from pygame.locals import *
import math

pg.init()

black = (0,0,0)
orange = (255, 73, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (40, 40, 40)
brown = (63, 49, 41)
red = (255,0,0)

class Planet(pg.sprite.Sprite):
    def __init__(self, color, distance, radius, angle, speed, nextTick):
        pg.sprite.Sprite.__init__(self)
        self.color = color
        self.distance = distance
        self.radius = radius * 2

        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (simulation.screenCenter[0] + self.distance, simulation.screenCenter[1])

        self.angle = angle
        self.speed = speed / 100
        self.nextTick = nextTick
        
    def move(self):
        self.rect.x = simulation.screenCenter[0] + self.distance * math.cos(math.radians(self.angle))
        self.rect.y = simulation.screenCenter[1] + self.distance * math.sin(math.radians(self.angle)) 

class Simulation:
    screenSize = (901, 901)
    screenCenter = (screenSize[0] // 2, screenSize[1] // 2)
    screen = pg.display.set_mode(screenSize, RESIZABLE, 32)

    def startSimulation(self):
        self.sun = Planet(yellow, 0, 1, 0, 0, 0)
        self.mercury = Planet(grey, 6, 2, 0, 88, 0)
        self.venus = Planet(brown, 10, 2, 0, 224.7, 0)
        self.earth = Planet(blue, 14, 2, 0, 365.2, 0)
        self.mars = Planet(orange, 21, 2, 0, 687, 0)
        self.jupiter = Planet(brown, 71, 2, 0, 4331, 0)
        self.saturn = Planet(red, 130, 2, 0, 10747, 0)
        self.uranus = Planet(green, 261, 2, 0, 30589, 0)
        self.neptune = Planet(blue, 409, 2, 0, 59800, 0)

        self.solarSystem = pg.sprite.Group()

        self.planetList = [self.sun, self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn, self.uranus, self.neptune]
        for planet in self.planetList:
            self.solarSystem.add(planet)

    def animateOrbits(self):
        ticks = pg.time.get_ticks() 
        for planet in self.planetList:
            if ticks > planet.nextTick:
                planet.nextTick += planet.speed
                planet.angle += 1
                planet.move()

    def gameLoop(self):
        self.startSimulation()     
        while True:
            
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()

            self.animateOrbits()

            self.screen.fill(black)
            for planet in self.planetList:
                pg.draw.circle(self.screen, grey, self.screenCenter, planet.distance, 1)

            self.solarSystem.draw(self.screen)

            pg.display.flip()

simulation = Simulation()
simulation.gameLoop()