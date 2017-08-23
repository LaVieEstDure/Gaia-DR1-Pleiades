import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii
import astropy.coordinates as coord
import astropy.units as u

# Read ascii table data
data = ascii.read("sample_data.ascii")


# Set up a list of proper motions
ra = coord.Angle(data['ra']*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = coord.Angle(data['dec']*u.degree)
data = ascii.read("sample_data.ascii")
rcoords = []
dcoords = []
for star in data:
    rcoords.append(star['pmra'])
    dcoords.append(star['pmdec'])

# Proper motion plot
plt.subplot(2,2,1)
arr = np.array([rcoords,dcoords])
plt.plot(arr[0,],arr[1,],'k.')
plt.axis([-30, 50, -60, 25])


# Hammer projection of coords
# Switch to BaseMap module to zoom into specific parts
plt.subplot(2,2,2,projection='hammer')
ra_norm = []
for angle in ra.radian:
    ra_norm += [float(angle)]

dec_norm = []
for angle in dec.radian:
    dec_norm += [float(angle)]

plt.scatter(ra.radian, dec.radian)

# Right ascension histogram
plt.subplot(2,2,3)
n, bins, patches = plt.hist(rcoords, 500, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.xlim([-100,100])

# Declination histogram
plt.subplot(2,2,4)
n2, bins2, patches2 = plt.hist(dcoords, 500, normed=1, facecolor='blue', alpha=0.75)
plt.xlim([-100,100])
plt.grid(True)

# Save file
plt.savefig('output.png', format='png')
plt.show()