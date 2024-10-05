#!/bin/bash

cyclone=("mandous" "asani" "yaas" "nivar" "phethai" "gaja" "mora" "vardah" "lehar" "helen" "thane" "jal" "laila" "aila" "gulab" "burevi" )
#cyclone=("mocha")

for cyc in ${cyclone[@]};
do

echo ${cyc}

oldtxt="mandous"
newtxt=${cyc}
newtxt1="${cyc}_3_q"
sed -i 's/'${oldtxt}'/'${newtxt}'/g' quasi_lag_data_copynonri.py
sed -i 's/'${oldtxt}'/'${newtxt1}'/g' /DISK-0/gokul/ENGY/rosscode/ross_runnonri.py
python quasi_lag_data_copynonri.py
python /DISK-0/gokul/ENGY/rosscode/ross_runnonri.py

oldtxt=${cyc}
oldtxt1="${cyc}_3_q"
newtxt="mandous"

sed -i 's/'${oldtxt}'/'${newtxt}'/g' quasi_lag_data_copynonri.py
sed -i 's/'${oldtxt1}'/'${newtxt}'/g' /DISK-0/gokul/ENGY/rosscode/ross_runnonri.py
done