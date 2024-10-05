# zke2eke1
# calculates the first term (of four)
# ..in the conversion of ZKE to EKE

import xarray as xr
import numpy as np

def zke2eke1(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #1/4 for conversion of KE-zonal to KE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
   
    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)

    #constants
    dx = 27750 #27.75km=0.25deg near equator
    dy = 27750
    g = 9.8

    #variable
    u = np.array(file.u)
    v = np.array(file.v)

    ubar = np.mean(u, axis= -1)
    vbar = np.mean(v, axis= -1)

    uprime = u[:,:,:,:] - ubar[:,:,:,None]
    vprime = v[:,:,:,:] - vbar[:,:,:,None]
    
    dudy=np.gradient(ubar,dy, axis= -1 )

    uprvprbar = np.mean((uprime*vprime), axis= -1)
    uprvprdudy = uprvprbar*dudy
   
    term = -(uprvprdudy)/g
    termarav = np.mean(term, axis= -1) # return this
    
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zke2eke1 = np.trapz(termarav, x=lev,dx=5000, axis= -1 )

    np.savetxt(path+storm+'zke2eke1.txt', zke2eke1)

    zke2eke1av = np.mean(zke2eke1, axis= -1)
    
    print('dudy[1,5,5]', dudy[1,5,5])
    print(uprvprdudy.shape)
    print('term[5,5,1] :',term[5,5,1])
    print('termarav_shape',termarav.shape)
    print('termarav[5,5]: ', termarav[5,5])    
    print('zke2eke1av:', zke2eke1av) 


    print('************this_code_ended************')
    print('|')

    return termarav

