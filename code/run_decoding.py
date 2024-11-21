#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:38:18 2024

@author: simon.kern
"""
import mne
import sklearn
from tqdm import tqdm
# from meg_utils import dataloading
from bids import BIDSLayout
from load_funcs import layout, load_localizer
import settings


#%% first load all data into memory

data_localizer = {}

for subject in tqdm(layout.subjects, 'loading localizer data'):
    if subject in ['01', '23', '03', '04']:
        # somehow, these give errors when loading, so leave them out for now
        # should be included in the final calculation
        # if you see this in a PR, please let me knowm ;-)
        continue

    # load MEG data from the localizer
    data_x, data_y = load_localizer(subject=subject, verbose=False)

    # do cross validation decoding in sensor space across time
