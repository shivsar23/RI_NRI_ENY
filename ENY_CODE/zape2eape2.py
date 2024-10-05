# zape2eape2
# calculates the conversion of zonal available potential energy
# ..to eddy available potential energy (second term)


import xarray as xr
import numpy as np

def zape2eape2(path :str, storm:str, **kwargs) -> np.ndarray:
    """calculates term #2/2 for conversion of APE-zonal to APE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constants
    dy =  27750  # 0.25 degree = 27750 meters 

    #variable
    omg = np.array(file.w)# vertical pressure velocity
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt')



    omgbar = np.mean(omg, axis= -1)
    tbar = np.mean(t, axis= -1)
    tdomav = np.mean(tbar, axis= -1)
    tstar = tbar[:,:,:] - tdomav[:,:,None]

    omgprime = omg[:,:,:,:] - omgbar[:,:,:,None]
    tprime = t[:,:,:,:] - tbar[:,:,:,None]
    dtdp = np.gradient(tstar, lev, axis= 1)

    omgprtprbar = np.mean(omgprime*tprime, axis= -1)

    term = -(omgprtprbar*dtdp)
    term = term[:,:,:]/statstab[:,:,None]

    termarav = np.mean(term, axis= -1)
    
    #intgrating y=f(x)=termarav(lev), [x]=[lev], dx=5000 pa
    zape2eape2 = np.trapz(termarav, x=lev, dx=5000, axis= -1)

    np.savetxt(path+storm+'zape2eape2.txt', zape2eape2)

    zape2eape2av = np.mean(zape2eape2, axis= -1)
    
    print('omg[5,5,5,5]:',omg[5,5,5,5])
    print('t[5,5,5,5]:',t[5,5,5,5])
    print('omgbar[5,5,1]: ',omgbar[5,5,1])
    print('tbar[5,5,1]: ',tbar[5,5,1])
    print('tstar[5,5,:5]: ',tstar[5,5,:5])
    print("omgpr[5,5,5,:5]" ,omgprime[5,5,5,:5])
    print('tpr[5,5,5,:5]',tprime[5,5,5,:5])
    print('dtdp[5,5,:5]' ,dtdp[5,5,:5])     
    print('omgprtprbar[5,5,:5]', omgprtprbar[5,5,:5])
    print('term[5,5,:4]',term[5,5,:4])
    print('termarav_shape',termarav.shape)
    print('zape2eape2av:', zape2eape2av)

    print('************this_code_ended************' , '|', sep='\n')
    return zape2eape2

