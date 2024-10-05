print('^^ Need to conda activate "PY3env" or ignore if satisfied ')
import xarray as xr
import numpy as np
import os.path

path = r'/DISK-0/gokul/ENGY/'
storm = 'data/phailin_3/'


file =  xr.open_dataset(path+storm[:-1]+'.nc')

# variable
u= file.u
v= file.v
w= file.w

t= file.t
z= file.z
q= file.q

tim = (np.array(u.time))

# provide these !
delta =6.25  # 7 degree  or 5.25
resolution = 0.25 #degree

track =[(12.0,96.0),(12.0,95.5),(12.0,95),(12.0,94.5),(12.25,94.25),(12.5,94.0),(13.75,93.75),(13.0,93.5),(13.0,93.5),(13.0,93.0),(13.5,92.5),
 (13.5,92.5),(13.6,92.5),(14.0,92.0),(14.0,92.0),(14.5,91.5),(14.5,91.0),(15.0,90.5),(15.0,90.5),
 (15.5,90.0),(15.5,90.0),(15.5,89.5),(15.5,89.0),(16.0,88.5),(16.0,88.5),(16.2,88.3),(16.5,88.0),
 (16.8,87.7),(16.9,87.2),(17.0,87.0),(17.1,86.8),(17.5,86.5),(17.8,86.0),(18.1,85.7),(18.6,85.4),
 (18.7,85.2),(19.1,85.2),(19.5,84.8),(20.0,84.5),(20.5,84.5),(21.0,84.0),(21.5,84.0),(21.8,83.8),
 (22.5,83.8),(22.75,83.65),(23.0,83.5),(23.25,83.75),(23.5,84.0),(24.0,84.1),(24.5,84.2),]





print(len(track))


period = '3 hourly' # peroid of track stamps
print('len_track: ', len(track))

u_t= 10 # control variable

for i,coord in enumerate(track):
    y,x = coord
    print(y,x, coord, i)
    y= round(y*4)/4
    x= round(x*4)/4 # round to nearest to resolution value
    y_range= np.arange(y-delta, y+delta, resolution)
    x_range= np.arange(x-delta, x+delta, resolution)
    if 1:
        if type(u_t) != int:
            u_t= xr.concat([u_t, u.sel(time=tim[i], 
                                 latitude=y_range, longitude=x_range )], dim= 'time', join='override' )
            v_t= xr.concat([v_t, v.sel(time=tim[i], 
                                 latitude=y_range, longitude=x_range )], dim= 'time', join='override' )
            w_t= xr.concat([w_t, w.sel(time=tim[i],
                                 latitude=y_range, longitude=x_range )], dim= 'time', join='override' )

            t_t= xr.concat([t_t, t.sel(time=tim[i], 
                                 latitude=y_range, longitude=x_range )],dim= 'time', join='override' )
            z_t= xr.concat([z_t, z.sel(time=tim[i],
                                 latitude=y_range, longitude=x_range )], dim= 'time', join='override' )
            q_t= xr.concat([q_t, q.sel(time=tim[i],
                                 latitude=y_range, longitude=x_range )], dim= 'time', join='override' )

        else:
            u_t = u.sel(time=tim[i], 
                latitude=y_range, longitude=x_range )
            v_t = v.sel(time=tim[i], 
                latitude=y_range, longitude=x_range )
            w_t = w.sel(time=tim[i],
                latitude=y_range, longitude=x_range )

            t_t = t.sel(time=tim[i], 
                latitude=y_range, longitude=x_range )
            z_t = z.sel(time=tim[i],
                latitude=y_range, longitude=x_range )
            q_t = q.sel(time=tim[i],
                latitude=y_range, longitude=x_range )

    
u_ds= u_t.to_dataset() 
ds= u_ds.assign({'v':v_t, 'w':w_t, 't':t_t, 'z':z_t, 'q':q_t})  # final xr.Dataset

ds.attrs= {
 'Careful': 'The latitude and longitude labels are true for first time step only ie. do not use actual longitude & latitude labels',
 'Track':period+' track (lat, lon) :'+str(track),
 'Method': ' Data contructed by slicing "Normal data" for fixed spatial area centred at storm track at each timestep for each variable for all the pressure levels',
 'Parent_convention':file.attrs['Conventions'], 'Parent_history': file.attrs['history'],
}
# make new directory for new file at ~/data/
mydir = path+'data/'+storm[5:-1]+'_q/'
if not os.path.isdir(mydir):
    os.mkdir(mydir)
    

print(ds.attrs)
print('len_time_new_data: ',len(ds.time))
ds.to_netcdf(mydir+storm[5:-1]+'_q.nc') # netcdf output

print('*****done_!*****')
quit()

