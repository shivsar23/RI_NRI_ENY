import netCDF4 as nc
import matplotlib.pyplot as plt

path = '/DISK-0/gokul/ENGY/'
storm = 'data/ockhi_e_fulltrack/'
# Open the NetCDF file
dataset = nc.Dataset(path+storm+'ockhi_e_fulltrack.nc', 'r')

# Extract Time Data
time = dataset.variables['time'][:]
print(time)
# Read Data from .txt File
with open(path+storm+'/casum.txt', 'r') as file:
    txt_data1 = [float(line.strip()) for line in file.readlines()]
with open(path+storm+'/cksum.txt', 'r') as file:
    txt_data2 = [float(line.strip()) for line in file.readlines()]
with open(path+storm+'/eape2eke.txt', 'r') as file:
    txt_data3 = [float(line.strip()) for line in file.readlines()]
with open(path+storm+'/zape2zke.txt', 'r') as file:
    txt_data4 = [float(line.strip()) for line in file.readlines()]
# Plot the variables
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed


# Create the Plot
# Plot variable1 with blue color and solid line
plt.plot(time, txt_data1, label='CA', color='blue', linestyle='-')
# Plot variable2 with green color and dashed line
plt.plot(time, txt_data2, label='CK', color='green', linestyle='--')
# Plot variable3 with red color and dotted line
plt.plot(time, txt_data3, label='CPK', color='red', linestyle=':')
# Plot variable4 with purple color and dash-dot line
plt.plot(time, txt_data4, label='CZ', color='purple', linestyle='-.')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Conversion rate(W/m2)')
plt.title('Energy conversion terms vs. Time')

# Add legend
plt.legend()

# Find maximum values and their indices
max_values = [max(txt_data1), max(txt_data2), max(txt_data3), max(txt_data4)]
max_indices = [txt_data1.index(max_values[0]), txt_data2.index(max_values[1]), txt_data3.index(max_values[2]), txt_data4.index(max_values[3])]



# Label maximum values
for i, value in enumerate(max_values):
    if i == 1:  # Adjust the position for variable2
        plt.text(time[max_indices[i]], value, f'Max: {value}', ha='right', va='bottom', color='black', fontsize=8)
        plt.scatter(time[max_indices[i]], value, marker='*', color='black', s=100)  # 's' is the marker size
    else:
        plt.text(time[max_indices[i]], value, f'Max: {value}', ha='left', va='bottom', color='black', fontsize=8)
        plt.scatter(time[max_indices[i]], value, marker='*', color='black', s=100)  # 's' is the marker size

   


# Save the plot to a desired location
plt.savefig(path+storm+storm[4:-1]+'_energy_conversion_plot.png')

# Close the NetCDF file
dataset.close()



