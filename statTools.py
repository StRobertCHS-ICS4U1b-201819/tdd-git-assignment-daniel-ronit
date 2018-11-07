def findMeanOfList():
  list = []
  number = int(input("Enter your the Length of your List))
  print("Enter your numbers")
  for i in range (number):
     data = int(input())
     list.append(data)
  mean = float(sum(list))/number
  
