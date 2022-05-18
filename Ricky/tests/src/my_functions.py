"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""

from .dependencies import *

def my_documentation():

    markdown_documentation = """   
# This notebook shows a simple procedure for making a map with geological features including water features, global seismicity (as point data) and seafloor ages (as raster data).

"""
    
    return markdown_documentation


#Add the coastlines feature using cartopy
#Here I define a function using cfeature.NaturalEarthFeature()
#To use this function, input one of resolutions, 10m, 50m and 110m.
def my_coastlines(resolution):
    """ returns the relevant coastlines at the requested resolution """

    import cartopy.feature as cfeature

    return cfeature.NaturalEarthFeature('physical', 'coastline', resolution,
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor="none")

#Here I want to make a list of water features including lakes, rivers and the ocean.
#Using the cfeature.NaturalEarthFeature() again
def my_water_features(resolution, lakes=True, rivers=True, ocean=True):
    """Returns a [list] of cartopy features"""
    
    features = []
    
    lakes= cfeature.NaturalEarthFeature('physical', 'lakes', resolution,
                                        edgecolor="yellow",
                                        facecolor="none")
    
    rivers= cfeature.NaturalEarthFeature('physical', 'rivers', resolution,
                                        edgecolor= "green",
                                        facecolor="none")
    
    ocean= cfeature.NaturalEarthFeature('physical', 'ocean', resolution,
                                        edgecolor="purple",
                                        facecolor="none")
    if lakes == True:
        features.append(lakes)
    
    if rivers == True:
        features.append(rivers)

    if ocean == True:
        features.append(ocean)
    
    return features

#Create a dictionary of map tile generators that cartopy can use with the token provided
def my_basemaps():
    """Returns a dictionary of map tile generators that cartopy can use"""
    
    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py

    # dictionary of possible basemap tile objects
    
    mapper = {}
    ## Open Street Map
    mapper["open_street_map"] = cimgt.OSM()  
    
    ## Open mapbox_outdooor
    mapper["mapbox_outdoors"] = cimgt.MapboxTiles(map_id='outdoors-v11', access_token='pk.eyJ1IjoibG91aXNtb3Jlc2kiLCJhIjoiY2pzeG1mZzFqMG5sZDQ0czF5YzY1NmZ4cSJ9.lpsUzmLasydBlS0IOqe5JA')

    return mapper



## specify some point data (e.g. global seismicity in this case) (e.g. from 1999_01_01 to 2022_01_01 with minimum magnitude of 5.)

def download_point_data(region):
    
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")

    starttime = UTCDateTime("1999-01-01")
    endtime   = UTCDateTime("2022-01-01")
    
    cat = client.get_events(starttime=starttime, endtime=endtime, minmagnitude=5,
                            catalog="ISC")

    print ("Point data: {} events in catalogue".format(cat.count()))
    
    # Unpack the obspy data into a plottable array

    event_count = cat.count()

    eq_origins = np.zeros((event_count, 5))


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
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "Resources/global_age_data.3.6.z.npz")

    datasize = (1801, 3601, 3)
    raster = np.empty(datasize)

    ages = np.load("Resources/global_age_data.3.6.z.npz")["ageData"]

    lats = np.linspace(90, -90, datasize[0])
    lons = np.linspace(-180.0,180.0, datasize[1])

    arrlons,arrlats = np.meshgrid(lons, lats)

    raster[...,0] = arrlons[...]
    raster[...,1] = arrlats[...]
    raster[...,2] = ages[...]
    

    return raster


def my_global_raster_data():

    raster = download_raster_data()
    
    return raster
