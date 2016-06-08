import features


def measure_morphology(label_image, plot=False):
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
    f = features.Morphology(
                label_image=label_image
    )

    outputs = {'measurements': f.extract()}

    if plot:
        outputs['figure'] = f.plot()
    else:
        outputs['figure'] = str()

    return outputs
