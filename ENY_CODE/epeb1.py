# epeb1
# calculates the first term in the expression
# ...for boundary flux of eddy pe

import xarray as xr
import numpy as np
import math


def epeb1(path: str, storm: str, **kwargs) -> np.ndarray:
    """calculates term #1/3 for boundary pressure work done by eddies"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    lon = np.array(file.longitude)
    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constant
    g = 9.8
    a = 6378100 # earth radius in meter
    phi = 0.4101 # latitude for tropic of cancer 23.5 dgree
    dlembda = math.radians(abs(lon[0]-lon[-1]) ) 
    # xlenght is E-W distance of the domain in meters.  
    xlength = a*math.cos(phi)*dlembda

    # variables
    u = np.array(file.u)
    fy = np.array(file.z)  # geopotential

    ubar = np.mean(u, axis= -1)
    uprime = u[:,:,:,:] - ubar[:,:,:,None]  
    fybar = np.mean(fy, axis= -1)
    fyprime = fy[:,:,:,:]  - fybar[:,:,:,None]  

    uprimetimesfyprime = uprime*fyprime
    uprimetimesfyprimex1 = uprimetimesfyprime[:,:,:,0]
    uprimetimesfyprimex2 = uprimetimesfyprime[:,:,:,-1]
    uprimetimesfyprimeavx1 = np.mean(uprimetimesfyprimex1, axis= -1)
    uprimetimesfyprimeavx2 = np.mean(uprimetimesfyprimex2, axis= -1)
    term = (uprimetimesfyprimeavx1-uprimetimesfyprimeavx2)/(g*xlength)

    #intgrating y=f(x)=term(lev), [x]=[lev], dx=5000 pa
    eddypebdyterm1 = np.trapz(term, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eddypebdyterm1.txt', eddypebdyterm1)
    eddypebdyterm1av = np.mean(eddypebdyterm1, axis= -1)
    
    print('xlength: ', xlength)
    print('ubar[5,5,1]: ',ubar[5,5,1])
    print('uprime[5,5,5,1]: ',uprime[5,5,5,1])
    print('fybar[5,5,1]: ',fybar[5,5,1])
    print('fyprime[5,5,5,1]: ',fyprime[5,5,5,1])
    print('term_shape: ', term.shape)
    print('eddypebdyterm1av:', eddypebdyterm1av)


    print('************this_code_ended************' , '|', sep='\n')
    return eddypebdyterm1


