#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Raghav Mishra"
__email__ = "r.mishra@uqconnect.edu.au"

from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np


def chi(val, mu):
    return ((val - mu)**2)/abs(mu)

if __name__ == "__main__":
    # Read ascii table data
    data = ascii.read("../data/extended_samp.ascii")

    chilit1 = []
    chilit2 = []
    for star in data:
        chidiff = chi(star['pmra'],19.45) + chi(star['pmdec'], -45.35) + chi(star['parallax'], 7.42)
        if chidiff < 10:
            chilit1 += [star]
        else:
            chilit2

    rcoords = []
    dcoords = []
    for star in chilit1:
        rcoords.append(star['pmra'])
        dcoords.append(star['pmdec'])

    # Proper motion plot
    arr = np.array([rcoords, dcoords])
    plt.plot(arr[0,], arr[1,], 'k.')
    plt.axis([-30, 50, -60, 25])
    plt.show()
