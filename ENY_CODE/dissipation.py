# calculates the last term in budget De dissipation term

import numpy as np

def dissipation(path: str, storm: str, openmode:str = False, **kwargs) -> float:
    """calculates KE-eddy dissipation term as a residual quantity from the budget equation."""

    eke = np.loadtxt(path+storm+'eke.txt')
    time = np.loadtxt(path+storm+'time.txt')
    cksum = np.loadtxt(path+storm+'cksum.txt')
    cpk = np.loadtxt(path+storm+'eape2eke.txt')
    kebsum = np.loadtxt(path+storm+'kebsum.txt')
    epebsum = np.loadtxt(path+storm+'epebsum.txt')
    dekedt = np.gradient(eke, time, axis=0)
    
    diss = cksum+cpk+kebsum+epebsum-dekedt # dissipation term
    
    np.savetxt(path+storm+'diss.txt',diss )
    dissav = np.mean(diss, axis=-1)
    
    print('time[:5]:',time[:5])
    print('dekedt[0]:',dekedt[0])
    print('dissav:',dissav)

    if openmode:
        with open(path+storm+storm[5:-1]+'_averages.txt', openmode) as file:
            try:
                file.read()
                file.write(f'dissav: {dissav} \n')
            except :
                print(f'write to {storm[5:-1]}_averages.txt failed')
    print('************this_code_ended************' , '|', sep='\n')

    return dissav

