import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii



data = ascii.read("sample_data.ascii")
rcoords = []
dcoords = []
for star in data:
    rcoords.append(star['pmra'])
    dcoords.append(star['pmdec'])

arr = np.array([rcoords,dcoords])
plt.plot(arr[0,],arr[1,],'k.')
plt.savefig('output.png', format='png')
plt.show()
