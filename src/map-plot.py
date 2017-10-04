#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Raghav Mishra"
__email__ = "r.mishra@uqconnect.edu.au"


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii
import astropy.coordinates as coord
import astropy.units as u

def chi(val, mu):
    return ((val - mu)**2)/abs(mu)

map = Basemap(projection='hammer',
              lat_0=0, lon_0=0)

    # Read ascii table data
data = ascii.read("sample_data.ascii")
fig = plt.figure()
ax1 = fig.add_subplot(111)

chilit1 = []
chilit2 = []
for star in data:
    chidiff = chi(star['pmra'],19.45) + chi(star['pmdec'], -45.35) + chi(star['parallax'], 7.42)
    if chidiff < 10:
        chilit1 += [star]
    else:
        chilit2 += [star]

rcoords = []
dcoords = []
for star in chilit2:
    rcoords.append(star['ra'])
    dcoords.append(star['dec'])

rcoordsnon = []
dcoordsnon = []
for star in chilit1:
    rcoordsnon.append(star['ra'])
    dcoordsnon.append(star['dec'])

colours = []
for i in rcoords:
    colours += [1]
for i   in rcoordsnon:
    colours += [0]

print(rcoords)

x, y = map(rcoords, dcoords)
x2, y2 = map(rcoordsnon, dcoordsnon)

map.scatter(x, y, color='y')
map.scatter(x2, y2, marker='D', color='k')

plt.show()
