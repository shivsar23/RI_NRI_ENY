#  genape
# calculates the generation of eddy available potential energy by...
#...diabatic heating [Ge]
 

import xarray as xr
import numpy as np
from diabhtg import diabhtg

def geneape(path: str, storm:str, openmode:str = False, **kwargs) -> float:
    """calculates generation of APE-eddy by diabatic heating """

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa


    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))


    #constants
    cp = 1004.5

    #variable
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt') 
    q = diabhtg(path, storm)
    
    tbar = np.mean(t, axis= -1) 
    tprime = t[:,:,:,:] - tbar[:,:,:,None]
    qbar = np.mean(q, axis= -1)
    qprime = q[:,:,:,:] - qbar[:,:,:,None]
 

    tprqprbar = np.mean(tprime*qprime, axis= -1)
    term = tprqprbar[:,:,:]/(cp*statstab[:,:,None])
    termarav = np.mean(term, axis= -1)

    np.savetxt(path+storm+'vertical_geape.txt', termarav) # energy conversion per 5000 hpa
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    geape = np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'geape.txt', geape)

    geapeav = np.mean(geape, axis= -1)

    print('geapeav:', geapeav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'geapeav: {geapeav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
      

    print('************this_code_ended************' , '|', sep='\n')
    return geapeav

