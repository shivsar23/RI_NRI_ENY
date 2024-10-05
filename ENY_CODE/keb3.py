# ekebdyterm3
# calculates the third term in the expression
# .. for boundary flux of eddy ke.


import xarray as xr
import numpy as np
import math

def keb3(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #3/3 for boundary flux of KE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constant
    g = 9.8
    a = 6378100 # earth radius in meter

    # variables
    u = np.array(file.u)
    v = np.array(file.v)
    omg = np.array(file.w)# omega

    ubar = np.mean(u, axis= -1)
    uprime = u[:,:,:,:] - ubar[:,:,:,None]

    vbar = np.mean(v, axis= -1)
    vprime = v[:,:,:,:] - vbar[:,:,:,None]
  
    omguprsqvprsqsum = omg*(uprime*uprime + vprime*vprime)
    omguprsqvprsqsumbar = np.mean(omguprsqvprsqsum, axis= -1)
    term = omguprsqvprsqsumbar/(2*g)
    termarav = np.mean(term, axis= -1)

    eddykebdyterm3 = termarav[:,0] - termarav[:,-1]
    np.savetxt(path+storm+'eddykebdyterm3.txt', eddykebdyterm3)

    eddykebdyterm3av = np.mean(eddykebdyterm3, axis= -1) 

    print('ubar[5,5,1]: ',ubar[5,5,1])
    print('uprime[5,5,5,1]: ',uprime[5,5,5,1])
    print('vbar[5,5,1]: ',vbar[5,5,1])
    print('vprime[5,5,5,1]: ',vprime[5,5,5,1])
    print('omg[5,5,5,1]: ',omg[5,5,5,1])
    print('term_shape: ', term.shape)
    print('eddykebdyterm3av:', eddykebdyterm3av)

    print('************this_code_ended************' , '|', sep='\n')

    return eddykebdyterm3


