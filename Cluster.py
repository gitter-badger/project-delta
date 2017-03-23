import torch as t
import numpy as np
from Point import Point

class Cluster:
    def __init__(self, name):#encapsulation
        self.__centroid = 0
        self.__name = name
        self.__points = []

    def get_name(self):
        return self.__name
    def get_centroid(self):
        return self.__centroid
    def set_centroid(self, centre):
        self.__centroid = centre
        return
    def set_name(self, name):
        self.__name = name;
        return
    def to_string(self):
        return "Name: " +str(self.__name) +" | Centroid: "+ str(self.__centroid)

    def calc_centroid(self):
        return



#self testing main
x = Cluster(2)
print(x.get_name())
x.set_name("test 2")
print(x.get_name())
x.set_centroid(120)
print(x.get_centroid())
print(x.to_string())
x = Point(1,2)
print (x.get_x())
