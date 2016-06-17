import numpy as np


def remove_full_image_object(label_image, plot=False):
    '''Jterator module to remove a single object that spans the entire labeled 
    image, which may occur as an artefact of thresholding.

    Parameters
    ----------
    label_image: numpy.ndarray[numpy.int32]
        labeled image that should be filtered
    plot: bool, optional
        whether a plot should be generated (default: ``False``)

    Returns
    -------
    Dict[str, numpy.ndarray[int32] or str]
        "filtered_image": filtered label image
        "figure": html string in case ``kwargs["plot"] == True``

    '''
    output = dict()
    if all(np.unique(label_image) == 1):
        output['filtered_image'] = np.zeros(
            label_image.shape, dtype=label_image.dtype
        )

    if plot:
        # TODO
        output['figure'] = str()
    else:
        output['figure'] = str()
    return output
