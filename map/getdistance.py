# -*- coding: UTF-8 -*-

import math

class Point:
    pass

def max(a,b):
    if a>b:
        return a
    return b
def min(a,c):
    if a>c:
        return c
    return a

def lw(a, b, c):
#     b != n && (a = Math.max(a, b));
#     c != n && (a = Math.min(a, c));
    a = max(a,b)
    a = min(a,c)
    return a

def ew(a, b, c):
    
    while a > c:
        a -= c - b
    while a < b:
        a += c - b
    return a
        

def oi(a):
    return math.pi * a / 180

def Td(a, b, c, d): 
    angle = math.sin(c) * math.sin(d) + math.cos(c) * math.cos(d) * math.cos(b - a)
    angle = max(angle,-1)
    angle = min(angle,1)
    dist = 6370996.81 * math.acos(angle)
    return int(dist/10)*10

def Wv(a, b):
    if not a or not b: 
        return 0;
    a.lng = ew(a.lng, -180, 180);
    a.lat = lw(a.lat, -74, 74);
    b.lng = ew(b.lng, -180, 180);
    b.lat = lw(b.lat, -74, 74);
    return Td(oi(a.lng), oi(b.lng), oi(a.lat), oi(b.lat))

def getDistance(a, b):
    c = Wv(a, b);
    return c