# zape

import xarray as xr
import numpy as np

def zape(path:str, storm:str, openmode:str= False, **kwargs) ->float:
    """calculates APE-zonal"""
    
    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    statstab = np.loadtxt(path+storm+'statstab.txt')

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # variables
    t = np.array(file.t)
    tbar = np.mean(t, axis=-1)

    tdomav = np.mean(tbar, axis=-1)
    tstar = tbar[:,:,:] - tdomav[:,:,None]


    term = (tstar*tstar)[:,:,:]/(2*statstab[:,:,None])
    termarav = np.mean(term, axis= -1)  

    np.savetxt(path+storm+'vertical_zape.txt', termarav) # energy per 5000 hpa
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zape = np.trapz(termarav, x=lev, dx=5000, axis=-1)
    #saving zape array in zape.txt file

    np.savetxt(path+storm+'zape.txt' ,zape)

    zapeav = np.mean(zape, axis=-1)
    
    print('tbar[5,5,1]: ',tbar[5,5,1])
    print('tstar[5,5,1]: ',tstar[5,5,1])
    print('term[5,5,1]: ',term[5,5,1])    
    print('termarav[5,5]: ',termarav[5,5])
    print('len_zape:',len(zape))
    print('zapeav:', zapeav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'zapeav: {zapeav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')

    print('************this_code_ended************' , '|', sep='\n')

    return zapeav

