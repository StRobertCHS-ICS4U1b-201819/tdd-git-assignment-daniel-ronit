def findMeanOfList():
  list = []
  number = int(input("Enter the length of your list"))
  print("Enter your numbers")
  for i in range (number):
     data = int(input())
     list.append(data)
  mean = float(sum(list))/number

 def findModeOfList():
   list = []
   number = int(input("Enter the length of your list"))
   print("Enter your numbers")
   for i in range (number):
     data = int(input())
     list.append(data)
   return max(set(list), key=list.count)
