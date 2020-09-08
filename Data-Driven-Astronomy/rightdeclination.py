# -*- coding: utf-8 -*-
import numpy as np

#def hms2dec (H,M,S):
#    return 15*(H+(M/60)+(S/(60*60)))

#def dms2dec(D,M,S):
#    if D>0:
#        dec= D+(M/60)+(S/(60*60))
#    else:
#        dec=-1*(-D+(M/60)+(S/(60*60)))
#    return dec
    

#print(hms2dec(23, 12, 6))
#print(dms2dec(22, 57, 18))
#print(dms2dec(-66, 5, 5.1))


'''Write a function called angular_dist that calculates the angular distance
between any two points on the celestial sphere given their right ascension
and declination.

Your function should take arguments in decimal degrees and return the distance
in decimal degrees too.'''


#def angular_dist (ra1_deg, dec1_deg, ra2_deg, dec2_deg):
#    ra1 = np.radians(ra1_deg) #convertir degrees to radianes
#    dec1 = np.radians(dec1_deg)
#    ra2 = np.radians(ra2_deg)
#    dec2 = np.radians(dec2_deg)
#    a = np.sin(np.abs(dec1-dec2)/2)**2
#    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
#    d = 2*np.arcsin(np.sqrt(a+b))
#    d_deg = np.degrees(d) #convertir radianes to degrees
#    return d_deg


#ra1, dec1 = 21.07, 0.1
#ra2, dec2 = 21.15, 8.2
#print(angular_dist(ra1, dec1, ra2, dec2))
#print(angular_dist(10.3, -3, 24.3, -29))

'''Write import_bss and import_super functions that import the AT20G BSS and
SuperCOSMOS catalogues from the files bss.dat and super.csv as described in
the previous slides.

Each function should return a list of tuples containing the object's ID
(an integer) and the coordinates in degrees. The object ID should be the
row of the object in the catalogue, starting at 1.'''

#catb = np.loadtxt('bss.dat', usecols=range(1, 7))
#print(catb[0])

#cats = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
#print(cats)


#def hms2dec (H,M,S):
#    return 15*(H+(M/60)+(S/(60*60)))

#def dms2dec(D,M,S):
#    if D>0:
#        dec= D+(M/60)+(S/(60*60))
#    else:
#        dec=-1*(-D+(M/60)+(S/(60*60)))
#    return dec

#def import_bss():
#  res = []
#  data = np.loadtxt('bss.dat', usecols=range(1, 7))
#  for i, row in enumerate(data, 1): #toma data que esta asi [[0]\\[1]\\[2]\\..\\[n]] donde data1 es [0], data2[1], data3[2] and so on, llama 
#    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5]))) #por eso se llamada raw, data agarra caja fila y cada fila es una lista y raw[0] llama el primer elemento de la lista 
#  return res

#def import_super():
#  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
#  res = []
#  for i, row in enumerate(data, 1):
#    res.append((i, row[0], row[1])) #llenar tuple
#  return res

#bss_cat = import_bss()
#super_cat = import_super()
#print(bss_cat)
#print(super_cat)

#data = np.loadtxt('bss.dat', usecols=range(1, 7))
#for i, row in enumerate(data, 1):
#     print (i,row)


