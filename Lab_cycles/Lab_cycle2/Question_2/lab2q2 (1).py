# -*- coding: utf-8 -*-
"""lab2q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KX-gfPjHbAl2H-DozLbnXxeQjnziByL

Write a program to read a string containing numbers separated by a space and convert it as a list of integers. Perform the following operations on it.

1. Rotate elements in a list by 'k' position to the right
2. Convert the list into a tuple using list comprehension
3. Remove all duplicates from the tuple and convert them into a list again.
4. Create another list by putting the results of the evaluation of the function 𝑓(𝑥) = 𝑥 2 – 𝑥 with each element in the final list
5. After sorting them individually, merge the two lists to create a single sorted list
"""

#function to convert string to list of integers
def string_to_int(stringList):
  newList = [int(i) for i in stringList]
  return newList

#function to rotate elements in a list by 'k' position to the right
def rotateElements(rot_list,k):
  print("After rotating",end = ":")
  print(rot_list[-k:]+rot_list[:-k])
  print("\n")

#function to convert the list into a tuple using list comprehension
def tuple_conversion(list_l):
  #converting the list into a tuple using list comprehension
  tuple_l = tuple(list_l)
  print("Tuple: ",tuple_l)
  print(type(tuple_l))
  print("\n")
  return tuple_l

#function to remove all duplicates from the tuple and convert them into a list again
def removeDuplicates(tuple_l):
  #3.removing all duplicates
  tuple_l = tuple(set(tuple_l))
  list_l = list(tuple_l)
  print("After removing duplicates : ",list_l)
  print("\n")
  return list_l

#function to create another list by putting the results of the evaluation of the function 𝑓(𝑥) = 𝑥 2 – 𝑥 with each element in the final list
def func_append(list_l):
#Creating another list by putting the results of the evaluation of the function 𝑓(𝑥) = 𝑥 2 – 𝑥 with each element in the final list
  f = []
  for i in list_l:
    f.append((i**2)-i)
  print("List after evaluating function with each element ",end = " = ")
  print(f)
  print("\n")
  return f

#function to sort lists individually, merge the two lists to create a single sorted list
def final_single_list(list_l,f):
  #sorting individually and merging to form a single list
  finalList = list_l + f
  finalList.sort()
  print("Final list ",end = " = ")
  print(finalList)
  print("\n")

#input string
input_string = input("Enter the numbers seperated by space : ")

list_numbers = list(input_string.split(" "))
print("\n")

#calling function
list_of_int =string_to_int(list_numbers)
print("After conversion to list of integers: ")
print(list_of_int)
print("\n")

k_unit=int(input("Enter the position by which you want to rotate: "))
#calling function
rotateElements(list_of_int,k_unit)
#calling function
int_tuple = tuple_conversion(list_of_int)
#calling function
list_of_int = removeDuplicates(int_tuple)
#calling function
function_list = func_append(list_of_int)
#calling function
final_single_list(list_of_int,function_list)
