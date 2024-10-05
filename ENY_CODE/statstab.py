# statab
# calculates the mean static stability at each level


import xarray as xr
import numpy as np


def statstab(path :str, storm:str, **kwargs) -> np.ndarray:
    """calculates mean static stability"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level))*100 #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    #constants
    r = 287
    g = 9.8
    cp = 1004.5

    # variables
    t = np.array(file.t)
    tbar = np.mean(t, axis= -1)
    tdomav = np.mean(tbar, axis= -1)

    dtaadp = (np.gradient(tdomav, lev, axis= -1))
    statstab = (tdomav*(g/cp))-((lev*g)/r)*dtaadp #pressure already in pa
    
    print('t[5,5,5,5]:',t[5,5,5,5])
    print('tdomav_shape: ', tdomav.shape)
    print('dtaadp[5,1]:', dtaadp[5,1])
    print('statstab[5,1]:',statstab[5,1])

    np.savetxt(path+storm+'statstab.txt', statstab )

    print('************this_code_ended************' , '|', sep='\n')

    return statstab

