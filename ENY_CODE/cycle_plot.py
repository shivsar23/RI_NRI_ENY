# code to plot the lorenz energy cycle
# requires [storm]_averages.txt [text] file

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from re import findall
# path = r'/home/cas/irdstaff/ird13323/'
# storm = r'data/jawad_3_q/'


def cycle_plot(path:str, storm :str) -> None:
    # handling averages.txt file
    file = open(path+storm+storm[5:-1]+'_averages.txt', 'r')
    string = file.read()
    file.close()
    text_l = [ 'zapeav','eapeav', 'zkeav','ekeav',  'eapebsumav', 
            'casumav',  'geapeav','zape2zkeav',  'eape2ekeav','cksumav',
        'dissav', 'epebsumav', 'kebsumav']

    value=[]
    for text in text_l:
        n=string.find(text)
        line = string[n:n+25]
        val = findall('[+-]?\d*\.\d+', line)
        value+= [float(*val)] 

    print('Read time average values from []_averages.txt file',value)


    for j,num in enumerate(value):
        if num <10:
            value[j]=round(num, 3)
        else:
            value[j]=round(num)
            
    for var,val in zip(text_l, value):
        globals()[var]=val


    # producing image

    def blank_sheet(fig_width=15, fig_height=11,
                    bg_color='white', color='midnightblue'):
        fig = plt.figure(figsize=(fig_width/2.54, fig_height/2.54))
        ax = fig.add_axes((0,0,1,1))  
        ax.set_xlim(0, fig_width)
        ax.set_ylim(0, fig_height)
        
        
        ax.tick_params(bottom=False, top=False,
                    left=False, right=False)
        ax.tick_params(labelbottom=False, labeltop=False,
                    labelleft=False, labelright=False)
        ax.set_facecolor(bg_color)
        ax.spines["top"].set_color(color)
        ax.spines["bottom"].set_color(color)
        ax.spines["left"].set_color(color)
        ax.spines["right"].set_color(color)
        ax.spines["top"].set_linewidth(0)
        ax.spines["bottom"].set_linewidth(0)
        ax.spines["left"].set_linewidth(0)
        ax.spines["right"].set_linewidth(0)
        
        return fig, ax
        
        
    fig ,ax= blank_sheet()
    corners_bottom_left = [(1,8), (9,8), (1,3),(9,3)]
    rect_x = 3
    rect_y = 1
    unknown='?'
    text_block = ['$A_{Z}$' + f'({zapeav})', '$A_{E}$' + f'({eapeav})',
                '$K_{Z}$' + f'({zkeav})','$K_{E}$' + f'({ekeav})']

    text_x = ['$A_{EB}$'+ f'({eapebsumav})', '$C_{A}$'+ f'({casumav})', '$G_{E}$'+ f'({geapeav})', 
            '$C_{Z}$'+ f'({zape2zkeav})','$C_{PK}$'+ f'({eape2ekeav})',
            '$C_{K}$'+ f'({cksumav})', '$D_{E}$'+ f'({dissav})',
            '$\Phi_{EB}$'+ f'({epebsumav})','$K_{EB}$'+ f'({kebsumav})']

    tex_coor = [(10.5,9.7), (4.8,8.7), (12.3,8.7), (2.6,6.7), 
                (10.5,6.7), (4.8,3.7), (12.2,3.7), (7,2), (11.7,2)]

    arrow_coor = [  
                [(10.4,9), (10.4,10.5)], [(9,8.5), (4.1,8.5)], 
                [(12,8.5), (13.8,8.5)], [(2.5,4), (2.5,8)],
                [ (10.4,4), (10.4,8)],[(9,3.5), (4.1,3.5)], 
                [(13.8,3.5), (12,3.5)], [ (9.5,3),(9.5,1)],
                [(11.6,3), (11.6,1),]
                            ]
    #energy terms in block
    for i,corner in enumerate(corners_bottom_left):
        x,y =corner
        ax.add_patch(patches.Rectangle( corner, rect_x, rect_y, 
                                                    fc='none', ec='b' )   )
        
        ax.text(x+0.5,y+0.4, text_block[i], ha='left')
        
    # xchange terms text rendering    
    for j,text in enumerate(text_x):
        ax.text(*tex_coor[j], text )
        
    # arrow annotations top to bottom left to right
    for val,coor in zip(value[4:],arrow_coor):
        coor = coor[::-1] if val<0 else coor
        ax.annotate( '',  *coor  , arrowprops=dict(arrowstyle = "-|>")    )

    fig.savefig(path+storm+storm[5:-1]+'_energy_cycle.png', dpi=200)
    print('check_your_plot')
    print('***code_ended****') 

    return None



