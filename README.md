# Gaia-DR1-Pleiades
Just me playing around with some Gaia data release 1 with data centered around the Pleiades star cluster using matplotlib and astro.py for ENGG1600 Semester 2 2017.

There are multiple files in the source directory, mainly for visualisation of data from the Gaia-Tycho catalogue. This includes graphing properties such as proper motions, apparent magnitudes in different EM bands, projecting the right ascension and declination of known Pleiades star members etc. 


**Note:** The DR1 data used is in an ascii table. The data for DR1 is usually provided as a VOTable so you must convert it to ascii yourself (`astropy.io.ascii` and `astropy.io.votable` may come in handy)

![Pleiades](https://github.com/LaVieEstDure/Gaia-DR1-Pleiades/blob/master/output_images/expanded_query.png?raw=true)

## Dependencies:
```
python3
numpy
matplotlib
BaseMap
astropy
```