'''Write a find_closest function that takes a catalogue and the position
of a target source (a right ascension and declination) and finds the
closest match for the target source in the catalogue.

Your function should return the ID of the closest object and the distance
to that object.

The right ascension and declination are in degrees. The catalogue list has
been loaded by import_bss from the previous question. The full 320 object
BSS catalogue is contained in bss.dat for you to test your code on.'''
##def hms2dec (H,M,S):
##    return 15*(H+(M/60)+(S/(60*60)))
##
##def dms2dec(D,M,S):
##    if D>0:
##        dec= D+(M/60)+(S/(60*60))
##    else:
##        dec=-1*(-D+(M/60)+(S/(60*60)))
##    return dec
##
##def angular_dist (ra1_deg, dec1_deg, ra2_deg, dec2_deg):
##    ra1 = np.radians(ra1_deg) #convertir degrees to radianes
##    dec1 = np.radians(dec1_deg)
##    ra2 = np.radians(ra2_deg)
##    dec2 = np.radians(dec2_deg)
##    a = np.sin(np.abs(dec1-dec2)/2)**2
##    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
##    d = 2*np.arcsin(np.sqrt(a+b))
##    d_deg = np.degrees(d) #convertir radianes to degrees
##    return d_deg
##
##def import_bss():
##  res = []
##  data = np.loadtxt('table2.dat.txt', usecols=range(1, 7))
##  for i, row in enumerate(data, 1): #toma data que esta asi [[0]\\[1]\\[2]\\..\\[n]] donde data1 es [0], data2[1], data3[2] and so on, llama 
##    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5]))) #por eso se llamada raw, data agarra caja fila y cada fila es una lista y raw[0] llama el primer elemento de la lista 
##  return res
##
##def import_super():
##  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
##  res = []
##  for i, row in enumerate(data, 1):
##    res.append((i, row[0], row[1])) #llenar tuple
##  return res
##
##def find_closest(cat,ra2_deg,dec2_deg):
##    min_dist = np.inf
##    min_id = None
##    for i, row in enumerate(cat, 1):
##        ra1_deg = row[1]
##        dec1_deg = row[2]
##        dist = angular_dist(ra1_deg, dec1_deg, ra2_deg, dec2_deg)
##        if dist < min_dist:
##            min_id = i
##            min_dist = dist          
##    return min_id,min_dist
##             
##         
##    
##
##cat = import_bss()
###for i, row in enumerate(cat, 1):
###       ra1_deg = row[1]
###        dec1_deg = row[2]
###        print(ra1_deg, dec1_deg)
##print(find_closest(cat, 175.3, -32.5))

'''Write a crossmatch function that crossmatches two catalogues within a
maximum distance. It should return a list of matches and non-matches for
the first catalogue against the second.

The list of matches contains tuples of the first and second catalogue object
IDs and their distance. The list of non-matches contains the unmatched object
IDs from the first catalogue only. Both lists should be ordered by the first
catalogue's IDs.

The BSS and SuperCOSMOS catalogues will be given as input arguments, each in
the format you’ve seen previously. The maximum distance is given in decimal
degrees.

Here's how crossmatch should work on our sample catalogues with a maximum
distance of 40 arcseconds:'''

##def hms2dec (H,M,S):
##    return 15*(H+(M/60)+(S/(60*60)))
##
##def dms2dec(D,M,S):
##    if D>0:
##        dec= D+(M/60)+(S/(60*60))
##    else:
##        dec=-1*(-D+(M/60)+(S/(60*60)))
##    return dec
##
##def import_bss():
##    res = []
##    data = np.loadtxt('table2.dat.txt', usecols=range(1, 7))
##    for i, row in enumerate(data, 1): #toma data que esta asi [[0]\\[1]\\[2]\\..\\[n]] donde data1 es [0], data2[1], data3[2] and so on, llama
##        res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5]))) #por eso se llamada raw, data agarra caja fila y cada fila es una lista y raw[0] llama el primer elemento de la lista 
##    return res
##
##def import_super():
##    data = np.loadtxt('super2.csv', delimiter=',', skiprows=1, usecols=(0, 1))
##    res = []
##    for i, row in enumerate(data, 1):
##        res.append((i, row[0], row[1])) #llenar tuple
##    return res
##
##def angular_dist (ra1_deg, dec1_deg, ra2_deg, dec2_deg):
##    ra1 = np.radians(ra1_deg) #convertir degrees to radianes
##    dec1 = np.radians(dec1_deg)
##    ra2 = np.radians(ra2_deg)
##    dec2 = np.radians(dec2_deg)
##    a = np.sin(np.abs(dec1-dec2)/2)**2
##    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
##    d = 2*np.arcsin(np.sqrt(a+b))
##    d_deg = np.degrees(d) #convertir radianes to degrees
##    return d_deg
##
##def find_closest(cat,ra2_deg,dec2_deg):
##    min_dist = np.inf
##    min_id = None
##    for i, row in enumerate(cat, 1):
##        ra1_deg = row[1]
##        dec1_deg = row[2]
##        dist = angular_dist(ra1_deg, dec1_deg, ra2_deg, dec2_deg)
##        if dist < min_dist:
##            min_id = i
##            min_dist = dist          
##    return min_id,min_dist
##
##def crossmatch(bss_cat, super_cat,max_dist):
##    matches = []
##    no_matches = []
##    for i, row in enumerate(bss_cat,1) :
##        ra2_deg = row[1]
##        dec2_deg = row[2]
##        closest_id, closest_dist = find_closest(super_cat,ra2_deg, dec2_deg)
##        if closest_dist > max_dist:
##            no_matches.append(i)
##        else:
##            matches.append((i, closest_id, closest_dist))
##    return matches, no_matches
##        
##bss_cat = import_bss()
##super_cat = import_super()
##
##max_dist = 5/3600
##matches, no_matches = crossmatch(bss_cat,super_cat,max_dist)
##print(matches) #imprime los primeros tres tuples de la gran lista
##print(no_matches[:3])
##print(len(no_matches))

