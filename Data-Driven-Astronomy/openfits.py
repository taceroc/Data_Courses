from astropy.io import fits
import numpy as np


# hdulist = fits.open('image0.fits')
# hdulist.info()

'''
Opening a FITS file in Astropy returns a HDU (Header/Data Unit) list.
Each HDU stores headers and (optionally) image data.

The header contains metadata about the HDU object,
e.g. its dimensions and data type. Every HDU can contain image data.
The first HDU is called the primary HDU.

If we want to access individual HDUs, we can index the HDU list object returned
by fits.open. The image data can be accessed using the data attribute:
'''

hdulist = fits.open('image0.fits')
#data = hdulist[0].data

#print(data.shape)

'''
The image data is conveniently stored in a NumPy array, so we can operate
on it directly. This example prints the dimensions of the image in the
primary HDU.'''

import matplotlib.pyplot as plt

# hdulist = fits.open('image0.fits')
# data = hdulist[0].data

## Plot the 2D array
#plt.imshow(data, cmap=plt.cm.viridis)
#plt.xlabel('x-pixels (RA)')
#plt.ylabel('y-pixels (Dec)')
#plt.colorbar()
#plt.show();


'''Then, to find the brightest pixel of the image we are looking for the
largest value in the 2D array. The argmax function from numpy provides
precisely this functionality: it searches for the largest value in the
array and returns its position. However, if you've printed out the result
of argmax on its own you would have found that it does not return a tuple
of x and y coordinates but just a single index. Why is that? This function
works on a flattened (or ravelled) array, i.e. the array gets converted
to a 1D array internally before the maximum is found. To revert this, or
to "unravel" the result, we can call the function unravel_index and pass
it the dimension of the initial data array as second argument.'''

#def load_fits(filename):
#  hdulist = fits.open(filename)
#  data = hdulist[0].data

#  arg_max = np.argmax(data)
#  max_pos = np.unravel_index(arg_max, data.shape)

#  return max_pos


#bright = load_fits('image0.fits')
#print(bright)

# def mean_fits(fitsfile):
#     n = len(fitsfile)
#     data = 0
#     for i in range (0,n):
#         hdulist = fits.open(fitsfile[i])
#         data += hdulist[0].data
#         hdulist.close()
#     if n > 0:
#         data_mean =  data/n
#         return data_mean
#
# data = mean_fits(['image0.fits', 'image1.fits', 'image3.fits'])
# print(data[100, 100])
