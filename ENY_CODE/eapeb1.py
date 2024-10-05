# eapeb1
# calculates the first term in the expression for 
# ..boundary flux of eddy ape

import xarray as xr
import numpy as np
import math 

def eapeb1(path: str, storm: str, **kwargs) -> np.ndarray:
    """calculates term #1/3 for boundary flux of APE-eddy"""

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
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt')

    tbar = np.mean(t, axis= -1)
    tprime = t[:,:,:,:] - tbar[:,:,:,None]

    utimestprimesq = u*tprime*tprime
    utimestprimesqx1 = utimestprimesq[:,:,:,0]
    utimestprimesqx2 = utimestprimesq[:,:,:,-1]
    utimestprimesqavx1 = np.mean(utimestprimesqx1, axis= -1)
    utimestprimesqavx2 = np.mean(utimestprimesqx2, axis= -1)
    term = (utimestprimesqavx1-utimestprimesqavx2)/(2*statstab*xlength)

    #intgrating y=f(x)=term(lev), [x]=[lev], dx=5000 pa
    eddyapebdyterm1 = np.trapz(term, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eddyapebdyterm1.txt', eddyapebdyterm1)
    eddyapebdyterm1av = np.mean(eddyapebdyterm1, axis= -1)
    
    print('xlength: ', xlength)
    print('tbar[5,5,1]: ',tbar[5,5,1])
    print('tprime[5,5,5,1]: ',tprime[5,5,5,1])
    print('term_shape: ', term.shape)
    print('eddyapebdyterm1av:', eddyapebdyterm1av)

    print('************this_code_ended************' , '|', sep='\n')
    return eddyapebdyterm1

