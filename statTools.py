import math
def findMeanOfList():
  list = []
  number = int(input("Enter the length of your list"))
  print("Enter your numbers")
  for i in range (number):
     data = int(input())
     list.append(data)
  mean = float(sum(list))/number
  print ("The mean of this list is " mean)

  def findModeOfList():
   list = []
   number = int(input("Enter the length of your list"))
   print("Enter your numbers")
   for i in range (number):
     data = int(input())
     list.append(data)
   mode = max(set(list), key=list.count)
   print("The mode of this list is " mode) 
  

def findVariance(list):
  average = sum(list) / len(list)
  number = 0
  for i in list:
    number += (average - i) * (average - i)
  return round(number / len(list))

def findStandardDeviation(list):
  average = sum(list) / len(list)
  number = 0
  for i in list:
    number += (average - i) * (average - i)
  return round(math.sqrt(total / len(list)) 


 
    
  
  