'''Write a crossmatch function for two catalogues to within a maximum radius.
The catalogues are 2D NumPy arrays of RA and declination in degrees.

Your function should convert all the coordinates to radians before it starts
crossmatching. It should return 3 values:

A list of tuples of matched IDs and their distance in degrees;
A list of unmatched IDs from the first catalogue;
The time taken (in seconds) to run the crossmatcher.
Both catalogues are given as an N×2 NumPy array of floats. Each row contains
the coordinates of a single object. The two columns are the RA and declination.

An object's ID is the index of its row, starting at 0. Your function should
work with input catalogues with any number of objects.'''

##import time
##
##def hms2dec (H,M,S): #RightAsention
##    return 15*(H+(M/60)+(S/(60*60)))
##
##def dms2dec(D,M,S): #Declination
##    if D>0:
##        dec= D+(M/60)+(S/(60*60))
##    else:
##        dec=-1*(-D+(M/60)+(S/(60*60)))
##    return dec
##
##
##def find_closest(cat,ra2_deg,dec2_deg):
##    min_dist = np.inf
##    min_id = None
##    for i, row in enumerate(cat, 0):
##        ra1_deg = row[0]
##        dec1_deg = row[1]
##        dist = angular_dist(ra1_deg, dec1_deg, ra2_deg, dec2_deg)
##        if dist < min_dist:
##            min_id = i
##            min_dist = dist          
##    return min_id,min_dist
##
##def angular_dist (ra1, dec1, ra2, dec2):
##    a = np.sin(np.abs(dec1-dec2)/2)**2
##    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
##    d = 2*np.arcsin(np.sqrt(a+b))
##    #d_deg = np.degrees(d) #convertir radianes to degrees
##    return d
##
##def crossmatch(cat1,cat2,max_distance):
##    start = time.perf_counter()
##    max_distance = np.radians(max_distance)
##    
##    matches = []
##    no_matches = []
##    
##    cat1 = np.radians(cat1)
##    cat2 = np.radians(cat2)
##    
##    for i, row in enumerate(cat1,0) :
##        ra2_deg = row[0]
##        dec2_deg = row[1]
##        closest_id, closest_dist = find_closest(cat2,ra2_deg, dec2_deg)
##        if closest_dist > max_distance:
##            no_matches.append(i)
##        else:
##            matches.append((i, closest_id, np.degrees(closest_dist)))
##            
##    time_taken = time.perf_counter() - start        
##    return matches, no_matches, time_taken
##    
##
##cat1 = np.array([[180, 30], [45, 10], [300, -45]])
##cat2 = np.array([[180, 32], [55, 10], [302, -44]])
##matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
##print('matches:', matches)
##print('unmatched:', no_matches)
##print('time taken:', time_taken)
##
##
### A function to create a random catalogue of size n
##def create_cat(n):
##    ras = np.random.uniform(0, 360, size=(n, 1))
##    decs = np.random.uniform(-90, 90, size=(n, 1))
##    return np.hstack((ras, decs))
##
### Test your function on random inputs
##np.random.seed(0)
##cat1 = create_cat(10)
##cat2 = create_cat(20)
##matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
##print('matches:', matches)
##print('unmatched:', no_matches)
##print('time taken:', time_taken)

'''Copy and modify your previous angular_dist and crossmatch in radians
functions to calculate the distances to all of the objects in the second
catalogue using NumPy arrays.

The return values should behave the same way as the original function,
given the same arguments, except time_taken should be noticeably smaller
for large catalogues.'''

