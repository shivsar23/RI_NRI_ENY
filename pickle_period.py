import pickle
import numpy as np
from datetime import datetime


Amphan = {"start_date": datetime(2020,5,16),
        "base_time" :datetime(2020,5,16),
        "end_date" : datetime(2020,5,21,12),
        "ri_start_date" :datetime(2020,5,16,6),
        "ri_end_date" : datetime(2020,5,18,18),
        "landfall_date" : datetime(2020,5,20,9)
        }
Phailin = {"start_date": datetime(2013,10,8,3),
        "base_time" :datetime(2013,10,8,3),
        "end_date" : datetime(2013,10,14,6),
        "ri_start_date" :datetime(2013,10,9,6),
        "ri_end_date" : datetime(2013,10,11,12),
        "landfall_date" : datetime(2013,10,12,15)
        }
Fani = {"start_date": datetime(2019,4,26,3),
        "base_time" :datetime(2019,4,26,3),
        "end_date" : datetime(2019,5,4,12),
        "ri_start_date" :datetime(2019,4,29),
        "ri_end_date" : datetime(2019,4,30,18),
        "landfall_date" : datetime(2019,4,30,18)
        }
Giri = {"start_date": datetime(2010,10,20,12),
        "base_time" :datetime(2010,10,20,12),
        "end_date" : datetime(2010,10,23,6),
        "ri_start_date" :datetime(2010,10,20,12),
        "ri_end_date" : datetime(2010,10,22,12),
        "landfall_date" : datetime(2010,10,22,12)
        }
Madi = {"start_date": datetime(2013,12,6,3),
        "base_time" :datetime(2013,12,6,3),
        "end_date" : datetime(2013,12,12,18),
        "ri_start_date" :datetime(2013,12,6,3),
        "ri_end_date" : datetime(2013,12,7,8),
        "landfall_date" : datetime(2013,12,12,12)
        }
Hudhud = {"start_date": datetime(2014,10,7,3),
        "base_time" :datetime(2014,10,7,3),
        "end_date" : datetime(2014,10,14,9),
        "ri_start_date" :datetime(2014,10,10,6),
        "ri_end_date" : datetime(2014,10,11,6),
        "landfall_date" : datetime(2014,10,12,6)
        }
Titli = {"start_date": datetime(2018,10,8,3),
        "base_time" :datetime(2018,10,8,3),
        "end_date" : datetime(2018,10,12,21),
        "ri_start_date" :datetime(2018,10,9,3),
        "ri_end_date" : datetime(2018,10,10,21),
        "landfall_date" : datetime(2018,10,10,21)
        }
Bulbul = {"start_date": datetime(2019,11,5,0),
        "base_time" :datetime(2019,11,5,0),
        "end_date" : datetime(2019,11,11,0),
        "ri_start_date" :datetime(2019,11,7,0),
        "ri_end_date" : datetime(2019,11,8,12),
        "landfall_date" : datetime(2019,11,9,15)
        }
Mocha = {"start_date": datetime(2023,5,9,12),
        "base_time" :datetime(2023,5,9,12),
        "end_date" : datetime(2023,5,15),
        "ri_start_date" :datetime(2023,5,10,18),
        "ri_end_date" : datetime(2023,5,13,15),
        "landfall_date" : datetime(2023,5,14,6)
        }
Mala = {"start_date": datetime(2006,4,25,3),
        "base_time" :datetime(2006,4,25,3),
        "end_date" : datetime(2006,4,29,18),
        "ri_start_date" :datetime(2006,4,27,6),
        "ri_end_date" : datetime(2006,4,29,0),
        "landfall_date" : datetime(2006,4,29,6)
        }
Sidr = {"start_date": datetime(2007,11,11,9),
        "base_time" :datetime(2007,11,11,9),
        "end_date" : datetime(2007,11,16,3),
        "ri_start_date" :datetime(2007,11,12,0),
        "ri_end_date" : datetime(2007,11,14,3),
        "landfall_date" : datetime(2007,11,15,15)
        }
Nargis = {"start_date": datetime(2008,4,27,3),
        "base_time" :datetime(2008,4,27,3),
        "end_date" : datetime(2008,5,3,9),
        "ri_start_date" :datetime(2008,4,27,9),
        "ri_end_date" : datetime(2008,4,28,9),
        "landfall_date" : datetime(2008,5,2,12)
        }



dc = {"giri": Giri,"amphan":Amphan,"phailin":Phailin,"fani":Fani,"madi":Madi,"bulbul":Bulbul,
      "hudhud":Hudhud,"mala":Mala,"mocha":Mocha,"titli":Titli,"sidr":Sidr,"nargis":Nargis
     }

# Save the data using pickle
with open("/DISK-0/gokul/ENGY/period.pkl", "wb") as file:
    pickle.dump(dc, file)
