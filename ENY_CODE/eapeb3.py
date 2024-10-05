# eapeb3
# calculates the third term in the expression for
# ..boundary flux of eddy ape

import xarray as xr
import numpy as np
import math 


def eapeb3(path: str, storm: str, **kwargs) -> np.ndarray:
    """calculates term #3/3 for boundary flux of APE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    lon = np.array(file.longitude)

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constant
    g = 9.8
    # variables
    omg = np.array(file.w)# omega
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt')

    tbar = np.mean(t, axis= -1)
    tprime = t[:,:,:,:] - tbar[:,:,:,None]

    omgtprimesq = omg*tprime*tprime
    omgtprimesqbar = np.mean(omgtprimesq, axis= -1)
    omgtprimesqbarav = np.mean(omgtprimesqbar, axis=-1)
    term = omgtprimesqbarav/(2*statstab)
    eddyapebdyterm3 = term[:,0] - term[:,-1]

    np.savetxt(path+storm+'eddyapebdyterm3.txt', eddyapebdyterm3)
    eddyapebdyterm3av = np.mean(eddyapebdyterm3, axis= -1)
    
    print('tbar[5,5,1]: ',tbar[5,5,1])
    print('tprime[5,5,5,1]: ',tprime[5,5,5,1])
    print('eddyapebdyterm3_shape: ', eddyapebdyterm3.shape)
    print('eddyapebdyterm3av:', eddyapebdyterm3av)

    print('************this_code_ended************' , '|', sep='\n')

    return eddyapebdyterm3


