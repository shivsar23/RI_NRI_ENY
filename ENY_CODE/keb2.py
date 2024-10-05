# ekebdyterm2
# calculates the second term in the expression
# .. for boundary flux of eddy ke.

import xarray as xr
import numpy as np
import math


def keb2(path:str, storm:str, **kwargs) -> np.ndarray: 
    """calculates term #2/3 for boundary flux of KE-eddy"""

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
    u = np.array(file.u)
    v = np.array(file.v)

    ubar = np.mean(u, axis= -1)
    uprime = u[:,:,:,:] - ubar[:,:,:,None]

    vbar = np.mean(v, axis= -1)
    vprime = v[:,:,:,:] - vbar[:,:,:,None]
    
    vtimesuprsqplusvprsq = v*(uprime*uprime + vprime*vprime)
    vtimesuprsqplusvprsqy1 = vtimesuprsqplusvprsq[:,:,0,:]
    vtimesuprsqplusvprsqy2 = vtimesuprsqplusvprsq[:,:,-1,:]

    vtimesuprsqplusvprsqavy1 = np.mean(vtimesuprsqplusvprsqy1, axis= -1)
    vtimesuprsqplusvprsqavy2 = np.mean(vtimesuprsqplusvprsqy2, axis= -1)
    term = (vtimesuprsqplusvprsqavy1 - vtimesuprsqplusvprsqavy2)/(2*g*ylength)

    #intgrating y=f(x)=term(lev), [x]=[lev], dx=5000 pa
    eddykebdyterm2 = np.trapz(term, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eddykebdyterm2.txt', eddykebdyterm2)

    eddykebdyterm2av = np.mean(eddykebdyterm2, axis= -1)
    
    print('ylength: ', ylength)
    print('ubar[5,5,1]: ',ubar[5,5,1])
    print('uprime[5,5,5,1]: ',vprime[5,5,5,1])
    print('vbar[5,5,1]: ',vbar[5,5,1])
    print('vprime[5,5,5,1]: ',vprime[5,5,5,1])
    print('vtimesuprsqplusvprsqy2_shape: ', vtimesuprsqplusvprsqy2.shape)
    print('eddykebdyterm2av:', eddykebdyterm2av)

    print('************this_code_ended************' , '|', sep='\n')
    return eddykebdyterm2


