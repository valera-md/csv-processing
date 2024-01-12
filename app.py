#pandas library - модуль pandas применяется для обработки и анализа табличных данных

import csv

def loadStats():
 file_name = "data/pop070100_20240111-213433.csv"
 file = open(file_name,"r")
 file_reader = csv.reader(file, delimiter = ";")
 rows = []
 for row in file_reader:
  rows.append(row) # bidimensional array/list
  #print (row)
 return rows
data = loadStats()
'''
#print(data)
for row in data[4:12]:
#print(row, "\n\n")
 if len(row) >= 1:
  print(f"{row[0]:>20s}", end = "|")
  for cell in row[1:8]:
   print(f"{cell:>3}", end = "|")
 print("\n", "-" * 50)
#for i in range(2, len(data) - 1):
 #print(data[i][0], "\n\n")
'''
'''
def printbyCountry(country_name, year = 2014):
 start_year = 2014
 period  = year - start_year
 for row in data[4:]:
  if len(row) >= 1:
   if row[0] == country_name:
    print(f"{row[0]:>20s}", end = "|")
    for cell in row[1 + period * 7 : 8 + period * 7]:
     print(f"{cell:>3}", end = "|")
 print()
printbyCountry("Afghanistan", 2016)
'''
#hm1 - refactor code
# print total for 7 cells - in this csv file database 6 cells categories per year
def printbyCountry(country_name, year = 1993):
 start_year = 1993
 period  = year - start_year
 for row in data[4:]:
  if len(row) >= 1:
   if row[0] == country_name:
    print(f"{row[0]:>20s}", end = "|")
    total = 0
    for cell in row[1 + period * 6 : 7 + period * 6]:
     print(f"{cell:>3}", end = "|")
     if cell.isnumeric():
      total += int(cell)
    print(f" total {total:>3}", end = "|")
 print()
printbyCountry("Belarus", 2001)
'''
matrix = [
 [1, 2, 3], # 0
 [4, 5, 6], # 1
 [7, 8, 9] # 2
]
# 0 1 2
print(matrix[2][2])
'''