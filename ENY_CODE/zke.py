#   zke

import xarray as xr
import numpy as np

def zke(path:str, storm:str, openmode:str = False, **kwargs ) ->float:
    """calculates KE-zonal""" 

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    time = np.array(list(map(float,file.time)))/1e9
    np.savetxt(path+storm+'time.txt', time)
    #constant
    g = 9.8

    #variables
    u = np.array(file.u)
    v = np.array(file.v)
    ubar = np.mean(u, axis=-1)
    vbar = np.mean(v, axis=-1)
    term = (ubar**2 + vbar**2)/(2*g)
    termarav = np.mean(term , axis=-1)

    np.savetxt(path+storm+'vertical_zke.txt', termarav) # energy per 5000 hpa
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zke = np.trapz(termarav, dx=5000, axis=-1)
    
    #saving zke array in zke.txt file
    
    np.savetxt(path+storm+'zke.txt' ,zke)
    zkeav = np.average(zke, axis=-1)
    
    print('u[5,5,5,5]:',u[5,5,5,5])
    print('v[5,5,5,5]:',v[5,5,5,5])
    print('ubar.shape', ubar.shape)
    print('ubar[5,5,1]',ubar[5,5,1])
    print('vbar[5,5,1]',vbar[5,5,1])
    print('term[5,5,1]:',term[5,5,1])
    print('termarav[5,5]:',termarav[5,5])
    print('len_zke:',len(zke))    
    print('zkeav:', zkeav)

    if openmode:
        try:
            with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
                file.write(f'zkeav: {zkeav} \n')
        except :
            print(f'write to {storm[5:-1]}_averages.txt failed, file may not exist \n or use "w+" openmode')

    print('************this_code_ended************' , '|', sep='\n')

    return zkeav

