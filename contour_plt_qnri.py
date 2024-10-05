# %%
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

path = '/DISK-0/gokul/ENGY/dat2/'
storm_name='mandous'
storm = storm_name+'_3_e/'+'vertical_eke'
# Load cyclone data
dc = np.load("/DISK-0/gokul/ENGY/period_nri.pkl", allow_pickle=True)

# Load the data from the file
data = np.loadtxt(path + storm + '.txt')
time, pressure_levels = data.shape
print(data.shape)
print(type(data))
# Pressure levels range from 1000 to 100 hPa with a step size of 50
pressure_levels_hpa = np.arange(1000,50,-50)  
# Define the base date and time
base_time = dc[storm_name.lower()]["base_time"]
base_date = base_time

# Create a list of datetime objects based on the time in hours
time_hours = np.arange(time) * 3  # Assuming data points are 3 hours apart
time_hours = time_hours.tolist()  # Convert to Python list
date_values = [base_date + timedelta(hours=t) for t in time_hours]

# Create a meshgrid for contour plotting with pressure levels on the y-axis
Y, X = np.meshgrid(pressure_levels_hpa, time_hours)

# Create a custom colormap for positive (green) and negative (red) values
cmap = plt.cm.RdYlGn

# Create a contour plot# Increase the number of contour levels (for example, 100 levels)
contour_levels = 80
plt.figure(figsize=(10, 6))
contour = plt.contourf(X, Y, data, levels=contour_levels, cmap='Oranges')
color_bar = plt.colorbar(contour)
color_bar.set_label('EKE (J/m^2)', fontsize=25, fontweight='bold')
color_bar.ax.tick_params(labelsize=18)  # Adjust color bar tick label size
plt.grid(color='black',alpha=0.3)
# Set labels and title
plt.xlabel('Date and Time (Hours)', fontdict={'fontsize': 25, 'fontweight': 'bold'})
plt.ylabel('Pressure Level (hPa)', fontdict={'fontsize': 25, 'fontweight': 'bold'})
# Increase x and y-axis tick label sizes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# Invert the y-axis
plt.gca().invert_yaxis()

# Format the x-axis with date and time values
plt.xticks(time_hours[::10], [f"{base_time + timedelta(hours=int(t))}" for t, date in zip(time_hours[::10], date_values[::10])], rotation=20)

# Adjust Margins
plt.subplots_adjust(left=0.15, right=0.98, top=0.94, bottom=0.26)

#Save the figure
plt.savefig(path+storm[:-12]+storm_name+'_3_e_'+'vertical_eke_contour_plt.png',dpi=300)

plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

path = '/DISK-0/gokul/ENGY/dat2/'
storm_name='mandous'
storm = storm_name+'_3_e/'+'vertical_geape'
# Load cyclone data
dc = np.load("/DISK-0/gokul/ENGY/period_nri.pkl", allow_pickle=True)

# Load the data from the file
data = np.loadtxt(path + storm + '.txt')
data *= 10**5  # Multiply GEAPE values by 10^5
time, pressure_levels = data.shape

# Pressure levels range from 1000 to 100 hPa with a step size of 50
pressure_levels_hpa = np.arange(1000, 50, -50)
# Define the base date and time
base_time = dc[storm_name.lower()]["base_time"]
base_date = base_time
# Create a list of datetime objects based on the time in hours
time_hours = np.arange(time) * 3  # Assuming data points are 3 hours apart
time_hours = time_hours.tolist()  # Convert to Python list
date_values = [base_date + timedelta(hours=t) for t in time_hours]

# Create a meshgrid for contour plotting with pressure levels on the y-axis
Y, X = np.meshgrid(pressure_levels_hpa, time_hours)

# Create a custom colormap for positive (green) and negative (red) values
cmap = plt.cm.RdYlGn
# Create a contour plot# Increase the number of contour levels (for example, 100 levels)
contour_levels = 80
# Create a contour plot
plt.figure(figsize=(10, 6))
vmin = min(np.min(data), -np.max(data))
vmax = max(np.max(data), -np.min(data))
contour = plt.contourf(X, Y, data, levels=contour_levels, cmap=cmap, vmin=vmin, vmax=vmax)
color_bar = plt.colorbar(contour)
color_bar.set_label('GE x 10^-5(W/m^2)', fontsize=20, fontweight='bold')
color_bar.ax.tick_params(labelsize=18)  # Adjust color bar tick label size
plt.grid(color='black',alpha=0.3)


# Set labels and title
plt.xlabel('Date and Time(Hours)', fontdict={'fontsize': 20, 'fontweight': 'bold'})
plt.ylabel('Pressure Level (hPa)', fontdict={'fontsize': 20, 'fontweight': 'bold'})
plt.title('GE Contour', fontdict={'fontsize': 20, 'fontweight': 'bold'})
# Increase x and y-axis tick label sizes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# Invert the y-axis
plt.gca().invert_yaxis()

# Format the x-axis with date and time values
plt.xticks(time_hours[::10], [f"{base_time + timedelta(hours=int(t))}" for t, date in zip(time_hours[::10], date_values[::10])], rotation=20)

# Adjust Margins
plt.subplots_adjust(left=0.15, right=0.98, top=0.94, bottom=0.26)

#Save the figure
plt.savefig(path+storm[:-14]+storm_name+'_3_e_'+'vertical_geape_contour_plt.png',dpi=300)
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

