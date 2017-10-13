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


from astropy.io import ascii
from astropy.table import vstack, Table
from astroquery.vizier import Vizier as vz

if __name__ == "__main__":
    data = ascii.read("../data/extended_samp.ascii")
    foundstars = []
    print("Searching for stars...")


    counter = 0
    for star in data:
        found_star = vz.query_object(str(star['ra']) + " " + str(star['dec']), catalog="II/246")
        foundstars += [found_star[0][0]]
        counter += 1
        print(f"Stars counted: {counter} \n Stars left: {len(data) - counter}")

    foundstars = vstack(foundstars)
    foundstars.write('../data/2mas_matched.ascii', format='ascii')
