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

# provide these !
eye_margin = 5.5
resolution = 0.25

track =[(12.0,96.0),(12.0,95.5),(12.0,95),(12.0,94.5),(12.25,94.25),(12.5,94.0),(13.75,93.75),(13.0,93.5),(13.0,93.5),(13.0,93.0),(13.5,92.5),
 (13.5,92.5),(13.6,92.5),(14.0,92.0),(14.0,92.0),(14.5,91.5),(14.5,91.0),(15.0,90.5),(15.0,90.5),
 (15.5,90.0),(15.5,90.0),(15.5,89.5),(15.5,89.0),(16.0,88.5),(16.0,88.5),(16.2,88.3),(16.5,88.0),
 (16.8,87.7),(16.9,87.2),(17.0,87.0),(17.1,86.8),(17.5,86.5),(17.8,86.0),(18.1,85.7),(18.6,85.4),
 (18.7,85.2),(19.1,85.2),(19.5,84.8),(20.0,84.5),(20.5,84.5),(21.0,84.0),(21.5,84.0),(21.8,83.8),
 (22.5,83.8),(22.75,83.65),(23.0,83.5),(23.25,83.75),(23.5,84.0),(24.0,84.1),(24.5,84.2),]


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
mydir = path+'data'+storm[4:-1]+'_e/'
if not os.path.isdir(mydir):
    os.mkdir(mydir)
    

print(ds.attrs)
print('len_time_new_data: ',len(ds.time))
ds.to_netcdf(mydir+storm[5:-1]+'_e.nc') # netcdf output

print('*****done_!*****')
quit()

