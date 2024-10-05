# ekebdyterm2
# calculates the second term in the expression
# .. for boundary flux of eddy pe

import xarray as xr
import numpy as np
import math


def epeb2(path: str, storm: str, **kwargs) -> np.ndarray:
    """calculates term #2/3 for boundary pressure work done by eddies""" 
    
    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    lat = np.array(file.latitude)
    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constant
    g = 9.8
    a = 6378100 # earth radius in meter
    dphi = math.radians(abs(lat[0]-lat[-1]) ) 
    # ylength is N-S distance of the domain in meters.  
    ylength = a*dphi

    # variables
    v = np.array(file.v)
    fy = np.array(file.z)  # geopotential

    vbar = np.mean(v, axis= -1)
    vprime = v[:,:,:,:] - vbar[:,:,:,None]

    fybar = np.mean(fy, axis= -1)
    fyprime = fy[:,:,:,:] - fybar[:,:,:,None]

    vprimetimesfyprime = vprime*fyprime
    vprimetimesfyprimey1 = vprimetimesfyprime[:,:,0,:]
    vprimetimesfyprimey2 = vprimetimesfyprime[:,:,-1,:]
    vprimetimesfyprimeavy1 = np.mean(vprimetimesfyprimey1, axis= -1)
    vprimetimesfyprimeavy2 = np.mean(vprimetimesfyprimey2, axis= -1)
    term = (vprimetimesfyprimeavy1-vprimetimesfyprimeavy2)/(g*ylength)

    #intgrating y=f(x)=term(lev), [x]=[lev], dx=5000 pa
    eddypebdyterm2 = np.trapz(term, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eddypebdyterm2.txt', eddypebdyterm2)
    eddypebdyterm2av = np.mean(eddypebdyterm2, axis= -1)
    
    

    print('ylength: ', ylength)
    print('vbar[5,5,1]: ',vbar[5,5,1])
    print('vprime[5,5,5,1]: ',vprime[5,5,5,1])
    print('fybar[5,5,1]: ',fybar[5,5,1])
    print('fyprime[5,5,5,1]: ',fyprime[5,5,5,1])
    print('term_shape: ', term.shape)
    print('eddypebdyterm2av:', eddypebdyterm2av)

    print('************this_code_ended************' , '|', sep='\n')
    return eddypebdyterm2


