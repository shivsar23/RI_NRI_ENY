# zke2eke2
# calculates the second term (of four) 
# ..in the conversion of ZKE to EKE  

import xarray as xr
import numpy as np

def zke2eke2(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #2/4 for conversion of KE-zonal to KE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)

    #constants
    g = 9.8

    #variable
    u = np.array(file.u)
    omg = np.array(file.w)  #omega

    ubar = np.mean(u, axis= -1)
    omgbar = np.mean(omg, axis= -1)

    uprime = u[:,:,:,:]- ubar[:,:,:,None]
    omgprime = omg[:,:,:,:] - omgbar[:,:,:,None]
    dudp = np.gradient(ubar, lev, axis= 1)
    upromgprbar = np.mean((uprime*omgprime), axis= -1)

    upromgprbardudp = upromgprbar*dudp
    term = -(upromgprbardudp)/g
    
    termarav = np.mean(term, axis= -1) # return this
    
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zke2eke2 = np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'zke2eke2.txt', zke2eke2)

    zke2eke2av = np.mean(zke2eke2, axis= -1)
    
    print('omgbar[5,5,1] :', omgbar[5,5,1])
    print('dudp[5,5,1]: ', dudp[5,5,1])
    print('term[5,5,1] :', term[5,5,1])
    print('termarav_shape :', termarav.shape)
    print('termarav[5,5]',termarav[5,5])
    print('zke2eke2av:', zke2eke2av)

    print('************this_code_ended************' , '|', sep='\n')
    return termarav


