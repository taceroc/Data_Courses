'''
Your first task is to replicate the following SQL query:


SELECT kepler_id, radius
FROM Star
WHERE radius > 1.0;
'''

import numpy as np

# data = np.loadtxt('stars.csv', delimiter=',', usecols=(0, 2)) #kepler_id is in col 0 and radius in col 2
# filtered_data = data[data[:,1] >1,:] #look on radius (data[:,1] >1) and show the ones that full field the requirement
# #print(filtered_data)
#
#
# def query(table):
#   data = np.loadtxt(table, delimiter=',', usecols=(0, 2))
#   filtered_data = data[data[:,1] >1,:]
#   return filtered_data
#
#  print(query('stars.csv'))


'''
Let's add another element to our query. Sort the resulting table in ascending order to match the result you would get with:


SELECT kepler_id, radius
FROM Star
WHERE radius > 1.0
ORDER BY radius ASC;
'''

# def query(table):
#   data = np.loadtxt(table, delimiter=',', usecols=(0, 2))
#   filtered_data = data[data[:,1] >1,:]
#   sorted_data = filtered_data[np.argsort(filtered_data[:,1]),:] #order descending radius
#   return(sorted_data)
#
# result = query('stars.csv')
# print(result)


'''
Let's add yet another element to our query. Join the Star table with the Planet table and calculate the size ratio, i.e. planet radius / star radius for each star-planet pair. Your query function should produce the same result as the SQL query:


SELECT p.radius/s.radius AS radius_ratio
FROM Planet AS p
INNER JOIN star AS s USING (kepler_id)
WHERE s.radius > 1.0
ORDER BY p.radius/s.radius ASC;
'''
def query(table_1,table_2):
  data_1 = np.loadtxt(table_1, delimiter=',', usecols=(0, 2))
  data_2= np.loadtxt(table_2, delimiter=',', usecols=(0, 5))

  filtered_data_1 = data_1[data_1[:,1] >1,:]
  #print(filtered_data_1)
  final = np.zeros((1, 1))
  for row_1 in range(filtered_data_1.shape[0]):
    kepler_id = filtered_data_1[row_1,0]
    sun_radius = filtered_data_1[row_1,1]
    #print(kepler_id)
    matching_row = data_2[np.where(data_2[:, 0] == kepler_id), 1].T
    #print(matching_row)
    ratio = matching_row/sun_radius
    final = np.concatenate((final, ratio))
    #ratio1 = np.sort([ratio[0][0]])

    #print(ratio)
  return np.sort(final[1:], axis = 0)

# def query(fname_1, fname_2):
#   stars = np.loadtxt(fname_1, delimiter=',', usecols=(0, 2))
#   planets = np.loadtxt(fname_2, delimiter=',', usecols=(0, 5))
#
#   f_stars = stars[stars[:,1]>1, :]
#   #s_stars = f_stars[np.argsort(f_stars[:, 1]), :]
#
#   final = np.zeros((1, 1))
#   for i in range(f_stars.shape[0]):
#     kep_id = s_stars[i, 0]
#     #s_radius = s_stars[i, 1]
#
#     matching_planets = planets[np.where(planets[:, 0] == kep_id), 1]
#     print(matching_planets)
#     #final = np.concatenate((final, matching_planets/s_radius))
#
#   #return np.sort(final[1:], axis = 0)
#   return matching_planets

result = query('stars.csv', 'planets.csv')
print(result)
