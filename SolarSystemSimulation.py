import pygame as py
from pygame.locals import *
import math

py.init()

black = (0,0,0)
orange = (255, 73, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (40, 40, 40)
brown = (63, 49, 41)

class Planet:
    def __init__(self, color, distance, radius, angle, speed, nextTick):
        self.color = color
        self.distance = distance
        self.center = (simulation.screenCenter[0] + self.distance, simulation.screenCenter[1])
        self.radius = radius
        self.surface = py.display.set_mode(simulation.screenSize, RESIZABLE, 32)
        self.angle = angle
        self.speed = speed / 100
        self.nextTick = nextTick
        
    def move(self):
        theta = math.radians(self.angle)
        return simulation.screenCenter[0] + self.distance * math.cos(theta), simulation.screenCenter[1] + self.distance * math.sin(theta)

class Simulation:
    screenSize = (900, 900)
    screenCenter = (screenSize[0] // 2, screenSize[1] // 2)
    screen = py.display.set_mode(screenSize, RESIZABLE, 32)

    def startSimulation(self):

        self.sun = Planet(yellow, 0, 3, 0, 0, 0)
        self.mercury = Planet(grey, 6, 2, 0, 88, 0)
        self.venus = Planet(brown, 10, 2, 0, 224.7, 0)
        self.earth = Planet(blue, 14, 2, 0, 365.2, 0)
        self.mars = Planet(orange, 21, 2, 0, 687, 0)
        self.jupiter = Planet(brown, 71, 2, 0, 4331, 0)
        self.saturn = Planet(yellow, 130, 2, 0, 10747, 0)
        self.uranus = Planet(green, 261, 2, 0, 30589, 0)
        self.neptune = Planet(blue, 409, 2, 0, 59800, 0)

        self.planetList = [self.sun, self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn, self.uranus, self.neptune]

    def drawOrbits(self):
        for planet in self.planetList:
                py.draw.circle(planet.surface, grey, self.screenCenter, planet.distance, 1)

    def drawPlanets(self):
        for planet in self.planetList:
                py.draw.circle(planet.surface, planet.color, planet.center, planet.radius)

    def gameLoop(self):
        self.startSimulation()
        while True:
            self.screen.fill(black)
            for event in py.event.get():
                if event.type == QUIT:
                    py.quit()

            ticks = py.time.get_ticks() 
            for planet in self.planetList:
                if ticks > planet.nextTick:
                    planet.nextTick += planet.speed
                    planet.angle += 1
                    planet.center = planet.move()

            self.drawOrbits()
            self.drawPlanets()

            py.display.flip()

simulation = Simulation()
simulation.gameLoop()
