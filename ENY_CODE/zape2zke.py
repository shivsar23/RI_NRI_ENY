# zape2zke

import xarray as xr
import numpy as np

def zape2zke( path:str, storm:str, openmode:str = False, **kwargs) -> float:
    """calculates conversion of APE-zonal to KE-zonal"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    


    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    nlev = len(lev)
   

    #constants
    g = 9.8
    r = 287
    #variable
    omg = np.array(file.w)# omega
    t = np.array(file.t)

    omgbar = np.mean(omg, axis= -1)
    tbar = np.mean(t, axis= -1)
    omgdomav = np.mean(omgbar, axis= -1)
    tdomav = np.mean(tbar, axis= -1)

    omgstar = omgbar[:,:,:] - omgdomav[:,:,None]
    tstar = tbar[:,:,:]- tdomav[:,:,None]

    term = -(omgstar*tstar*r)/g
    term = term[:,:,:] /lev[None,:, None]

    termarav = np.mean(term, axis= -1)

    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zape2zke = np.trapz(termarav, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'zape2zke.txt', zape2zke)
    zape2zkeav = np.mean(zape2zke, axis= -1)
    
    print('term[5,5,1] :', term[5,5,1])
    print('termarav_shape',termarav.shape)
    print('termarav[5,5]: ', termarav[5,5])
    print('zape2zkeav:', zape2zkeav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'zape2zkeav: {zape2zkeav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
   

    print('************this_code_ended************' , '|', sep='\n')
    return zape2zkeav

