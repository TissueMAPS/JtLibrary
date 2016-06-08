import features

def measure_morphology_3d(label_image, plot=False):
    '''
    Jterator module for measuring morhological features of objects
    (connected components) in a labeled image.
    For more details see
    `mahotas docs <http://mahotas.readthedocs.org/en/latest/features.html>`_.

    Parameters
    ----------
    label_image: numpy.ndarray[int32]
        labeled image; pixels with the same label encode an object
    plot: bool, optional
        whether a plot should be generated (default: ``False``)

    Returns
    -------
    Dict[str, pandas.DataFrame[float] or str]
        * "measurements": extracted morphology features
        * "figure": html string in case `plot` is ``True``

    See also
    --------
    :py:class:`jtlib.features.Morphology`
    '''
    
    siz = label_image.shape
    output1 = []
    
    if (siz[2] == 1):
        
        f = features.Morphology(
                    label_image=label_image
        )
    
        outputs = {'measurements': f.extract()}
        
    elif (siz[2] > 1):
        
        for i in range(0,siz[2]):

            label_image1 = label_image[:,:,i]
            
            f = features.Morphology(
                    label_image=label_image1
                    )
    
            output1.append(f.extract()) 
        
        outputs = {'measurements': output1}
        

    if plot:
        outputs['figure'] = f.plot()
    else:
        outputs['figure'] = str()

    return outputs
