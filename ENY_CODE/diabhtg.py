# sums up the local derivatives of theta wrt. dx, dy, dt= [from file] seconds, 
# ..to get total derivative Dtheta/Dt. Then multiply it by 
# Cp*temp/theta to get the total diabatic heating 
# rate per unit mass of air.

import xarray as xr
import numpy as np

from theta import theta as theta_func

def diabhtg(path: str, storm: str, **kwargs) -> np.ndarray:
    """calculates total diabatic heating rate per unit mass of air."""

    file = xr.open_dataset(path+storm+storm[5:-1]+'.nc')
    lev = (np.array(file.level)*100) #hpa to +--> pa
    time = file.time
    print(r'variable dimensions are in order (time, level, latitude, longitude)')
    print('dimension lengths:',*list(map(
        len, [file.time, file.level, file.latitude, file.longitude ])))
        
    #***************************************
    # u*del_theta/del_dx + v*del_theta/del_dy

    # constants
    dy =  27750  # 0.25 degree = 27750 meters 
    dx = 27750 # 
    #variable
    
    u = np.array(file.u)
    v = np.array(file.v)
    theta = theta_func(path, storm)

    thetadx = np.gradient(theta, dx , axis= -1)
    thetady = np.gradient(theta, dy, axis= -2)
    delx = u*thetadx
    dely = v*thetady

    # delxdelysum
    delsum = delx + dely
    
    print('u[5,5,5,5]:',u[5,5,5,5])
    print('v[5,5,5,5]:',v[5,5,5,5])
    print('theta[5,5,5,5]:',theta[5,5,5,5])
    print('delx[5,5,5,1]: ',delx[5,5,5,1])
    print('dely[5,5,5,1]: ',dely[5,5,5,1])
    print('delsum[5,5,5,1]: ',delsum[5,5,5,1])
    #**************************************
    # del_theta/del_dt

    # constants
    dt =float( (time[1]-time[0])/1e9  ) # from nano second to second
    thetadt = np.gradient(theta, dt, axis= 0)
    
    print(r'dt = '+f'{dt}'+ 'seconds')
    print('theta[5,5,5,5]:',theta[5,5,5,5])
    print('thedt[5,5,5,5]:',thetadt[5,5,5,5])

    #***************************************
    # omg * del_theta/del_dp

    #variable
    omg = np.array(file.w)# omega
    
    thetadp = np.gradient(theta, lev, axis= 1)
    last = omg*thetadp

    print('omg[5,5,5,5]:',omg[5,5,5,5])
    print('theta[5,5,5,5]:',theta[5,5,5,5])
    print('last[5,5,5,1]: ',last[5,5,5,1])

    #***************************************
    ## Dtheta/Dt

    #constants
    cp = 1004.5
    #variable
    t = np.array(file.t)
    
    dthetadt = thetadt + delsum + last
    tdh = (dthetadt*cp*t)/theta

    print('tdh[5,5,5,1]: ',tdh[5,5,5,1] )
    print('************this_code_ended************' , '|', sep='\n')

    return tdh
    
