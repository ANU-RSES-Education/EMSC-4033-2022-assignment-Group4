# EMSC4033-2022-Assignment
The repository provides guides and examples to produce maps which include visual information regarding water features, earthquakes and seafloor age. The user has the option to define the extent of the map, the types of water features and the minimum earthquake magnitude that will be projected on the map. 

**Map Details**

Each folder in the repository uses the python package 'Cartopy' to process geospatial data and produce maps. On the MapMaker notebook, the user begins by specifying the coordinate extent that defines the desired map boundaries (Examples show the San Francisco region). Different folders also offer different map tile generators (basemaps) that the user can select to form the foundation of the map. 

**Water Features**

The user specifies which water features and the resolution they wish to include on the map. Water features available include rivers, lakes and oceans, whereas resolutions can be selected from '10m', '50m' and '110m'.  

**Earthquake Data**

A minimum magnitude is defined by the user and only earthquakes with a magnitude equal or larger than the minimum magnitude will be shown on the map. The function collates events from 1 January 1975 to 1 January 2022 and within the geographical confines established previously. 

The relevant functions will ultimately return an array of arrays containing earthquake longitudes, latitudes, depths and magnitudes. 

**Seafloor Age Data**

Seafloor age and associated coordinates are collected from Earthbyters and recorded in a matrix. The matrix form the rasters of data used to project contours of seafloor age on the maps. 

**Final Map**

The map will display the selected basemap overprinted by the seafloor age contours and earthquake point data colour-coded by depth.
