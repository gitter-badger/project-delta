import torch as t
import numpy as np
class Point:
    def __init__(self, x,y):#exncap
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x= x
        return
    def set_y(self, y):
        self.__y = y
        return
    def to_string(self):
        return "X Value: " + str(__x) + " | Y Value: " + str(__y)
