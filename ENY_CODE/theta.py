# potential temperature , theta

import xarray as xr
import numpy as np


def theta(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates potential temperature"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constants
    p0 = 100000
    cp = 1004.5
    r = 287
    #variable
    t = np.array(file.t)

    theta = (t[:,:,:,:] )*( (p0/lev)**(r/cp))[None, :, None,None]
    
    print('data at :',storm)
    print('t[5,5,5,5]:',t[5,5,5,5])
    print('theta[5,5,5,5]:',theta[5,5,5,5])

    print('************this_code_ended************' , '|', sep='\n')

    return theta

