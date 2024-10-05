
# epebtermssum
# This program sums the three EPE boundary flux terms
# ...epeb1+epeb2+epeb3

import numpy as np
import xarray as xr

from epeb1 import epeb1
from epeb2 import epeb2
from epeb3 import epeb3

def epebtermssum(path:str, storm:str, openmode:str =False, **kwargs) -> float:
    """calculates boundary pressure work done by eddies"""

    eddypebdyterm11 = epeb1(path, storm)
    eddypebdyterm22 = epeb2(path, storm)
    eddypebdyterm33 = epeb3(path, storm)

    epebsum = eddypebdyterm11 + eddypebdyterm22 + eddypebdyterm33
    np.savetxt(path+storm+'epebsum.txt', epebsum)

    epebsumav = np.mean(epebsum, axis= -1)
    print('epebsumav:', epebsumav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'epebsumav: {epebsumav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')

    print('************this_code_ended************' , '|', sep='\n')
    return epebsumav

