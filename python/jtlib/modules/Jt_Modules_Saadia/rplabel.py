# Created on 25-March-2016 by Dr. Saadia Iftikhar, saadia.iftikhar@fmi.ch
# ---------------------------------------------------------------------

import numpy as np
from skimage.measure import regionprops, label

def rplabel(imlogical=None,imintensity=None,property_name=None,logarithm=None,
            *args,**kwargs):

    imlabel=label(imlogical)
    
    logarithimic_mask =  imlabel.copy()
    logarithimic_mask[logarithimic_mask>0] = 1
        
    if imintensity.shape == 0:
        imintensity=np.zeros(imlogical.shape).astype(np.int64)
    
    i1 = 0
    for region in regionprops(imlabel):
            i1 = i1 + 1 
            if len(logarithm) >0 :
                if logarithm == np.str('two'):
                    logarithimic_mask[imlabel==i1] = np.log2(region[property_name])
                if logarithm == np.str('ten'):
                    logarithimic_mask[imlabel==i1] = np.log10(region[property_name])
                if logarithm == np.str('nat'):
                    logarithimic_mask[imlabel==i1] = np.log(region[property_name])
            else:
                logarithimic_mask[imlabel==i1] = region[property_name]
       
    return logarithimic_mask

