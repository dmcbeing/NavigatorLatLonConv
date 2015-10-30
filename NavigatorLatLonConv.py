#!/bin/python
import sys
#Read coordinate from console
def readCoordinate(what):
	user_in=input(what)
	crds = user_in.split(":")
	if(len(crds) == 3):	## XX:XX:XX.XXX
		return [float(crds[0]),float(crds[1]),float(crds[2])]
	if(len(crds) == 1):	## Google (floating point degrees)
		return [float(crds[0]),0,0]

def coordToDeg(coords):
	return coords[0] + coords[1]/60 + coords[2]/3600

def degToMilliArc(degs):
	return int(3600000*degs)

lon = coordToDeg(readCoordinate("Longitude:"))
lat = coordToDeg(readCoordinate("Latitude:"))
print("-= Degress =-")
print("Latitude : ",lat)
print("Longitude: ",lon)

lat = degToMilliArc(lat)
lon = degToMilliArc(lon)
print("-= MilliArcs =-")
print("Latitude : ",lat)
print("Longitude: ",lon)

print("-= Navigator XML item =-")
print("<item name=\"Enter Name Here\" lat=\""+str(lat)+"\" lon=\""+str(lon)+"\" />")
