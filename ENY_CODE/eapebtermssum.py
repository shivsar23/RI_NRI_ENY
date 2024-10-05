# eapebtermssum
# This program sums the three EAPE boundary flux terms
# ..eapeb1+eapeb2+eapeb3

import numpy as np
import xarray as xr



from eapeb1 import eapeb1
from eapeb2 import eapeb2
from eapeb3 import eapeb3

def eapebtermssum(path: str, storm: str, openmode:str=False, **kwargs) -> float:
    """calculates boundary flux of APE-eddy"""

    eddyapebdyterm11 = eapeb1(path, storm)
    eddyapebdyterm22 = eapeb2(path, storm)
    eddyapebdyterm33 = eapeb3(path, storm)

    eapebsum = eddyapebdyterm11 + eddyapebdyterm22 + eddyapebdyterm33
    eapebsumav = np.mean(eapebsum, axis= -1)
    np.savetxt(path+storm+'eapebsum.txt', eapebsum)
    print('eapebsumav:', eapebsumav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'eapebsumav: {eapebsumav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')

    print('************this_code_ended************' , '|', sep='\n')
    return eapebsumav

