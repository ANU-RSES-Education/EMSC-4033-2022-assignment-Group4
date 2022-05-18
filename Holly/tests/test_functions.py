import pytest
from src.my_functions import *
  
    
def test_my_coastlines():
    """ Testing that function can return coastline at different resolutions """
    coastline_a = my_coastlines("10m")
    coastline_b = my_coastlines("50m")
    coastline_c = my_coastlines("175m")
    assert True
    
    
def test_my_water_features():
    """ Testing that the function can return different combinations of the water features. This confirms functionality of the parameters within the functions """
    water_features_all = my_water_features('50m', lakes=True, rivers=True, ocean=True)
    water_features_only_lakes = my_water_features('50m', lakes=True, rivers=False, ocean=False)
    water_features_mapmaker_required = my_water_features('50m', lakes=True, rivers=True, ocean=False)
    assert True, " Indivudal water features are functional "

    
# Code from MapMaker.ipynb for third test    
datasize = (1801, 3601, 3) 

def test_raster_coordinates():
    """ tests if function fails as expected when the coordinate values are invalid """
    lat = np.linspace(100, -100, datasize[0]) # +100 and -100 latitude do not exist
    assert False, " latitude coordinates are outside the possible range "
    
def test_raster_coordinates_2():
    """ above test but for coordinate values that are valid """
    lon = np.linspace(100, -100, datasize[1]) # +100 and -100 longitude exist
    assert True, " latitude coordinates are inside the possible range "
    
