import pytest
from src.functions import *
from src.my_functions import *

#My cosatlines
#Example given    
def test_my_coastlines():
    coastline= my_coastlines("50m")
    assert True, " *** Error!"


#My water feature
# At least, it should be a list...
def test_my_water_features():
    my_water_features("50m")
    assert type(my_water_features("50m"))== list, " *** Error, not even a list!"

def test_my_water_features():
    assert my_water_features("50m", lakes=False, rivers=False, ocean=False) == [], " *** Error! Not an empty list"
    
#The elements in this list should be between 0-3. (counting rivers, lakes and the ocean)
def test_my_water_features():
    assert 0<=len(my_water_features("50m"))<= 3, " *** Error, element number incorrect!"

#my basemaps
#It should be a dict that is not empty
def test_my_basemaps():
    assert type(my_basemaps())== dict and my_basemaps != {}, " *** Error, not a dict or a empty dict" 

#Download 
#This can be shown by the plottable array printed 

#my_point_data
#These data should be in a numpy array
def test_my_point_data():
    lat0 =  30  ; lat1 = 40
    lon0 =  -123; lon1 = -113
    map_extent = [lon0, lon1, lat0, lat1]
    assert type(my_point_data(map_extent))== np.ndarray, " *** Error, function type does not belong to <class 'numpy.ndarray'>" 

#my global raster data
#again, the data is printed in the MapMarker, I just want to make sure the integrity of the file and hope no datas are missing.
def test_my_global_raster_data():
    assert np.shape(my_global_raster_data())== (1801, 3601, 3)," *** Error! The datasize is not correct"
    
    
    
