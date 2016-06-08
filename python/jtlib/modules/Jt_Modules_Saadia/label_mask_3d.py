import logging
import numpy as np
#from .. import utils
from skimage.measure import label
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)


def label_mask_3d(mask, plot=False):
    '''
    Jterator module for labeling objects (connected components)
    in a binary image.

    Parameters
    ----------
    mask: numpy.ndarray[bool]
        binary image that should labeled
    plot: bool, optional
        whether a plot should be generated (default: ``False``)
    Returns
    -------
    Dict[str, numpy.ndarray[numpy.int32]]
        "label_image": labeled image
        "figure": html string in case ``kwargs["plot"] == True``

    Note
    ----
    If `mask` is not binary, it will be binarized, i.e. pixels will be set to
    ``True`` if values are greater than zero and ``False`` otherwise.
    '''

    siz = mask.shape
    output1 = []
    
    if (siz[2] == 1):
        mask = mask > 0
        #label_image = utils.label_image(mask)
        label_image = label(mask)
    
        logger.info('identified %d objects', len(np.unique(label_image))-1)
    
        output = {'label_image': label_image}
        
    elif (siz[2] > 1):
        
        for i in range(0,siz[2]):
            
            mask1 = mask[:,:,i] > 0
            label_image = label(mask1)
           # label_image = utils.label_image(mask1)
#            plt.imshow(label_image, cmap='Greys_r')
#            plt.show()
    
            logger.info('identified %d objects', len(np.unique(label_image))-1)
    
            output1.append(label_image) 
            
        output = np.int32(np.dstack(output1))
        
        # print output.shape
        
        output = {'label_image': output}    

            
        
    if plot:
        from .. import plotting

        plots = [
            plotting.create_mask_image_plot(mask, 'ul'),
            plotting.create_mask_image_plot(label_image, 'ur')
        ]

        output['figure'] = plotting.create_figure(
                                plots, title='Labeled objects in mask.')
    else:
        output['figure'] = str()

    return output
