import pytest
from src.functions import *


def test_my_water_features(rtol = 1.e-13):
    result = len(my_water_features('50m')) - 3
    assert result < rtol, " *** at least one water feature is omitted "

    
lat0 =  30  ; lat1 = 40
lon0 =  -123; lon1 = -113

map_extent = [lon0, lon1, lat0, lat1]
                 
    
def test_eq_coord():
    eq = download_point_data(map_extent, 5)
    for i in range(len(eq)):
        assert map_extent[0] <= eq[i][0] <= map_extent[1], " *** earthquake longitude out of map extent "
        assert map_extent[2] <= eq[i][1] <= map_extent[3], " *** earthquake latitude out of map extent "
        

def test_eq_mag():
    eq = download_point_data(map_extent, 5)
    for i in range(len(eq)):
        assert eq[i][3] >= 5, " *** magnitude is below the requested minimum "
    
