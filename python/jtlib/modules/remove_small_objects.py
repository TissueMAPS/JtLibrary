
# Created on 25-March-2016 by Dr. Saadia Iftikhar, saadia.iftikhar@fmi.ch
# ---------------------------------------------------------------------


from skimage.measure import label, regionprops

def remove_small_objects(threshold_image=None,area_threshold=None,*args,**kwargs):
    
     label_image = label(threshold_image)
     
     mask = label_image.copy()
     
     mask[mask>0] = 255

     i1 = 0
     for region in regionprops(label_image):
         
        i1 = i1 + 1 

        if region.area < area_threshold:
            mask[label_image == i1] = 0
     
     label_im = label(mask)
     
     output_image = mask
     
     return output_image, label_im