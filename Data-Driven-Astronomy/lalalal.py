# -*- coding: utf-8 -*-



##import numpy as np
##from astropy.coordinates import SkyCoord #The SkyCoord objects are general
#purpose sky catalogue storage and manipulation objects in Astropy.
#They take anything that looks like an array of coordinates as long as
#you specify the units (here we specify degrees with u.degree)
#and a reference frame (ICRS is essentially the same as equatorial
#coordinates. 
##from astropy import units as u
##coords1 = [[270, -30], [185, 15]]
##coords2 = [[185, 20], [280, -30]]
##sky_cat1 = SkyCoord(coords1*u.degree, frame='icrs')
##sky_cat2 = SkyCoord(coords2*u.degree, frame='icrs')
##closest_ids, closest_dists, closest_dists3d = sky_cat1.match_to_catalog_sky(sky_cat2)
##print(closest_ids)
##print(closest_dists)

import  astropy 
astropy.test()

import numpy as np
import time
from astropy.coordinates import SkyCoord #The SkyCoord objects are general
#purpose sky catalogue storage and manipulation objects in Astropy.
#They take anything that looks like an array of coordinates as long as
#you specify the units (here we specify degrees with u.degree)
#and a reference frame (ICRS is essentially the same as equatorial
#coordinates. 
from astropy import units as u



def crossmatch(cat1,cat2,max_distance):
    start = time.perf_counter()
    #max_distance = np.radians(max_distance) porque? no hay que pasarlo a radianes?
    
    matches = []
    no_matches = []
    
    sky_cat1 = SkyCoord(cat1*u.degree, frame='icrs')
    sky_cat2 = SkyCoord(cat2*u.degree, frame='icrs')
 
    closest_ids, closest_dists, closest_dists3d = sky_cat1.match_to_catalog_sky(sky_cat2)
    #da el id del catalogo 2

    for id1, (closest_id2, dist) in enumerate(zip(closest_ids, closest_dists)):
        #zip itera sobre dos listas de forma paralela
        closest_dist = dist.value
        
        if closest_dist > max_distance:
            no_matches.append(id1)
        else:
            matches.append((id1, closest_id2, closest_dist))
            
    time_taken = time.perf_counter() - start        
    return matches, no_matches, time_taken

cat1 = np.array([[180, 30], [45, 10], [300, -45]])
cat2 = np.array([[180, 32], [55, 10], [302, -44]])
matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
print('matches:', matches)
print('unmatched:', no_matches)
print('time taken:', time_taken)
