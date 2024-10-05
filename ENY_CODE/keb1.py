# ekebdyterm1
# calculates the first term in the expression
# ... for boundary flux of eddy ke

import xarray as xr
import numpy as np
import math

def keb1(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #1/3 for boundary flux of KE-eddy"""
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
    v = np.array(file.v)

    ubar = np.mean(u, axis= -1)
    uprime = u[:,:,:,:] - ubar[:,:,:,None]
    vbar = np.mean(v, axis= -1)
    vprime = v[:,:,:,:] - vbar[:,:,:,None]


    utimesuprsqplusvprsq = u*(uprime*uprime + vprime*vprime)
    utimesuprsqplusvprsqx1 = utimesuprsqplusvprsq[:,:,:,0]
    utimesuprsqplusvprsqx2 = utimesuprsqplusvprsq[:,:,:,-1]
    utimesuprsqplusvprsqavx1 = np.mean(utimesuprsqplusvprsqx1, axis= -1)
    utimesuprsqplusvprsqavx2 = np.mean(utimesuprsqplusvprsqx2, axis= -1)
    term = (utimesuprsqplusvprsqavx1 - utimesuprsqplusvprsqavx2)/(2*g*xlength)

    #intgrating y=f(x)=term(lev), [x]=[lev], dx=5000 pa
    eddykebdyterm1 = np.trapz(term, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eddykebdyterm1.txt', eddykebdyterm1)
    eddykebdyterm1av = np.mean(eddykebdyterm1, axis= -1)
    
    print('xlength: ', xlength)
    print('ubar[5,5,1]: ',ubar[5,5,1])
    print('uprime[5,5,5,1]: ',vprime[5,5,5,1])
    print('vbar[5,5,1]: ',vbar[5,5,1])
    print('vprime[5,5,5,1]: ',vprime[5,5,5,1])
    print('eddykebdyterm1av:', eddykebdyterm1av)

    print('************this_code_ended************' , '|', sep='\n')

    return eddykebdyterm1


