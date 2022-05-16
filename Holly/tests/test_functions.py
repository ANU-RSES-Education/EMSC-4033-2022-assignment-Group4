# Examples from class:

# import pytest
# from src.functions import *

# def test_foo_function(rtol=1.e-13):
#     result = foo_function(4) - 16
#     assert result < rtol, " *** error is too big "
    
# def test_my_coastlines():
#     coastline= my_coastlines("50m")
#     assert True, " *** pass!"

import pytest
from src.my_functions import *
    
def test_my_coastlines():
    """ Testing that function can return coastline at different resolutions """
    coastline_a = my_coastlines("10m")
    coastline_b = my_coastlines("50m")
    coastline_c = my_coastlines("175m")
    assert True
    
    
def test_my_water_features():
    """ Testing that the function can return different combinations of the water features if asked for. This confirms functionality of the parameters within the functions """
    water_features_all = my_water_features('50m', lakes=True, rivers=True, ocean=True)
    water_features_only_lakes = my_water_features('50m', lakes=True, rivers=False, ocean=False)
    water_features_mapmaker_required = my_water_features('50m', lakes=True, rivers=True, ocean=False)
    assert True, "pass!"
