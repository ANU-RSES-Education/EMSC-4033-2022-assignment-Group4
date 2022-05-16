# a random placeholder function to be replaced with
# actual functional functions :)

def foo_function(x):
    return x**2


def my_coastlines(res):
    """ 
    Returns relevant coastlines at the requested resolution.
    """

    import cartopy.feature as cfeature

    return cfeature.NaturalEarthFeature('physical', 'coastline', res,
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor="none")


def my_water_features(res, lakes=True, rivers=True, ocean=True):
    """
    Returns a [list] of cartopy features at the requested resolution.
    """
    import cartopy.feature as cfeature
    
    features = []
    
    if rivers:
        features.append(cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', res, 
                                                     edgecolor='Blue', facecolor="none"))
        
    if lakes:
        features.append(cfeature.NaturalEarthFeature('physical', 'lakes', res,
                                                     edgecolor="blue", facecolor="blue"))

    if ocean:
        features.append(cfeature.NaturalEarthFeature('physical', 'ocean', res,
                                                     edgecolor="green", facecolor="blue"))
    
    return features


def download_point_data(region, minmag):
    '''
    Returns an array of arrays that contains obspy earthquake data (longitude, latitude, depth and magnitude) from the ISC catalogue occurring between 1 Jan 1975 and 1 Jan 2022.
    The user defines the map extent that the data will include. 
    '''
    
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime
    
    import numpy as np

    client = Client("IRIS")

    extent = region

    # Specify time range and minimum magnitude
    
    starttime = UTCDateTime("1975-01-01")
    endtime   = UTCDateTime("2022-01-01")
    
    cat = client.get_events(starttime = starttime,
                            endtime = endtime,
                            minlatitude=extent[2],
                            maxlatitude=extent[3],
                            minlongitude=extent[0],
                            maxlongitude=extent[1],
                            minmagnitude = minmag,
                            catalog = "ISC"
                           )

    print ("Point data: {} events in catalogue".format(cat.count()))
    
    # Present obspy data into a plottable array

    event_count = cat.count()

    eq_origins = np.zeros((event_count, 4))

    for i in range(event_count):
        lon = cat[i].preferred_origin()['longitude']
        lat = cat[i].preferred_origin()['latitude']
        z = cat[i].preferred_origin()['depth']
        mag = cat[i].preferred_magnitude().mag

        eq_origins[i][0] = lon
        eq_origins[i][1] = lat
        eq_origins[i][2] = z
        eq_origins[i][3] = mag

    return eq_origins


def download_raster_data():
    """
    Returns a matrix containing coordinate and seafloor age data from Earthbyters. 
    """

    from cloudstor import cloudstor
    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "Resources/global_age_data.3.6.z.npz")

    # Create empty matrix
    
    datasize = (1801, 3601, 3)
    raster_data = np.empty(datasize)   
    
    # Include coordinate and age data into matrix
    
    age_data = np.load("Resources/global_age_data.3.6.z.npz")["ageData"]

    lat = np.linspace(90, -90, datasize[0])
    lon = np.linspace(-180.0,180.0, datasize[1])

    arrlon,arrlat = np.meshgrid(lon, lat) 

    raster_data[...,0] = arrlon[...]
    raster_data[...,1] = arrlat[...]
    raster_data[...,2] = age_data[...]

    return raster_data

