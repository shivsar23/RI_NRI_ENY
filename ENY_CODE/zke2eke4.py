# zke2eke4
# calculates the fourth term (of four)
# ..in the conversion of ZKE to EKE

import xarray as xr
import numpy as np

def zke2eke4(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #4/4 for conversion of KE-zonal to KE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa


    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)

    #constants
    g = 9.8

    #variable
    v = np.array(file.v)
    omg = np.array(file.w)  # omega

    vbar = np.mean(v, axis= -1)
    omgbar = np.mean(omg, axis= -1)

    vprime = v[:,:,:,:] - vbar[:,:,:,None]
    omgprime = omg[:,:,:,:] - omgbar[:,:,:,None]


    dvdp = np.gradient(vbar, lev, axis= 1)
    vpromgpr = vprime*omgprime
    vpromgprbar = np.mean(vpromgpr, axis= -1)
    vpromgprbardvdp = vpromgprbar*dvdp
    term = -(vpromgprbardvdp)/g

    termarav = np.mean(term, axis= -1) # return this

    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zke2eke4 = np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'zke2eke4.txt', zke2eke4)

    zke2eke4av = np.mean(zke2eke4, axis= -1)
    print('term[5,5,1]: ', term[5,5,1])
    print('termarav',termarav.shape)
    print('termarav[5,5] :', termarav[5,5])
    print('zke2eke4av:', zke2eke4av)

    print('************this_code_ended************' , '|', sep='\n')

    return termarav


