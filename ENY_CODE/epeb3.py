# ekebdyterm3
# calculates the third term in the expression 
# ..for boundary flux of eddy pe


import xarray as xr
import numpy as np
import math


def epeb3(path:str, storm:str, **kwargs) -> 'array':
    """calculates term #3/3 for boundary pressure work done by eddies"""
    
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
    fy = np.array(file.z)  # geopotential

    omgbar = np.mean(omg, axis= -1)
    omgprime = omg[:,:,:,:] - omgbar[:,:,:,None] 

    fybar = np.mean(fy, axis= -1)
    fyprime = fy[:,:,:,:] - fybar[:,:,:,None]
    
    omgprimetimesfyprime = omgprime*fyprime
    omgprimetimesfyprimebar = np.mean(omgprimetimesfyprime, axis= -1)
    term = omgprimetimesfyprimebar/g
    termarav = np.mean(term, axis= -1)
    eddypebdyterm3 = termarav[:,0] - termarav[:,-1] 

    np.savetxt(path+storm+'eddypebdyterm3.txt', eddypebdyterm3)
    eddypebdyterm3av = np.mean(eddypebdyterm3, axis= -1)
    

    print('omgbar[5,5,1]: ',omgbar[5,5,1])
    print('omgprime[5,5,5,1]: ',omgprime[5,5,5,1])
    print('fybar[5,5,1]: ',fybar[5,5,1])
    print('fyprime[5,5,5,1]: ',fyprime[5,5,5,1])
    print('eddypebdyterm3_shape: ', eddypebdyterm3.shape)
    print('eddypebdyterm3av:', eddypebdyterm3av)

    print('************this_code_ended************' , '|', sep='\n')
    return eddypebdyterm3
    

