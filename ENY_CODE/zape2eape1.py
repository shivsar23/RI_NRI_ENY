# zape2eape1
# calculates the conversion of zonal available potential energy
# ..to eddy available potential energy (first term)

import xarray as xr
import numpy as np

def zape2eape1(path:str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #1/2 for conversion of APE-zonal to APE-eddy"""
    
    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constants
    dy =  27750  # 0.25 degree = 27750 meters 

    #variable
    v = np.array(file.v)
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt')
    
    vbar = np.mean(v, axis= -1)
    tbar = np.mean(t, axis= -1)

    vprime = v[:,:,:,:] - vbar[:,:,:,None]
    tprime = t[:,:,:,:] - tbar[:,:,:,None]
  
    dtdy = np.gradient(tbar, dy, axis= -1)

    vprtprbar = np.mean(vprime*tprime, axis= -1)
    term = -(vprtprbar*dtdy)
    term = term[:,:,:]/statstab[:,:,None]

    termarav = np.mean(term, axis= -1)

    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zape2eape1 = np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'zape2eape1.txt', zape2eape1)

    zape2eape1av = np.mean(zape2eape1, axis= -1)
    
    print('v[5,5,5,5]:',v[5,5,5,5])
    print('t[5,5,5,5]:',t[5,5,5,5])

    print('vbar[5,5,1]: ',vbar[5,5,1])
    print('tbar[5,5,1]: ',tbar[5,5,1])

    print("vpr[5,5,5,:5]" ,vprime[5,5,5,:5])
    print('tpr[5,5,5,:5]',tprime[5,5,5,:5])
    print('dtdy[5,5,:5]' ,dtdy[5,5,:5])  
    print('term[5,5,:4]',term[5,5,:4])   
    print('termarav_shape',termarav.shape)
    print('zape2eape1av:', zape2eape1av)

    print('************this_code_ended************' , '|', sep='\n')
    return zape2eape1

 
