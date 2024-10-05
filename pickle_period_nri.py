import pickle
import numpy as np
from datetime import datetime


Mandous = {"start_date": datetime(2022,12,6,12),
        "base_time" :datetime(2022,12,6,12),
        "end_date" : datetime(2022,12,10,3),
        "landfall_date" : datetime(2022,12,9,18)
        }
Asani = {"start_date": datetime(2022,5,7,6),
        "base_time" :datetime(2022,5,7,6),
        "end_date" : datetime(2022,5,12,0),
        "landfall_date" : datetime(2022,5,11,12)
        }
Yaas = {"start_date": datetime(2021,5,23,6),
        "base_time" :datetime(2021,5,23,6),
        "end_date" : datetime(2021,5,27,18),
        "landfall_date" : datetime(2021,5,26,3)
        }
Nivar = {"start_date": datetime(2020,11,22,21),
        "base_time" :datetime(2020,11,22,21),
        "end_date" : datetime(2020,11,26,18),
        "landfall_date" : datetime(2020,11,25,18)
        }
Phethai = {"start_date": datetime(2018,12,13,0),
        "base_time" :datetime(2018,12,13,0),
        "end_date" : datetime(2018,12,17,18),
        "landfall_date" : datetime(2018,12,17,6)
        }
Gaja = {"start_date": datetime(2018,11,10,3),
        "base_time" :datetime(2018,11,10,3),
        "end_date" : datetime(2018,11,19,12),
        "landfall_date" : datetime(2018,11,15,18)
        }
Mora = {"start_date": datetime(2017,5,28),
        "base_time" :datetime(2017,5,28),
        "end_date" : datetime(2017,5,30,18),
        "landfall_date" : datetime(2017,5,30,3)
        }
Vardah = {"start_date": datetime(2016,12,6,9),
        "base_time" :datetime(2016,12,6,9),
        "end_date" : datetime(2016,12,13,0),
        "landfall_date" : datetime(2016,12,12,9)
        }
Lehar = {"start_date": datetime(2013,11,23,12),
        "base_time" :datetime(2013,11,23,12),
        "end_date" : datetime(2013,11,28,12),
        "landfall_date" : datetime(2013,11,28,6)
        }
        
Helen = {"start_date": datetime(2013,11,19,0),
        "base_time" :datetime(2013,11,19,0),
        "end_date" : datetime(2013,11,22,18),
        "landfall_date" : datetime(2013,11,22,6)
        }
Thane = {"start_date": datetime(2011,12,25,12),
        "base_time" :datetime(2011,12,25,12),
        "end_date" : datetime(2011,12,30,12),
        "landfall_date" : datetime(2011,12,30,0)
        }

Jal = {"start_date": datetime(2010,11,4,0),
        "base_time" :datetime(2010,11,4,0),
        "end_date" : datetime(2010,11,8,3),
        "landfall_date" : datetime(2010,11,7,15)
        }

Laila = {"start_date": datetime(2010,5,17,6),
        "base_time" :datetime(2010,5,17,6),
        "end_date" : datetime(2010,5,21,6),
        "landfall_date" : datetime(2010,5,20,9)
        }

Aila = {"start_date": datetime(2009,5,23,6),
        "base_time" :datetime(2009,5,23,6),
        "end_date" : datetime(2009,5,26,6),
        "landfall_date" : datetime(2009,5,25,6)
        }
Gulab = {"start_date": datetime(2021,9,24,12),
        "base_time" :datetime(2021,9,24,12),
        "end_date" : datetime(2021,9,28,3),
        "landfall_date" : datetime(2021,9,26,12)
        }
Burevi = {"start_date": datetime(2020,11,30),
        "base_time" :datetime(2020,11,30),
        "end_date" : datetime(2020,12,5,3),
        "landfall_date" : datetime(2020,12,3,6)
        }



dc = {"mandous": Mandous,"asani":Asani,"yaas":Yaas,"nivar":Nivar,"phethai":Phethai,"gaja":Gaja,
      "mora":Mora,"vardah":Vardah,"lehar":Lehar,"helen":Helen,"thane":Thane,"jal":Jal,"laila":Laila,
      "aila":Aila,"gulab":Gulab,"burevi":Burevi,
     }

# Save the data using pickle
with open("/DISK-0/gokul/ENGY/period_nri.pkl", "wb") as file:
    pickle.dump(dc, file)
