"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""

from .dependencies import *

def my_documentation():

    markdown_documentation = """   
# Notebook documentation
    
## my_functions package 

The functions within this package were adapted and elborated on to make the notebook run and produce processed data output for earthquake events from 01/01/1975 to 01/01/2022 (inclusive). To produce a map of these events, code for coastlines, waterfeatures, a basemap, point data and raster data as contours were written and used.

## `Python` documentation

The general set up of the notebook is as follows:

```python
# These indicate comments, found in the notebook and the my_functions.py code file.

print("output")
# Above is an example of calling a function to print the output it has process and produced.
```
"""
    
    return markdown_documentation



def my_coastlines(resolution):
    """ returns the relevant coastlines at the requested resolution """

    import cartopy.feature as cfeature

    return cfeature.NaturalEarthFeature('physical', 'coastline', '10m',
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor="none")

# 10m has been defined in the return function as that is the coastlines resolution the notebook code asks for.

def my_water_features(resolution, lakes=True, rivers=True, ocean=False):
    """Returns a [list] of cartopy features"""
    
    features = []
    
    if rivers:
        features.append('50m')
        
    if lakes:
        features.append('50m')

    if ocean:
        features.append('50m')
    
    return features

# 50m has been defined in the return function as that is the water features resolution the notebook code asks for.

def my_basemaps():
    """Returns a dictionary of map tile generators that cartopy can use"""
    
    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py

    # dictionary of possible basemap tile objects
    
    mapper = {}
    
    ## Open Street map
    mapper["open_street_map"] = cimgt.OSM()
    
    return mapper

## specify some point data (e.g. global seismicity in this case)

def download_point_data(region):
    
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")

    extent = region

    starttime = UTCDateTime("1975-01-01")
    endtime   = UTCDateTime("2022-01-01")    
    
    # Define startime and endtime as parameters in the function. Define more parameters so that get_events doesn't overload and stop running with too many individual points.

    cat = client.get_events(starttime=starttime, endtime=endtime,
                         minlongitude=region[0],
                         maxlongitude=region[1],
                         minlatitude=region[2],
                         maxlatitude=region[3],
                         minmagnitude=5.5, catalog="ISC")

    print ("Point data: {} events in catalogue".format(cat.count()))
    
    # Unpack the obspy data into a plottable array

    event_count = cat.count()

    eq_origins = np.zeros((event_count, 5))

    # Define the output parameters written in the array, specifically longitutde, latitude, depth, magnitude and time of each earthquake event.

    for ev, event in enumerate(cat.events):
        eq_origins[ev,0] = dict(event.origins[0])['longitude']
        eq_origins[ev,1] = dict(event.origins[0])['latitude']
        eq_origins[ev,2] = dict(event.origins[0])['depth']
        eq_origins[ev,3] = dict(event.magnitudes[0])['mag']
        eq_origins[ev,4] = (dict(event.origins[0])['time']).date.year

    return eq_origins


def my_point_data(region):
    
    data = download_point_data(region)
    
    return data


## - Some global raster data (lon, lat, data) global plate age, in this example

def download_raster_data():
    
    # Seafloor age data and global image - data from Earthbyters

    # The data come as ascii lon / lat / age tuples with NaN for no data. 
    # This can be loaded with ...

    # age = numpy.loadtxt("Resources/global_age_data.3.6.xyz")
    # age_data = age.reshape(1801,3601,3)  # I looked at the data and figured out what numbers to use
    # age_img  = age_data[:,:,2]

    # But this is super slow, so I have just stored the Age data on the grid (1801 x 3601) which we can reconstruct easily

    from cloudstor import cloudstor
    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "global_age_data.3.6.z.npz")

    datasize = (1801, 3601, 3)
    raster_data = np.empty(datasize)
    
    # Produce raster cotaining longitutde, latitude and age data.

    raster = np.load("global_age_data.3.6.z.npz")["ageData"]

    lats = np.linspace(90, -90, datasize[0])
    lons = np.linspace(-180.0,180.0, datasize[1])

    arrlons,arrlats = np.meshgrid(lons, lats)

    raster_data[...,0] = arrlons[...]
    raster_data[...,1] = arrlats[...]
    raster_data[...,2] = raster[...]

    return raster_data


def my_global_raster_data():

    raster = download_raster_data()
    
    return raster
