# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the save model
loaded_model=pickle.load(open('C:/Users/yash/Documents/Deployment/diabetes/trained_model.sav','rb')) #rb read the binary format


input_data=(1,85,66,29,0,26.6,0.351,31)
#changing the input_data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
#standardize the input data
#std_data=ss.transform(input_data_reshaped)
#print(std_data)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction[0]==0:
    print("not diabetes")
else:
    print("diabetes")

