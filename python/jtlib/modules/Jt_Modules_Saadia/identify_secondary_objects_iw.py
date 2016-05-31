# Created on 25-March-2016 by Dr. Saadia Iftikhar, saadia.iftikhar@fmi.ch
# ---------------------------------------------------------------------

import numpy as np
#import jtlib as jtlib
from matplotlib import pyplot as plt
import skimage as sk
from scipy import ndimage as ndi
import remove_small_objects 
from skimage.morphology import watershed, binary_dilation
from skimage.measure import label
import segment_secondary as segment_secondary

def identify_secondary_objects_iw(input_label_image=None,input_image=None,
                                  correction_factors=None,min_threshold=None):

#    if input_image.dtype is not 'integer':
#        raise TypeError("Input Image must have type integer.")
        
    if input_image.dtype == "uint16":
        input_image = sk.img_as_uint(input_image)
        min_threshold = sk.img_as_uint(min_threshold)
    else:
        if input_image.dtype == 'uint8':
            input_image = sk.img_as_ubyte(input_image)
            min_threshold = sk.img_as_ubyte(min_threshold)
        else:
            raise TypeError(
                        "Argument input_image must have type uint8 or uint16.")
            
#    if input_label_image.dtype == 'logical':
#        raise TypeError("Argument input_label_image must be a labeled image.")
        
#    if input_label_image.dtype != 'integer':
#        raise TypeError("Argument input_label_image must have type integer.")
        
#    if input_label_image.dtype == 'int32':
#        raise TypeError("Argument input_label_image  must have type int32.")
        
    input_label_image = input_label_image
    
    max_threshold = 1

    output_label_image = segment_secondary.segment_secondary(
                                                input_image,input_label_image,
                                                input_label_image,
                                                correction_factors,
                                                min_threshold, max_threshold)
#    print(output_label_image)
    
#    if args[4]:
#        
#        out_mask = ndi.binary_fill_holes(output_label_image)
#        
#        dilated_image = binary_dilation(out_mask)
#    
#        borders = np.logical_xor(out_mask, dilated_image)
#        
#        [mask,label_image] = remove_small_objects(
#                            threshold_image=borders.copy(), area_threshold)
#                
#        labeled_cells=sk.color.colorlabel.label2rgb(label(label_image))
#        
#        fig = plt.figure()
#        fig.plt.subplot(2,2,1)
#        fig.plt.title('Outlines of identified objects')
#        fig.plt.imshow(input_image,[np.quantile(input_image[:],0.01),
#                                    np.quantile(input_image[:],0.99)])
#        fig.plt.show()
#        
#        fig.plt.subplot(2,1,2)
#        fig.plt.imshow(labeled_cells)
#        plt.title('Identified objects')
#        fig.plt.show()
        
    output_label_image = output_label_image
    
    return output_label_image
