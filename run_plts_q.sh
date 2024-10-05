#!/bin/bash

cyclone=("giri" "phailin" "madi" "hudhud" "titli" "fani" "amphan" "bulbul" "mocha" "mala" "sidr" "nargis")


for cyc in ${cyclone[@]};
do

echo ${cyc}

oldtxt="amphan"
newtxt=${cyc}

sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_plt1.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_convrsn_plt_q.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' contour_plt_q.py
python engy_plt1.py
python engy_convrsn_plt_q.py
python contour_plt_q.py

oldtxt=${cyc}
newtxt="amphan"

sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_plt1.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' engy_convrsn_plt_q.py
sed -i 's/'${oldtxt}'/'${newtxt}'/g' contour_plt_q.py

done