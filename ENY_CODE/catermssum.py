# catermssum
# sums the two CA energy conversion 
# ...terms zape2eape1 + zape2eape2

import numpy as np
import xarray as xr
from zape2eape1 import zape2eape1
from zape2eape2 import zape2eape2

def catermssum(path: str, storm: str, openmode:str=False, **kwargs) -> float:
    """calculates conversion from APE-zonal to APE-eddy"""
    casum = zape2eape1(path, storm) + zape2eape2(path, storm)
    casumav = np.mean(casum,axis= -1)
    
    print('casum[5]', casum[5])
    np.savetxt(path+storm+'casum.txt', casum)
    print('casumav:', casumav)
    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'casumav: {casumav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
                
    print('************this_code_ended************' , '|', sep='\n')

    return casumav

