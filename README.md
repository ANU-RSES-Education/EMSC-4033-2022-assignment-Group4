# EMSC4033-2022-Assignment
The repository provides guides and examples to produce maps which include visual information regarding water features, earthquakes and seafloor age. The user has the option to define the extent of the map, the types of water features and the minimum earthquake magnitude that will be projected on the map. 

# Guide to access the repository
To anyone who clicks in and wants to make a map, welcome! The contents of this repository are there to help you make a simple geological map.
Once you open the repository, you should see the first three folders with the names of our group members. By clicking into one of the name folders, you can access the individual notebook each of us wrote to create a map.
All three name folders have the same configuration. 

**src folder**

Inside a name folder, the first folder called src is a source folder with functions we wrote to create a map step by step. Inside the src folder, click on the my_functions file, and you can read through how these functions contribute to the map-making and our intentions behind them. We have brief docstrings and comments there available to make the codes easy to follow. The depends file has all dependencies we imported to make the notebook run.

**tests folder**

Let’s move back to the name folder, you would see the second folder inside called tests. You can open the tests folder to access a file called test_functions.py to see how we manage to test our functions to make sure these functions work as we expected. They are prominently pytest based.

**MapMaker.ipynb and RunTests. ipynb files**

To actually run the mapmaker and the corresponding tests, go back to the name folder again and open the third and fourth files called MapMaker.ipynb and RunTests. ipynb respectively. Simply run the whole block of codes and you can have a map on hand.

To know more details about the MapMaker file and how it works, please read carefully the following MapMaker Guide. Copy this repository on your device, run it, test it out and have fun with it.

# MapMaker Guide

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