##import time
##
##
##def angular_dist (ra1, dec1, ra2, dec2):
##    a = np.sin(np.abs(dec1-dec2)/2)**2
##    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
##    d = 2*np.arcsin(np.sqrt(a+b))
##    #d_deg = np.degrees(d) #convertir radianes to degrees
##    return d
##
##def crossmatch(cat1,cat2,max_distance):
##    start = time.perf_counter()
##    max_distance = np.radians(max_distance)
##    
##    matches = []
##    no_matches = []
##    
##    cat1 = np.radians(cat1)
##    cat2 = np.radians(cat2)
##    
##    ra2_deg = cat2[:,0]
##    dec2_deg = cat2[:,1]
##
##    for i, row in enumerate(cat1, 0):
##        ra1_deg = row[0]
##        dec1_deg = row[1]
##        dist = angular_dist(ra1_deg, dec1_deg, ra2_deg, dec2_deg)
##        min_dist = np.min(dist)
##        min_id = np.argmin(dist)
##        #closest_id, closest_dist = find_closest(cat2,ra2_deg, dec2_deg)
##        if min_dist > max_distance:
##            no_matches.append(i)
##        else:
##            matches.append((i,min_id, np.degrees(min_dist)))
##            
##    time_taken = time.perf_counter() - start        
##    return matches, no_matches, time_taken
##
##ra1, dec1 = np.radians([180, 30])
##cat2 = [[180, 32], [55, 10], [302, -44]]
##cat2 = np.radians(cat2)
##ra2s, dec2s = cat2[:,0], cat2[:,1]
##dists = angular_dist(ra1, dec1, ra2s, dec2s)
##print(np.degrees(dists))

##cat1 = np.array([[180, 30], [45, 10], [300, -45]])
##cat2 = np.array([[180, 32], [55, 10], [302, -44]])
##matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
##print('matches:', matches)
##print('unmatched:', no_matches)
##print('time taken:', time_taken)


'''Copy your crossmatch solution from Microoptimisation and modify it so that
it sorts catalogue 2 by declination and breaks out of the inner loop early.

Your crossmatch should break out of the loop over the second catalogue when
the declination reaches dec1 + max_radius.

The return values should behave the same way as the original function, given
the same arguments, except time_taken should be noticeably smaller for large
catalogues.

We will test your function on random input arrays. We've included the function
create_cat in the starting file to generate random arrays so you can test your
function yourself.'''
##import time
##
##def angular_dist (ra1, dec1, ra2, dec2):
##    a = np.sin(np.abs(dec1-dec2)/2)**2
##    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
##    d = 2*np.arcsin(np.sqrt(a+b))
##    #d_deg = np.degrees(d) #convertir radianes to degrees
##    return d
##
##def crossmatch(cat1,cat2,max_distance):
##    start = time.perf_counter()
##    max_distance = np.radians(max_distance)
##    
##    matches = []
##    no_matches = []
##    
##    cat1 = np.radians(cat1)
##    cat2 = np.radians(cat2)
##    order = np.argsort(cat2[:,1]) #ordenar por declinacion
##    cat2_ordered = cat2[order] #definir la lista de cat2 en ese orden
##      
## #   ra2_deg = cat2_ordered[:,0]
###    dec2_deg = cat2_ordered[:,1]
##
##    for id1,(ra1_deg,dec1_deg) in enumerate(cat1, 0):
##        min_dist = np.inf
##        min_id = None
##        max_dec = dec1_deg + max_distance #definir lamaxima declinacion tolerada
##        for id2,(ra2_deg, dec2_deg) in enumerate (cat2_ordered,0):
##            if dec2_deg > max_dec:
##                break
##            dist = angular_dist(ra1_deg, dec1_deg, ra2_deg, dec2_deg)
##            if dist < min_dist:
##                min_id2 = order[id2]
##                min_dist = dist
##  
##        
##        if min_dist > max_distance:
##            no_matches.append(id1)
##        else:
##            matches.append((id1, min_id2, np.degrees(min_dist)))
##            
##    time_taken = time.perf_counter() - start        
##    return matches, no_matches, time_taken
##
####cat1 = np.array([[180, 30], [45, 10], [300, -45]])
####cat2 = np.array([[180, 32], [55, 10], [302, -44]])
####matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
####print('matches:', matches)
####print('unmatched:', no_matches)
####print('time taken:', time_taken)
##
##
##def create_cat(n):
##    ras = np.random.uniform(0, 360, size=(n, 1))
##    decs = np.random.uniform(-90, 90, size=(n, 1))
##    return np.hstack((ras, decs))
##
##  # Test your function on random inputs
##np.random.seed(0)
##cat1 = create_cat(10)
##cat2 = create_cat(20)
##matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
##print('matches:', matches)
##print('unmatched:', no_matches)
##print('time taken:', time_taken)


