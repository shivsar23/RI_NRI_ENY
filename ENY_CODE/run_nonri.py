import math

import numpy as np
import xarray as xr

 # from rooscode

from zke import zke
from statstab import statstab
from zape import zape
from zape2zke import zape2zke
from eke import eke
from eape import eape


from cktermssum import cktermmsum
from eape2eke import eape2eke
from catermssum  import catermssum


from geneape import geneape


from kebtermssum import kebtermssum
from epebtermssum import epebtermssum
from eapebtermssum import eapebtermssum

from dissipation import dissipation

path = r'/DISK-0/gokul/ENGY/'
storm = r'dat2/mandous/'


print(storm, '|', sep='\n')


zke(path, storm, openmode='w+')
statstab(path, storm)
zape(path, storm, openmode='r+')

zape2zke(path, storm, openmode='r+')
eke(path, storm, openmode='r+')
eape(path, storm, openmode='r+')

cktermmsum(path, storm , openmode='r+')

eape2eke(path, storm, openmode='r+')


catermssum(path, storm, openmode='r+')


geneape(path, storm, openmode='r+')

kebtermssum(path, storm, openmode='r+')

epebtermssum(path, storm, openmode='r+')

eapebtermssum(path, storm, openmode='r+')
dissipation(path, storm, openmode='r+')
#******* energy_cylce plot

from cycle_plot import cycle_plot
cycle_plot(path, storm )
