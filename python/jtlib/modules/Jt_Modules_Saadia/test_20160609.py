# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:56:02 2016

@author: saadiaiftikhar
"""
#!/Users/saadiaiftikhar/miniconda2/bin/python
import numpy as np
#import pylab
import matplotlib.pyplot as plt
import mahotas as mahotas

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb
from skimage import data, io, filters,feature
import cv2
import os, glob
from scipy import ndimage as ndi
import numpy as np
import skimage as sk
#import removeSmallObjects_Saadia as removeSmallObjects_Saadia
#import calculateThresholdLevel_Saadia
import PIL.ImageOps 
from skimage.morphology import watershed
import scipy as sp
from skimage.feature import peak_local_max
#import segmentSecondary as segmentSecondary
import identify_secondary_objects_iw 
import remove_small_objects 
import separate_clumps
import outline as outline
import label_mask_3d as label_mask_3d
import label_mask as label_mask

import measure_gabor_3d as measure_gabor_3d
import measure_haralick_3d as measure_haralick_3d
import measure_hu_3d as measure_hu_3d
import measure_tas_3d as measure_tas_3d
import measure_zernike_3d as measure_zernike_3d

# import measure_morphology as measure_morphology
import measure_morphology_3d as measure_morphology_3d
# import measure_intensity as measure_intensity
import measure_intensity_3d as measure_intensity_3d

import register_objects as register_objects
import expand_objects_3d as expand_objects_3d
import filter_objects_3d as filter_objects_3d
import relate_objects_3d as relate_objects_3d


#path = '/Volumes/cv7000s$/Users/iftisaad/TM_Test_Data/Corrected_Images/'

path = '/Volumes/cv7000s$/Users/iftisaad/Probability_Images_Results_Test/Original_Images/'
searchString = path + '*_G09_*C01.tif'

#path = '/Users/saadiaiftikhar/Documents/Markus_Data_Samples/'
#searchString = path + '*_c002*.tif'

correction_factors = [2, 1.5, 1.3, 0.9, 0.7, 0.6, 0.58, 0.55, 0.50, 0.45, 0.4, 0.35, 0.3, 0.25]
min_threshold = [0]
plot = False
minarea = 100;
args = []
kwargs=[]
thresh = []
threshold_image = []
imIntensity_original = []

for f in glob.glob(searchString):
    filename, file_extension = os.path.splitext(f)
    print f
    if f.endswith(".tif"):
         Input_filename = os.path.join(path,f) # source file 
        # print(Input_filename)
         imIntensity = cv2.imread(Input_filename, cv2.IMREAD_UNCHANGED) 
         #imIntensity = imIntensity[0:1024,0:1024]
#         imIntensity = mahotas.imread(Input_filename)
         gaussed_intensity_image = mahotas.gaussian_filter(imIntensity,8)
         
         thresh1 = threshold_otsu(gaussed_intensity_image)
         #thresh.append(thresh1)
         
         thresholded_orig_image = gaussed_intensity_image > thresh1
         
        
         
         # print thresholded_orig_image.shape
         
         thresholded_orig_image, label_image = remove_small_objects.remove_small_objects(thresholded_orig_image,minarea)
         
         threshold_image.append(thresholded_orig_image)
         imIntensity_original.append(imIntensity)
        
#         perimeter_trace =outline.outline(label_image)
#         max_eqiv_radius = 30
#         min_eqiv_angle = 6
#         objsize_thres = 50
#         num_region_threshold = 10
#        
#        # Test to do  ... next week 
#        
#         separate_clumps.separate_clumps(label_image, imIntensity, perimeter_trace,max_eqiv_radius, min_eqiv_angle,objsize_thres, num_region_threshold) 
         
#         plt.imshow(thresholded_orig_image, cmap='Greys_r')
#         plt.show()


         #siz1 = threshold_image.shape   
         #print(siz1)

index1 = np.dstack(threshold_image)  
intesity_images = np.dstack(imIntensity_original)

#index1 = threshold_image[0]
#intesity_images = imIntensity_original[0]

siz = index1.shape
print ('The size of Z-stack is:', siz[2])

        
label_images = label_mask_3d.label_mask_3d(index1)
label_image = np.int32(label_images['label_image'])

filtered = filter_objects_3d.filter_objects_3d(label_image, 
                                'area', 100, 'below', relabel=True, plot=False)
filtered_label_image = np.int32(filtered['filtered_image'])

n1 = 5
expanded = expand_objects_3d.expand_objects_3d(label_image, n1, plot=False)
expanded_label_image = np.int32(expanded['expanded_image'])

registered = register_objects.register_objects(expanded_label_image)
registered_label_image = np.int32(registered['objects'])


measurements1 = measure_morphology_3d.measure_morphology_3d(registered_label_image, plot=False)
measurements_morphology = measurements1['measurements']

measurements2 = measure_intensity_3d.measure_intensity_3d(registered_label_image, intesity_images, plot=False)
measurements_intesity = measurements2['measurements']

measurements3 = measure_gabor_3d.measure_gabor_3d(registered_label_image, intesity_images, plot=False)
measurements_gabor = measurements3['measurements']

measurements4 = measure_haralick_3d.measure_haralick_3d(registered_label_image, intesity_images, plot=False)
measurements_haralick = measurements4['measurements']

measurements5 = measure_hu_3d.measure_hu_3d(registered_label_image, intesity_images, plot=False)
measurements_hu = measurements5['measurements']

measurements6 = measure_tas_3d.measure_tas_3d(registered_label_image, intesity_images, plot=False)
measurements_tas = measurements6['measurements']

measurements7 = measure_zernike_3d.measure_zernike_3d(registered_label_image, plot=False)
measurements_zernicke = measurements7['measurements']

#        searchString1 = path + '*_c004_*.tif'
#
#        for f1 in glob.glob(searchString1):
#            filename1, file_extension1 = os.path.splitext(f1)
#            if f1.endswith(".tif"):
#                 Input_filename1 = os.path.join(path,f1) # source file 
##                 print(Input_filename1)
#                 input_image = cv2.imread(Input_filename1, cv2.IMREAD_UNCHANGED) 
#                 input_image = input_image[0:1024,0:1024]
##                input_image = mahotas.imread(Input_filename1)
#                 siz2 = input_image.shape   
#                 print(siz2)
#                 
#                 plt.imshow(input_image, cmap='Greys_r')
#                 plt.show()

#                 print(input_image.dtype)
#                 print(input_image.max())
#                 print(input_image.min())
                
#                 [secondaryLabelMatrixImage,edited_primary_binary_image,th_array] = identify_secondary_objects_iw.identify_secondary_objects_iw(label_image,input_image,correction_factors,min_threshold)
              
              
       # path2 = path + 'Results';
      #  s1 = filename +'_Output_Image'+file_extension
       # labelled_image_filename = os.path.join(path2,s1) 
#        cv2.imwrite(labelled_image_filename, thresholded_orig_image)
        
#        s2 = filename1 +'_Output_Image'+file_extension
#        output_image_filename = os.path.join(path2,s2) 
       # cv2.imwrite(output_image_filename, secondaryLabelMatrixImage) 
#        
#        s3 = filename+'_Output_Image_Log'+file_extension
#        output_image_filename_log = os.path.join(path,s3) 
#        cv2.imwrite(output_image_filename_log, logarithimic_mask) 
        
#plt.show()

