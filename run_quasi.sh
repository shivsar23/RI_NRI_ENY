#!/bin/bash

cyclone=("giri" "phailin" "madi" "hudhud" "titli" "fani" "amphan" "bulbul" "mocha" "mala" "sidr" "nargis")
#cyclone=("mocha")

for cyc in ${cyclone[@]};
do

echo ${cyc}

oldtxt="amphan"
newtxt=${cyc}
newtxt1="${cyc}_3_q"
sed -i 's/'${oldtxt}'/'${newtxt}'/g' quasi_lag_data_copy.py
sed -i 's/'${oldtxt}'/'${newtxt1}'/g' /DISK-0/gokul/ENGY/rosscode/ross_run.py
python quasi_lag_data_copy.py
python /DISK-0/gokul/ENGY/rosscode/ross_run.py

oldtxt=${cyc}
oldtxt1="${cyc}_3_q"
newtxt="amphan"

sed -i 's/'${oldtxt}'/'${newtxt}'/g' quasi_lag_data_copy.py
sed -i 's/'${oldtxt1}'/'${newtxt}'/g' /DISK-0/gokul/ENGY/rosscode/ross_run.py
done