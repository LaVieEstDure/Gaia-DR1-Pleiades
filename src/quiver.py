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
from astropy.io import ascii
import matplotlib.pyplot as plt

data = ascii.read('../data/extended_samp.ascii')
map = Basemap(projection='hammer', lat_0=0, lon_0=0)

map.quiver((0,0), (0,0), (1,0), (1,3), units = 'xy', scale = 1)
plt.axis('equal')
plt.xticks(range(-5,6))
plt.yticks(range(-5,6))
plt.grid()
plt.show()
