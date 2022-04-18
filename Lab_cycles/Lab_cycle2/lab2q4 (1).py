# -*- coding: utf-8 -*-
"""lab2q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nMMzKaYyo3mUy8HpmVbmGsDjX0zqyQ2j

Write a program to create a class Box with data members length, breadth, height, area, and volume. Provider constructor that enables initialization with one parameter (for cube), two parameters (for square prism) three parameters (rectangular prism). Also, provide functions to calculate area and volume. Create a list of N boxes with random measurements and print the details of the box with maximum volume: area ratio.
"""

import random
#creating class
class Box:
  def __init__(box,*arg):
    if len(arg) == 1:
      box.length = arg[0]
      box.breadth = arg[0]
      box.height = arg[0]
    elif len(arg) == 2:
      box.length = arg[0]
      box.breadth = arg[0]
      box.height = arg[1]
    else:
      box.length = arg[0]
      box.breadth = arg[1]
      box.height = arg[2]
   #function to find area
  def get_area(box):
    box.area = box.length*box.breadth
    return box.area
   #function to find volume
  def get_volume(box):
    box.volume = box.length*box.breadth*box.height
    return box.volume
   #function to print details of box
  def show(self):
    print("Dimensions : ",self.length,self.breadth,self.height,sep = " ")
    print("Area       : ",self.area)
    print("Volume     : ",self.volume)
N = int(input("Enter number of boxes to create:"))
print("\n")
box = [Box(random.randint(1,1000),random.randint(1,1000),random.randint(1,1000)) for i in range(N)]
area = [i.get_area() for i in box]
volume = [i.get_volume() for i in box]
ratio = [x//y for x,y in zip(volume,area)]
index = ratio.index(max(ratio))
#To print the details of the box with maximum volume: area ratio
print("Details of Box with Maximum Volume:Area ratio")
box[index].show()
print("Ratio      :",max(ratio))