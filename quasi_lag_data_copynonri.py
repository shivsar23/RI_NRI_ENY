print('^^ Need to conda activate "PY3env" or ignore if satisfied ')
import xarray as xr
import numpy as np
import os.path

path = r'/DISK-0/gokul/ENGY/'
storm_name = 'mandous'
storm = 'dat2/'+storm_name+'_3/'


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

track_data = np.load("/DISK-0/gokul/ENGY/track_nonri.npy",allow_pickle=True)

track = track_data.item().get(storm_name)



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
mydir = path+'dat2/'+storm[5:-1]+'_q/'
if not os.path.isdir(mydir):
    os.mkdir(mydir)
    

print(ds.attrs)
print('len_time_new_data: ',len(ds.time))
ds.to_netcdf(mydir+storm[5:-1]+'_q.nc') # netcdf output
print(mydir+storm[5:-1]+'_q.nc')
print('*****done_!*****')
quit()

