# -*- coding: utf-8 -*-
"""lab2q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cH2mexGN-yUOGq6Yez6WLVAdjJG9LMnM

Suppose a newly born pair of rabbits, one male and one female, are
put in a field. Rabbits can mate at the age of one month so that at the
end of its second month, a female has produced another pair of
rabbits. Suppose that our rabbits never die and that the female always
produces one new pair every month from the second month.Develop a program to show a table containing the number of pairs of
rabbits in the first N months
"""

#the number of rabbits follows a fibonacci sequence
#function to calculate number of pairs
def rabbit_pair(n):
  #initialising the number of pairs of rabbits
  numPair = [1,1]
  print("\nMonth\t\tNumber of pairs ")
  for i in range(0,n):#iteration
    #printing data
    print(i+1,end="\t\t")
    print(numPair[i])
    numPair.append(numPair[i]+numPair[i+1])

#to input number of months
num = int(input("Enter number of months: "))
#calling function
rabbit_pair(num)