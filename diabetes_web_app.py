# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:31:07 2024

@author: yash
"""

import numpy as np
import pickle
import streamlit
loaded_model=pickle.load(open('C:/Users/yash/Documents/Deployment/diabetes/trained_model.sav','rb')) #rb read the binary format