path = '/DISK-0/gokul/ENGY/dat2/'
storm_name='mandous'
storm = storm_name+'_3_e/'+'vertical_eape2eke'
# Load cyclone data
dc = np.load("/DISK-0/gokul/ENGY/period_nri.pkl", allow_pickle=True)

# Load the data from the file
data = np.loadtxt(path + storm + '.txt')
data *= 10**5  # Multiply CPK values by 10^5
time, pressure_levels = data.shape

# Pressure levels range from 1000 to 100 hPa with a step size of 50
pressure_levels_hpa = np.arange(1000, 50, -50)

# Define the base date and time
base_time = dc[storm_name.lower()]["base_time"]
base_date = base_time

# Create a list of datetime objects based on the time in hours
time_hours = np.arange(time) * 3  # Assuming data points are 3 hours apart
time_hours = time_hours.tolist()  # Convert to Python list
date_values = [base_date + timedelta(hours=t) for t in time_hours]

# Create a meshgrid for contour plotting with pressure levels on the y-axis
Y, X = np.meshgrid(pressure_levels_hpa, time_hours)

# Create a custom colormap for positive (green) and negative (red) values
cmap =plt.cm.RdYlGn
# Create a contour plot# Increase the number of contour levels (for example, 100 levels)
contour_levels = 80
# Create a contour plot
plt.figure(figsize=(10, 6))
vmin = min(np.min(data), -np.max(data))
vmax = max(np.max(data), -np.min(data))
contour = plt.contourf(X, Y, data, levels=contour_levels, cmap=cmap, vmin=vmin, vmax=vmax)
color_bar = plt.colorbar(contour)
color_bar.set_label('CPK x 10^-5(W/m^2)', fontsize=12, fontweight='bold')
color_bar.ax.tick_params(labelsize=12)  # Adjust color bar tick label size
plt.grid(color='black',alpha=0.3)

# Set labels and title
plt.xlabel('Date and Time(Hours)', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.ylabel('Pressure Level (hPa)', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.title('CPK Contour', fontdict={'fontsize': 14, 'fontweight': 'bold'})
# Increase x and y-axis tick label sizes
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Invert the y-axis
plt.gca().invert_yaxis()

# Format the x-axis with date and time values
plt.xticks(time_hours[::10], [f"{base_time + timedelta(hours=int(t))}" for t, date in zip(time_hours[::10], date_values[::10])], rotation=15)

# Adjust Margins
plt.subplots_adjust(left=0.15, right=0.98, top=0.95, bottom=0.2)


#Save the figure
plt.savefig(path+storm[:-17]+storm_name+'_3_e_'+'vertical_eape2eke_contour_plt.png',dpi=300)
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

path = '/DISK-0/gokul/ENGY/dat2/'
storm_name='mandous'
storm = storm_name+'_3_e/'+'vertical_cksum'
# Load cyclone data
dc = np.load("/DISK-0/gokul/ENGY/period_nri.pkl", allow_pickle=True)

# Load the data from the file
data = np.loadtxt(path + storm + '.txt')
data *= 10**5  # Multiply CK values by 10^5
time, pressure_levels = data.shape

# Pressure levels range from 1000 to 100 hPa with a step size of 50
pressure_levels_hpa = np.arange(1000, 50, -50)

# Define the base date and time
base_time = dc[storm_name.lower()]["base_time"]
base_date = base_time


# Create a list of datetime objects based on the time in hours
time_hours = np.arange(time) * 3  # Assuming data points are 3 hours apart
time_hours = time_hours.tolist()  # Convert to Python list
date_values = [base_date + timedelta(hours=t) for t in time_hours]

# Create a meshgrid for contour plotting with pressure levels on the y-axis
Y, X = np.meshgrid(pressure_levels_hpa, time_hours)

# Create a custom colormap for positive (green) and negative (red) values
cmap =plt.cm.RdBu_r
# Create a contour plot# Increase the number of contour levels (for example, 100 levels)
contour_levels = 80
# Create a contour plot
plt.figure(figsize=(10, 6))
vmin = min(np.min(data), -np.max(data))
vmax = max(np.max(data), -np.min(data))
contour = plt.contourf(X, Y, data, levels=contour_levels, cmap=cmap, vmin=vmin, vmax=vmax)
color_bar = plt.colorbar(contour)
color_bar.set_label('CK x 10^-5(W/m^2)', fontsize=12, fontweight='bold')
color_bar.ax.tick_params(labelsize=12)  # Adjust color bar tick label size
plt.grid(color='black',alpha=0.3)


# Set labels and title
plt.xlabel('Date and Time(Hours)', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.ylabel('Pressure Level (hPa)', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.title('CK Contour', fontdict={'fontsize': 14, 'fontweight': 'bold'})
# Increase x and y-axis tick label sizes
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Invert the y-axis
plt.gca().invert_yaxis()

# Format the x-axis with date and time values
plt.xticks(time_hours[::10], [f"{base_time + timedelta(hours=int(t))}" for t, date in zip(time_hours[::10], date_values[::10])], rotation=15)

# Adjust Margins
plt.subplots_adjust(left=0.15, right=0.98, top=0.95, bottom=0.2)

#Save the figure
plt.savefig(path+storm[:-14]+storm_name+'_3_e_'+'vertical_cksum_contour_plt.png',dpi=300)
plt.show()