'''If a list is sorted, it can be much faster to find the index of some element using a
binary search, rather than doing comparisons on every element in the list.

A binary search splits the list in half repeatedly, continuing the search in the half
that may contain the target element.

An example is finding the value 15 in the following list:

#     0   1   2   3   4   5   6   7   8   9
s = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

The middle (rounding down) of s is s[4], which is 14;
14 is less than 15, so 15 must be in s[5:10];
The middle of s[5:10] is s[7], which is 17;
17 is greater than 15, so 15 must be somewhere in s[5:7];
The midpoint of s_list[5:7] is s[5], which is 15;
15 is the element we're searching for, so its index is 5
This seems a roundabout way of finding 15 in a list of 10 to 19, but note that only 3
comparisons were made, whereas 6 comparisons would been made if we'd just searched the
whole list.

On big arrays the savings can be enormous. Whereas 500 comparisons are on average necessary
to find an element in a list of length 1000 with direct searching, only 10 are necessary
with a binary search.

NumPy provides binary search with the searchsorted function.

Rather than searching for a specific element, searchsorted finds the insertion position
of the target (actually the index after) that would maintain the sorted order. Using the
previous example, we can find the element just after the number 14.5:'''

##
###     0   1   2   3   4   5   6   7   8   9
##s = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
##
##index = np.searchsorted(s, 15, side='left')
##print(index)


'''Copy crossmatch from Break out and modify it to only loop through objects in
the second catalogue with declinations between dec1 - max_radius and dec1 + max_radius
using binary search.

Your crossmatch should use np.searchsorted to find the starting point
(just before dec1 - max_radius) and then break out of the loop when the declination
reaches dec1 + max_radius.

The return values should behave the same way as the original function, given the same
arguments, except time_taken should be noticeably smaller for large catalogues.

We will test your function on random input arrays. We've included the function
create_cat in the starting file to generate random arrays so you can test your
function yourself.'''

import time

def angular_dist (ra1, dec1, ra2, dec2):
    a = np.sin(np.abs(dec1-dec2)/2)**2
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    d = 2*np.arcsin(np.sqrt(a+b))
    #d_deg = np.degrees(d) #convertir radianes to degrees
    return d

def crossmatch(cat1,cat2,max_distance):
    start = time.perf_counter()
    max_distance = np.radians(max_distance)
    
    matches = []
    no_matches = []
    
    cat1 = np.radians(cat1)
    cat2 = np.radians(cat2)
    order = np.argsort(cat2[:,1]) #ordenar por declinacion
    cat2_ordered = cat2[order] #definir la lista de cat2 en ese orden
    dec2_ordered = cat2_ordered[:,1]
 

    for id1,(ra1_deg,dec1_deg) in enumerate(cat1, 0):
        min_dist = np.inf
        min_id2 = None
        min_dec = dec1_deg - max_distance
        max_dec = dec1_deg + max_distance #definir lamaxima declinacion tolerada
        min_decid = np.searchsorted(dec2_ordered ,min_dec, side = 'left')
        max_decid = np.searchsorted(dec2_ordered ,max_dec, side = 'right')
        for id2, (ra2_deg, dec2_deg) in enumerate (cat2_ordered[min_decid:max_decid+1],min_decid):
            dist = angular_dist(ra1_deg, dec1_deg, ra2_deg, dec2_deg)
            if dist < min_dist:
                min_id2 = order[id2]
                min_dist = dist
  
        
        if min_dist > max_distance:
            no_matches.append(id1)
        else:
            matches.append((id1, min_id2, np.degrees(min_dist)))
            
    time_taken = time.perf_counter() - start        
    return matches, no_matches, time_taken

cat1 = np.array([[180, 30], [45, 10], [300, -45]])
cat2 = np.array([[180, 32], [55, 10], [302, -44]])
matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
print('matches:', matches)
print('unmatched:', no_matches)
print('time taken:', time_taken)
