#!/bin/bash

cyclone=("mandous" "asani" "yaas" "nivar" "phethai" "gaja" "mora" "vardah" "lehar" "helen" "thane" "jal" "laila" "aila")


for cyc in ${cyclone[@]};
do

echo ${cyc}

oldtxt="mandous"
newtxt=${cyc}

sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_plt_nri.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_convrsn_plt_qnri.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' contour_plt_qnri.py
python engy_plt_nri.py
python engy_convrsn_plt_qnri.py
python contour_plt_qnri.py

oldtxt=${cyc}
newtxt="mandous"

sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_plt_nri.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_convrsn_plt_qnri.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' contour_plt_qnri.py

done