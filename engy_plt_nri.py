# %%
#For running the code for different cyclones ,
#you need to change the storm location,name of cyclone in dataset,and star_date and end_date in the code
#For shading the ri period you need to change the ri_start_date and ri_end_date
#For quasi lagrangian change the base time to start time of the cyclone
import numpy as np
import pickle
import netCDF4 as nc
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.ticker import AutoMinorLocator
import matplotlib.ticker as ticker

path = '/DISK-0/gokul/ENGY/'
storm_name='mandous'
storm = 'dat2/'+storm_name+'_3_e/'


# Open the NetCDF file
dataset = nc.Dataset(path+storm+storm_name+'_3_e.nc', 'r')
# Load cyclone data
dc = np.load("/DISK-0/gokul/ENGY/period_nri.pkl", allow_pickle=True)


# Extract Time Data
time = dataset.variables['time'][:]
print("Time steps")
print(time)
print(f"No.of timesteps= {len(time)}")
time_units = dataset.variables['time'].units
calendar = time.calendar if hasattr(time, 'calendar') else 'standard'
# Convert time values to datetime objects
base_time=datetime(1900,1,1)
#base_time = dc[storm_name.lower()]["base_time"]
date_values = [base_time + timedelta(hours=float(t)) for t in time]


print(date_values)
print(len(date_values))
print(f"Base time  = {base_time}")

# Read Data from .txt File
with open(path+storm+'/eke.txt', 'r') as file:
    txt_data1 = [float(line.strip()) for line in file.readlines()]
with open(path+storm+'/zke.txt', 'r') as file:
    txt_data2 = [float(line.strip()) for line in file.readlines()]
with open(path+storm+'/zape.txt', 'r') as file:
    txt_data3 = [float(line.strip()) for line in file.readlines()]
with open(path+storm+'/eape.txt', 'r') as file:
    txt_data4 = [float(line.strip()) for line in file.readlines()]
# Assuming date_values contains datetime objects
start_date = dc[storm_name.lower()]["start_date"]
end_date = dc[storm_name.lower()]["end_date"]
# Extend the end_date by 3 hours
end_date_extended = end_date + timedelta(hours=3)


#ri_start_date =dc[storm_name.lower()]["ri_start_date"]
#ri_end_date = dc[storm_name.lower()]["ri_end_date"]
# landfall_date is the datetime object representing the landfall time
landfall_date = dc[storm_name.lower()]["landfall_date"]
# Find the indices corresponding to start_date and end_date
start_index = date_values.index(start_date)
end_index = date_values.index(end_date)

# Plot the variables
plt.figure(figsize=(10,6))  # Adjust the figure size as needed
plt.xlim(start_date, end_date_extended)
# Add a shaded region
#plt.axvspan(ri_start_date, ri_end_date, alpha= 0.5, color='#FF9999')  # Adjust color and alpha as needed
# Increase x and y-axis tick label sizes
plt.xticks(fontsize=15)
# Set y-axis in scientific notation with an exponent of 10^3
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# Access the y-axis tick labels
y_formatter = plt.gca().get_yaxis().get_major_formatter()

# Adjust the global font size of the plot (including exponent part)
plt.rc('font', size=15)
plt.yticks(fontsize=15)


# Create the Plot
# Plot variable1 with blue color and solid line
plt.plot(date_values[start_index:end_index+1], txt_data1[start_index:end_index+1], label='EKE', color='blue', linestyle='-')
# Plot variable2 with green color and dashed line
plt.plot(date_values[start_index:end_index+1], txt_data2[start_index:end_index+1], label='ZKE', color='green', linestyle='--')
# Plot variable3 with red color and dotted line
plt.plot(date_values[start_index:end_index+1], txt_data3[start_index:end_index+1], label='ZAPE', color='red', linestyle=':')
# Plot variable4 with purple color and dash-dot line
plt.plot(date_values[start_index:end_index+1], txt_data4[start_index:end_index+1], label='EAPE', color='purple', linestyle='-.')


# Add labels and title
plt.xlabel('Date and Time (Hours)', fontdict={'fontsize': 21, 'fontweight': 'bold'})
plt.ylabel('Energy (J/m²)', fontdict={'fontsize': 21, 'fontweight': 'bold'})

# Add legend
plt.legend(prop={'weight':'bold'})
plt.legend(fontsize=15)
# Find maximum values and their indices
max_values = [max(txt_data1), max(txt_data2), max(txt_data3), max(txt_data4)]
max_indices = [txt_data1.index(max_values[0]), txt_data2.index(max_values[1]), txt_data3.index(max_values[2]), txt_data4.index(max_values[3])]
max_values_rounded = [round(value, 1) for value in max_values]

# Add a vertical dashed line at landfall time
plt.axvline(landfall_date, color='black', linestyle='--') 
# Label maximum values
for i, value in enumerate(max_values_rounded):
    if i == 2 :  # Adjust the position for variable2
        plt.text(date_values[max_indices[i]], value, f'Max: {value}', ha='right', va='bottom', color='black', fontsize=15)
        plt.scatter(date_values[max_indices[i]], value, marker='*', color='black', s=100)  # 's' is the marker size
    else:
        plt.text(date_values[max_indices[i]], value, f'Max: {value}', ha='right', va='bottom', color='black', fontsize=15)
        plt.scatter(date_values[max_indices[i]], value, marker='*', color='black', s=100)  # 's' is the marker size
# Increase thickness of major ticks
plt.tick_params(axis='x', which='major', width=2,length=4,rotation=15)
plt.tick_params(axis='y', which='major', width=2,length=4)
plt.tick_params(axis='x', which='minor', width=1, length=2, direction='in')
# Set the minor locator to AutoMinorLocator for 8 minor ticks between majors
plt.gca().xaxis.set_minor_locator(AutoMinorLocator(8))
# Set y-axis range
plt.ylim(0, 8e5)  # Set the y-axis range from 0 to 1.5*10^6


# Adjust Margins
plt.subplots_adjust(left=0.1, right=0.94, top=.95, bottom=0.2)
# Save the plot to a desired location
plt.savefig(path+storm+storm[4:-1]+'_energy_plot.png',dpi =300)
plt.show()
# Close the NetCDF file
dataset.close()



