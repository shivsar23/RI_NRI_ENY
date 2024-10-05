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

# provide these !
eye_margin = 5.5
resolution = 0.25

track_data = np.load("/DISK-0/gokul/ENGY/track_nonri.npy",allow_pickle=True)

track = track_data.item().get(storm_name)


print(len(track))



# track np.ndarray of list [lat, long]
track = np.array(list(map(list, track) )  )
#******************

#track coords to nearest 0.25 ndarray of lists
npfunc = np.vectorize(lambda n:round(n*4)/4)
track = npfunc(track)

def track_in_domain(track, dom_lat, dom_long ):
    lat_except = [y for y in track[:,0] if y not in dom_lat]
    long_except = [x for x in track[:,1] if x not in dom_long]
    if lat_except !=[] or long_except !=[]:
        print(f"""these latitudes {lat_except} are not in selected domain
these longitudes {long_except } are not in selected domain """)
        return False
    else:
        return True

min_lat = np.amin(track[:,0])
max_lat = np.amax(track[:,0]) 

min_long = np.amin(track[:,1])
max_long = np.amax(track[:,1]) 

period = '3 hourly' # peroid of track stamps


if 1:
    y_range= np.arange(min_lat-eye_margin, max_lat+eye_margin , resolution)
    x_range= np.arange(min_long-eye_margin, max_long+eye_margin, resolution)

    if not track_in_domain(track, y_range, x_range):
        print('exiting..')
        exit()
 
    if 1:
        if 1:
            u_t = u.sel(latitude=y_range, longitude=x_range )
            v_t = v.sel(latitude=y_range, longitude=x_range )
            w_t = w.sel(latitude=y_range, longitude=x_range )

            t_t = t.sel(latitude=y_range, longitude=x_range )
            z_t = z.sel(latitude=y_range, longitude=x_range )
            q_t = q.sel(latitude=y_range, longitude=x_range )

                                 
    
u_ds= u_t.to_dataset() 
ds= u_ds.assign({'v':v_t, 'w':w_t, 't':t_t, 'z':z_t, 'q':q_t})  # final xr.Dataset

ds.attrs= {'Info': 'contains sliced data for 6 variables acc. to total spatial domain of cyclone from genesis to dissipation',
 'Parent_convention':file.attrs['Conventions'], 'Parent_history': file.attrs['history'],
}
# make new directory for new file at ~/data/
mydir = path+'dat2/'+storm[5:-1]+'_e/'
if not os.path.isdir(mydir):
    os.mkdir(mydir)
    

print(ds.attrs)
print('len_time_new_data: ',len(ds.time))
ds.to_netcdf(mydir+storm[5:-1]+'_e.nc') # netcdf output
print(mydir+storm[5:-1]+'_e.nc')
print('*****done_!*****')
quit()

