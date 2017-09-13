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

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii
import astropy.coordinates as coord
import astropy.units as u
from astropy.visualization import hist


def chi(val, mu):
    return ((val - mu)**2)/abs(mu)

if __name__ == "__main__":
    # Read ascii table data
    data = ascii.read("sample_data.ascii")

    # Set up a list of proper motions
    ra = coord.Angle(data['ra'] * u.degree)
    ra = ra.wrap_at(180 * u.degree)
    dec = coord.Angle(data['dec'] * u.degree)
    rcoords = []
    dcoords = []
    prlx = []

    for star in data:
        rcoords.append(star['pmra'])
        dcoords.append(star['pmdec'])
        prlx.append(star['parallax'])

    # Proper motion plot
    plt.subplot(3, 2, 1)
    arr = np.array([rcoords, dcoords])
    plt.plot(arr[0,], arr[1,], 'k.')
    plt.axis([-30, 50, -60, 25])

    # Hammer projection of coords
    # TODO: Switch to BaseMap module to zoom into specific parts
    plt.subplot(3, 2, 2, projection='hammer')
    ra_norm = []
    for angle in ra.radian:
        ra_norm += [float(angle)]

    dec_norm = []
    for angle in dec.radian:
        dec_norm += [float(angle)]

    plt.scatter(ra.radian, dec.radian)

    # Right ascension histogram
    plt.subplot(3, 2, 3)
    n, bins, patches = plt.hist(rcoords, 500, normed=1, facecolor='green', alpha=0.75)
    plt.grid(True)
    plt.xlim([-100, 100])

    # Declination histogram
    plt.subplot(3, 2, 4)
    n2, bins2, patches2 = plt.hist(dcoords, 500, normed=1, facecolor='blue', alpha=0.75)
    plt.xlim([-100, 100])
    plt.grid(True)
    plt.rcParams["figure.figsize"] = (20, 3)

    # Parallax histogram
    plt.subplot(3, 2, 5)
    n2, bins2, patches2 = plt.hist(prlx, 700, normed=1, facecolor='blue', alpha=0.75)
    plt.xlim([-10, 20])
    plt.grid(True)
    plt.rcParams["figure.figsize"] = (20, 3)

    # Chi histogram
    chil = []
    for star in data:
        chil += [chi(star['pmra'],19.45) + chi(star['pmdec'], -45.35) + chi(star['parallax'],7.42)]

    plt.subplot(3, 2, 6)
    n2, bins2, patches2 = hist(chil, bins='freedman', normed=1, facecolor='blue', alpha=0.75)
    plt.grid(True)
    plt.rcParams["figure.figsize"] = (20, 3)

    # Save file
    plt.savefig('output.png', format='png', dpi=400)
    plt.show()
