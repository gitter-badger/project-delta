import torch as t
import numpy as np

class Cluster:
    def __init__(self, name):
        self.centroid = 0
        self.name = name
        self.points = []
    def get_name(self):
        return self.name
    def get_centroid(self):
        return self.centroid
    def set_centroid(self, centre):
        self.centroid = centre
        return
    def set_name(self, name):
        self.name = name;
        return
    def to_string(self):
        return "Name: " +str(self.name) +" |Centroid: "+ str(self.centroid)


#self testing main
x = Cluster(2)
print(x.get_name())
x.set_name("test 2")
print(x.get_name())
x.set_centroid(120)
print(x.get_centroid())
print(x.to_string())
