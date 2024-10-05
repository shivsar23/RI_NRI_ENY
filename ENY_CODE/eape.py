# eape

import xarray as xr
import numpy as np


def eape(path: str, storm: str, openmode:str= False, **kwargs) -> float:
    """calculates APE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa


    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))


    # variables
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt')

    tbar = np.mean(t, axis=-1)
    tprime = t[:,:,:,:] - tbar[:,:,:,None]
    tprtprbar = np.mean(tprime*tprime, axis= -1)

    term = tprtprbar[:,:,:]/(2*statstab[:,:,None])
    termarav = np.mean(term, axis= -1)
    
    np.savetxt(path+storm+'vertical_eape.txt', termarav) # energy per 5000 hpa
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    eape = np.trapz(termarav, x=lev, dx=5000, axis=-1)
    
    np.savetxt(path+storm+'eape.txt' ,eape)

    eapeav = np.mean(eape, axis=-1)
    
    print('tbar[5,5,1]: ',tbar[5,5,1])
    print('tprime[5,5,5,1]: ',tprime[5,5,5,1])
    print('len_zke:',len(eape))
    print('eapeav:', eapeav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'eapeav: {eapeav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')

    print('************this_code_ended************' , '|', sep='\n')

    return eapeav


