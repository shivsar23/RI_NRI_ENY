#kebtermssum
# sums the three KEB boundary flux terms
# keb1+keb2+keb3

import numpy as np
import xarray as xr

from keb1 import keb1
from keb2 import keb2
from keb3 import keb3

def kebtermssum(path:str, storm:str, openmode:str= False, **kwargs) -> float:
    """calculates boundary flux of KE-eddy"""

    eddykebdyterm11 = keb1(path, storm)
    eddykebdyterm22 = keb2(path, storm)
    eddykebdyterm33 = keb3(path, storm)
    kebsum = eddykebdyterm11 + eddykebdyterm22 + eddykebdyterm33
    np.savetxt(path+storm+'kebsum.txt', kebsum)
    kebsumav = np.mean(kebsum, axis= -1)
    print('kebsumav:', kebsumav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'kebsumav: {kebsumav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
      


    print('************this_code_ended************' , '|', sep='\n')
    return kebsumav

