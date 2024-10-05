#to compute stage wise averages of terms in energetics study

import numpy as np

path = r'/DISK-0/gokul/ENGY/'
storm = r'data/phailin_3_q'

#variables

total = 14 #total number of timesteps

stages  = [ [0,2], [2,4], [4,10], [10,12], [12,-1] ]
st_names = ['d', 'dd', 'cs', 'dd_a', 'd_a']

#quantities
names = [
	  'casum', 'cksum' , 'diss', 'eape', 'eape2eke', 'eapebsum', 
	'eddyapebdyterm1', 'eddyapebdyterm2', 'eddyapebdyterm3',
	'eddykebdyterm1', 'eddykebdyterm2', 'eddykebdyterm3' ,
	'eddypebdyterm1', 'eddypebdyterm2', 'eddypebdyterm3',
	'eke', 'epebsum', 'geape', 'kebsum', 'zape',
	'zape2eape1', 'zape2eape2', 'zape2zke', 'zke', 'zke2eke1',
	'zke2eke2', 'zke2eke3', 'zke2eke4'
]  



for i,steps in enumerate(stages):
    denominator_eke = []  #'Ck', 'Cpk', '-De', 'Ke'
    denominator_tee = []  #'Ca', 'Ge', 'Ck', '-De', 'Ke'
    Ke=0
    Ae_Ke = []
    with open(path+storm+storm[5:-1]+st_names[i]+'.txt', 'w+') as file:
        pass
    for quantity in names:
        array = np.loadtxt(path+storm+quantity+'.txt')
        #print(steps)
        mean = np.mean(array[steps[0]: steps[-1]], axis=-1) #slice for stage of storm

        with open(path+storm+storm[5:-1]+st_names[i]+'.txt', 'r+') as file:
            file.read()
            file.write(f'{quantity}av: {mean} \n') # writing in file

        if quantity in [ 'cksum' , 'eape2eke', 'diss']:
            denominator_eke +=[mean]
        if quantity in ['casum', 'geape', 'cksum', 'diss']:
            denominator_tee +=[mean]
        if quantity in [ 'eke', 'eape']:
            Ae_Ke+=[mean]
            Ke = mean

    doubletime_eke =  Ke/(sum(denominator_eke)*3600*24) # doubing time in days
    doubletime_tee =  sum(Ae_Ke)/(sum(denominator_tee)*3600*24) # doubling time in days

    with open(path+storm+storm[5:-1]+st_names[i]+'.txt', 'r+') as file:
        file.read()
        file.write(f'\n doubletime_eke: {doubletime_eke} \ndoubletime_tee: {doubletime_tee} \ncheck: \nCk+De+Cpk: {denominator_eke} \nCa+Ck+De+Ge: {denominator_tee} \nEke: {Ke} \nEape+Eke: {Ae_Ke}') # writing in file

print('****done !******')
  






