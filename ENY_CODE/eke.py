# eke

import xarray as xr
import numpy as np

def eke(path: str, storm: str, openmode:str= False, **kwargs) -> float: 
    """calculates KE-eddy """

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)

    #constants
    g = 9.8

    #variable
    u = np.array(file.u)#
    v = np.array(file.v)

    ubar = np.mean(u, axis= -1)
    vbar = np.mean(v, axis= -1)
    uprime = u[:,:,:,:] - ubar[:,:,:,None]
    vprime = v[:,:,:,:] - vbar[:,:,:,None]


    uprsqvprsqsum = uprime**2 + vprime**2
    uprsqvprsqbar = np.mean(uprsqvprsqsum, axis= -1)
    term = uprsqvprsqbar/(2*g)

    termarav = np.mean(term, axis= -1)

    np.savetxt(path+storm+'vertical_eke.txt', termarav) # energy per 5000 hpa
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    eke= np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'eke.txt', eke)
    ekeav = np.mean(eke, axis= -1)
    
    print('term[5,5,1] : ', term[5,5,1])
    print('termarav',termarav.shape)
    print('termarav[5,5]: ', termarav[5,5])
    print('ekeav:', ekeav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'ekeav: {ekeav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')

    print('************this_code_ended************' , '|', sep='\n')

    return ekeav

