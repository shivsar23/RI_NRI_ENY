# cktermsum
# sum of zke2eke1+zke2eke2+zke2eke3+zke2eke4
#...sums the four Ck energy conversion terms 
import numpy as np
import xarray as xr

from zke2eke1 import zke2eke1
from zke2eke2 import zke2eke2
from zke2eke3 import zke2eke3
from zke2eke4 import zke2eke4

def cktermmsum (path: str, storm: str, openmode:str= False, **kwargs) -> float:
    """calculates conversion from KE-zonal to KE-eddy"""

    termarav_total = zke2eke1(path, storm)+ zke2eke2(path, storm)+ zke2eke3(path, storm)+ zke2eke4(path, storm)
    np.savetxt(path+storm+'vertical_cksum.txt', termarav_total)
    
    cksum = np.loadtxt(path+storm+'zke2eke1.txt') + np.loadtxt(path+storm+'zke2eke2.txt') + np.loadtxt(path+storm+'zke2eke3.txt') + np.loadtxt(path+storm+'zke2eke4.txt')
    cksumav = np.mean(cksum, axis= -1)


    np.savetxt(path+storm+'cksum.txt', cksum)
    print('cksum[5]:', cksum[5])
    print('cksumav:', cksumav)
    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'cksumav: {cksumav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
    print('************this_code_ended************' , '|', sep='\n')

    return cksumav

