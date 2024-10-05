import pandas as pd
import numpy as np

begyear = 2010
endyear = 2023

name_list = []
lat_list = []
lon_list = []

# Define the columns you want to extract
columns_to_extract = [2,5,6] # Replace with your actual column names

filepath = "/DISK-0/gokul/ENGY/data/IMD_Best_track.xls"

for year in range(begyear, endyear+1):

    print(year)

    # Load the Excel file
    df = pd.read_excel(filepath, header=0, sheet_name=str(year))

    names = df.iloc[:,2].tolist()
    lat = df.iloc[:,5].tolist()
    lon = df.iloc[:,6].tolist()

    name_list.extend(names)
    lat_list.extend(lat)
    lon_list.extend(lon)

print(np.array(name_list).shape)

#search_list = []

def toalpha(inpstr):
    outstr = ''.join(ch for ch in inpstr if ch.isalnum())
    return outstr

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

for pos in range(len(name_list)):
    if isfloat(name_list[pos]):
        if(np.isnan(name_list[pos])):
            name_list[pos] = ""

#print(name_list)

def get_loc(arr, name):
    loc_list = []
    for i in range(len(arr)):
        if(toalpha(arr[i]).lower() == name.lower()):
            loc_list.append(i)
    return loc_list

cyclone = "OCKHI"

pos_list = get_loc(name_list, cyclone)

wfilename = cyclone.lower()+"_track_data.dat"
print(wfilename)

wfile = open(wfilename, "w")
#for pos in pos_list:
    #print("("+str(lat_list[pos])+","+str(lon_list[pos])+")")
#    if(isfloat(lat_list[pos]) and isfloat(lon_list[pos])):
#        if(not np.isnan(lat_list[pos]) and not np.isnan(lon_list[pos])):
#            wline = str(lat_list[pos])+"\t"+str(lon_list[pos])+"\n"
#            print(wline)
#            wfile.write(wline)
for i, pos in enumerate(pos_list):
    if i % 1 == 0:  # Process only alternate rows
        if(isfloat(lat_list[pos]) and isfloat(lon_list[pos])):
            if(not np.isnan(lat_list[pos]) and not np.isnan(lon_list[pos])):
                wline = str(lat_list[pos]) + "\t" + str(lon_list[pos]) + "\n"
                print(wline)
                wfile.write(wline)

wfile.close()

data = np.loadtxt(cyclone.lower()+"_track_data.dat")

track = []

for i in range(len(data)):
    track.append((data[i,0], data[i,1]))

print(track)
print(len(track))