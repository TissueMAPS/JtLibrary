# -*- coding: utf-8 -*-

# Created on 19-May-2016 by Dr. Saadia Iftikhar, saadia.iftikhar@fmi.ch
# ---------------------------------------------------------------------

"""
Created on Thu May 19 10:36:54 2016

@author: saadiaiftikhar
"""

def ismember(a, b):
    k = {}
    for i, j in enumerate(b):
        if j not in k:
            k[j] = i
    return [k.get(itm, None) for itm in a]  