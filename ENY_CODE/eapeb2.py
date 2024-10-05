# eapeb2
# calculates the second term in the expression for
# ..boundary flux of eddy ape


import xarray as xr
import numpy as np
import math 

def eapeb2(path: str, storm: str, **kwargs) -> np.ndarray:
    """calculates term #2/3 for boundary flux of APE-eddy"""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    lat = np.array(file.latitude)

    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))

    # constant
    g = 9.8
    a = 6378100 # earth radius in meter
    dphi = math.radians(abs(lat[0]-lat[-1]) ) 
    # ylength is N-S distance of the domain in meters.  
    ylength = a*dphi

    # variables
    v = np.array(file.v)
    t = np.array(file.t)
    statstab = np.loadtxt(path+storm+'statstab.txt')
    tbar = np.mean(t, axis= -1)
    tprime = t[:,:,:,:] - tbar[:,:,:,None]


    vtimestprimesq = v*tprime*tprime
    vtimestprimesqy1 = vtimestprimesq[:,:,0,:]
    vtimestprimesqy2 = vtimestprimesq[:,:,-1,:]
    vtimestprimesqavy1 = np.mean(vtimestprimesqy1, axis= -1)
    vtimestprimesqavy2 = np.mean(vtimestprimesqy2, axis= -1)
    term = (vtimestprimesqavy1-vtimestprimesqavy2)/(2*statstab*ylength)
	
    #intgrating y=f(x)=term(lev), [x]=[lev], dx=5000 pa
    eddyapebdyterm2 = np.trapz(term, x=lev, dx=5000, axis= -1)
    np.savetxt(path+storm+'eddyapebdyterm2.txt', eddyapebdyterm2)
    eddyapebdyterm2av = np.mean(eddyapebdyterm2, axis= -1)
    
    print('ylength: ', ylength)
    print('tbar[5,5,1]: ',tbar[5,5,1])
    print('tprime[5,5,5,1]: ',tprime[5,5,5,1])
    print('term_shape: ', term.shape)
    print('eddyapebdyterm2av:', eddyapebdyterm2av)

    print('************this_code_ended************' , '|', sep='\n')

    return eddyapebdyterm2

