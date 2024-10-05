#zke2eke3
# calculates the third term (of four)
# ..in the conversion of ZKE to EKE

import xarray as xr
import numpy as np


def zke2eke3(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #3/4 for conversion of KE-zonal to KE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)

    #constants
    dx = 27750 #27.75km=0.25deg near equator
    dy = 27750
    g = 9.8

    #variable
    v = np.array(file.v)

    vbar = np.mean(v, axis= -1)

    vprime = v[:,:,:,:] - vbar[:,:,:,None]


    vprsq = vprime*vprime
    dvdy = np.gradient(vbar, dy, axis= -1)
    vprsqbar = np.mean(vprsq, axis= -1)
    vprsqbardvdy = vprsqbar*dvdy
    term = -(vprsqbardvdy)/g
        
    termarav = np.mean(term, axis= -1) # return this

    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zke2eke3 = np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'zke2eke3.txt', zke2eke3)

    zke2eke3av = np.mean(zke2eke3, axis= -1)
    
    print('term[5,5,1]: ', term[5,5,1])
    print('termarav',termarav.shape)
    print('termarav[5,5]: ', termarav[5,5])
    print('zke2eke3av:', zke2eke3av)

    print('************this_code_ended************' , '|', sep='\n')
    return termarav


