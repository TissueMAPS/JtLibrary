import skimage.measure
import numpy as np
#from .. import utils
from skimage.measure import label

def filter_objects_3d(label_image, feature, threshold, remove, relabel, plot):
    '''
    Jterator module to filter labeled image regions (objects) based
    on measured features.

    Parameters
    ----------
    label_image: numpy.ndarray[numpy.int32]
        labeled image that should be filtered
    feature: str
        name of the region property based on which the image should be filtered
        see `scikit-image docs <http://scikit-image.org/docs/dev/api/skimage.measure.html#regionprops>`_
    threshold:
        threshold level (type depends on the chosen `feature`)
    remove: str
        remove objects ``"below"`` or ``"above"`` `threshold`
    relabel: bool
        relabel objects after filtering
    plot: bool, optional
        whether a plot should be generated (default: ``False``)

    Returns
    -------
    Dict[str, numpy.ndarray[int32] or str]
        "filtered_image": filtered label image
        "figure": html string in case ``kwargs["plot"] == True``

    Raises
    ------
    ValueError
        when value of `remove` is not ``"below"`` or ``"above"``
    '''
    if label_image.dtype != np.int32:
        raise TypeError('Argument label image must have data type int32.')

    
    siz = label_image.shape
    output1 = []
    
    if (len(siz) == 2):
        
        label_image1 = label_image
        regions = skimage.measure.regionprops(label_image)
        if remove == 'above':
            ids_to_keep = [r['label'] for r in regions if r[feature] < threshold]
        elif remove == 'below':
            ids_to_keep = [r['label'] for r in regions if r[feature] > threshold]
        else:
            raise ValueError(
                    'Argument "remove" must be a either "above" or "below"')
    
        filtered_image = np.zeros(label_image.shape)
        for ix in ids_to_keep:
            filtered_image[label_image == ix] = ix
    
        n_removed = len(np.unique(label_image)) - len(np.unique(filtered_image))
    
        if relabel:
            filtered_image = label(filtered_image > 0)
    
        output = {'filtered_image': filtered_image}
        
    elif (len(siz) > 2):
        
        for i in range(0,siz[2]):
            
            label_image1 = label_image[:,:,i]
        
            regions = skimage.measure.regionprops(label_image1)
            
            if remove == 'above':
                ids_to_keep = [r['label'] for 
                                        r in regions if r[feature] < threshold]
            elif remove == 'below':
                ids_to_keep = [r['label'] for 
                                        r in regions if r[feature] > threshold]
            else:
                raise ValueError(
                    'Argument "remove" must be a either "above" or "below"')
    
            filtered_image = np.zeros(label_image1.shape)
            for ix in ids_to_keep:
                filtered_image[label_image1 == ix] = ix
    
            n_removed = len(np.unique(label_image1)
                        ) - len(np.unique(filtered_image))
    
            if relabel:
                filtered_image = label(filtered_image > 0)
            
            output1.append(filtered_image)
            
        output = np.dstack(output1) 
        output = {'filtered_image': output}
        
    
    
    if plot:
        from .. import plotting

        plots = [
            plotting.create_mask_image_plot(label_image1, 'ul'),
            plotting.create_mask_image_plot(filtered_image, 'ur'),
        ]

        output['figure'] = plotting.create_figure(
                                plots, title='''
                                    removed %d objects with %s values %s %d
                                ''' % (n_removed, feature, remove, threshold)
        )
    else:
        output['figure'] = str()

    return output
