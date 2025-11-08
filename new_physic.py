import numpy as np
import pygame

PIXELTOMETER=10 #10 pixels = 1m
WIDTH, HEIGHT = 1000, 600
N=50 #box size in pixels
TAILLEX, TAILLEY= (WIDTH // N)+1, (HEIGHT // N)+1 #number of boxes in each direction
FPS = 120

class Object:
    def __init__(self):
        self.Position=[0,0]
        self.PastPositions=[0,0]
        self.Velocity=0
        self.VectorForce=0
        self.Mass=0
        self.Type="Normal"
        self.Stuck=False
        self.Color=(12,65,90)
        self.ec=0
        self.CoefficientFriction=0
        self.object={} #point/line
    def MouvementUpdate(self, x,y,velocity,vectorForce):
        self.Position=

    def RotationUpdate(self, next):


#TODO: collistion detection -> SAT -> non convex to convex
#TODO: transform polygone into triangle to draw


#simule position with act force
#check if in this movement intersect
#if intersect -> calc time of impact ; calc perfect position
#calc interaction
#timeToral - timeOfImpact = remaining time
#simulate remaining time with new forces