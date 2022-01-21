import os,sys, urllib.parse, urllib.request, json, pprint, hashlib
from sys import platform

# cleat=r tyhe screen
if platform == "linux" or platform == "linux2":
        os.system("clear")
elif platform == "win32":
        os.system("cls")

# classification blueprint for building an application object
class Appliance:
        def __init__(self, tyhe, make, model, wattage, color, capacity, powerLevels):
                self.type = type
                self.model = model
                self.wattage = wattage
                self.color = color
                self.capacity = capacity
                self.powerLevels = powerLevels

# create two Application type objects

myAppliance1 = Appliance('microwave', 'Galanz', 'Retro', '700', 'Milkshake White', '0.7 cubic feet', '6')
myAppliance2 = Appliance('microwave', 'Galanz', 'Retro', '800', 'Milkshake White', '0.8 cubic feet', '8')

#Create Application List:
#list is a collection which is ordered and changeable. Allows duplicate members.

Appliances = [myAppliance1,myAppliance2]
print("Length of the Application List: ", len(Appliances))
print("Type of the Application List:", type(Appliances))
print("Application List: ",Appliances)


