# eape2eke
# Cpk

import xarray as xr
import numpy as np

def eape2eke(path: str, storm: str, openmode:str = False, **kwargs) -> float:
    """calculates conversion APE-eddy to KE-eddy."""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    statstab = np.loadtxt(path+storm+'statstab.txt')

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    #constants
    dx = 27750 #27.75km=0.25deg near equator
    dy = 27750
    g = 9.8
    r = 287
    #variable
    t = np.array(file.t)
    omg = np.array(file.w) #omega

    tbar = np.mean(t, axis= -1)
    omgbar = np.mean(omg, axis= -1)

    tprime = t[:,:,:,:] - tbar[:,:,:,None]  
    omgprime = omg[:,:,:,:]- omgbar[:,:,:,None] 
    omgprtpr = omgprime*tprime
    omgprtprbar = np.mean(omgprtpr, axis= -1)
    term = -(omgprtprbar*r)/g
    term = term[:,:,:]/lev[None,:,None]
    termarav = np.mean(term, axis= -1)
    
    np.savetxt(path+storm+'vertical_eape2eke.txt', termarav) # energy conversion per 5000 hpa
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    eape2eke = np.trapz(termarav, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eape2eke.txt', eape2eke)
    eape2ekeav = np.mean(eape2eke, axis= -1)
    
    print('term[5,5,1]:',term[5,5,1])
    print('termarav',termarav.shape)
    print('eape2ekeav:', eape2ekeav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'eape2ekeav: {eape2ekeav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
    print('************this_code_ended************' , '|', sep='\n')

    return eape2ekeav


