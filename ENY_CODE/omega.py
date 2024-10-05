# omega :vertical pressure velocity
# from vertical velocity (meter per second) to pascals per second

import xarray as xr
import numpy as np


def omega(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates vertical pressure velocity ( Pa/s) from vertical velocity (m/s)"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    #time = np.array(file.time)
    lev = (np.array(file.level)*100) #hpa to +--> pa
    #lat = np.array(file.latitud)


    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)
    #ntime = len(time)
    #nlat = len(lat)

    #constants
    g = 9.8
    r = 287
    #variable
    t = np.array(file.t)#
    w = np.array(file.w) # in m/s

    den = lev[None, :, None, None]/(r*t[:,:,:,:])
    omega = -(den*g*w)

    print('w[5,5,5,1]: ',w[5,5,5,1])
    print('omega[5,5,5,1]:',omega[5,5,5,1])
    np.save(path+storm+'omega.npy',omega) #saving in NumPy .npy format

    print('************this_code_ended************' , '|', sep='\n')

    return omega



