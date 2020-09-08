# -*- coding: utf-8 -*-
from statistics import mean
import numpy as np


'''
fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
m = mean(fluxes)
print (m)


fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
m = sum(fluxes)/len(fluxes)
print(m)
'''
'''
def calculate_mean(lst):
    m = sum(lst)/len(lst)
    return m

#lst = [1, 2.2, 0.3, 3.4, 7.9]
print(calculate_mean([1, 2.2, 0.3, 3.4, 7.9]))
'''

'''
#NUMPY
fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
m = np.mean(fluxes)
print(m)
print(np.size(fluxes)) # length of array
print(np.std(fluxes))  # standard deviation
'''
'''
data = []
for line in open('data.csv'):
  data.append(line.strip().split(','))

#print(data)'''

'''
The strip method removes whitespace (including the newline) from the ends of
line. The split method creates a list of strings using the ',' character as
the separator between items.
The split method returns a list of strings, so each value in each row is a
string. We have to convert the values to floats before we can do any
calculations with them.
'''

'''Convert to float:'''

'''With loops'''
'''
for line in open('data.csv'):
  row = []
  for col in line.strip().split(','):
    row.append(float(col))
  data.append(row)

#print(data) '''

'''Whit Numpy'''
'''
for line in open('data.csv'):
  data.append(line.strip().split(','))

data = np.asarray(data, float)
#print(data)'''


'''The NumPy loadtxt function can automatically read a CSV file into a NumPy
array, including converting from string to numbers. The NumPy loadtxt function
is simpler, faster, and less error-prone than our previous solution.'''

'''
data = np.loadtxt('data.csv', delimiter=',')
#print(data)'''

'''Calculate mean and median'''
'''
def calc_stats(data):
    data = np.loadtxt(data, delimiter=',')
    mean = np.round((np.mean(data)),1)
    median = np.round(np.median(data),1)
    return mean, median

mean=calc_stats('data.csv')
print(mean)'''

'''Numpy operations'''

a = np.array([[1,2,3], [4,5,6]])  # 2x3 array

# Print first row of a:
#print(a[0])

# Print second column of a:
#print(a[:,1])

lst = []

def mean_datasets(filenames):
    n = len(filenames)
    data = 0
    for i in range(0,n):
      data += np.loadtxt(filenames[i], delimiter=',')
    
    # Mean across all files:
    data_mean = data/n
        

print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

'''
data = np.loadtxt('data1.csv', delimiter=',')
print(data)
'''
