#!/usr/bin/env python
# coding: utf-8

# # Own segmentator

# At the final of the readme of FFN algorithm, here is a short description of how to get the segmented images with FFN. However, that code does not work. Below, you will find a script which creates the images from the inference output. The inference output is a directory called 0, which has a file called `seg-0_0_0.npz`.
# 
# In order to check this images in a clear way, the original color background was switched from black to white. To do this, launch the function called `just_blue()`. If you want to see the original version, launch `black_blue()` function.

# In[ ]:


import numpy as np
import imageio 
from PIL import Image

def just_blue(input_dir, output_dir):
    data = np.load(input_dir)

    if 'segmentation' in data:
      seg = data['segmentation']
    else:
      raise ValueError('FFN NPZ file %s does not contain valid segmentation.' %
                       target_path)

    #origins = data['origins'].item()
    output = seg.astype(np.uint64)
    print('Cube size: ', output.shape)


    rgbArray = np.zeros((output.shape[1],output.shape[2],3), 'uint8')


    for k in range(output.shape[0]):#output.shape[0]
        ima=output[k,:,:]
        #print("Image N. "+str(k))
        for j in range(ima.shape[1]):
            #if( j%100 == 0):
                #print ("conversion percent "+ str(j/output.shape[1]))
            for i in range(ima.shape[0]):
                rgbArray[i,j,0] = ima[i,j]/(256*256)
                rgbArray[i,j,1] = (ima[i,j]%(256*256))/256
                rgbArray[i,j,2] = (ima[i,j]%(256*256))%256
                #print(rgbArray[i,j,0], rgbArray[i,j,1], rgbArray[i,j,2])

                if(rgbArray[i,j,0] == 0 and rgbArray[i,j,1] == 0 and (rgbArray[i,j,2] == 0 or rgbArray[i,j,2] == 1)):
                    rgbArray[i,j,0]=255
                    rgbArray[i,j,1]=255
                    rgbArray[i,j,2]=255
                else: 
                    rgbArray[i,j,2]=rgbArray[i,j,2] + 100


        img = Image.fromarray(rgbArray)
        img.save(output_dir + str(k)+ '.tif') #change name


        
def black_blue(input_dir, output_dir):
    data = np.load(input_dir)

    if 'segmentation' in data:
      seg = data['segmentation']
    else:
      raise ValueError('FFN NPZ file %s does not contain valid segmentation.' %
                       target_path)

    #origins = data['origins'].item()
    output = seg.astype(np.uint64)
    print('Cube size: ', output.shape)


    rgbArray = np.zeros((output.shape[1],output.shape[2],3), 'uint8')


    for k in range(output.shape[0]):#output.shape[0]
        ima=output[k,:,:]
        for j in range(ima.shape[1]):
            for i in range(ima.shape[0]):
                rgbArray[i,j,0] = ima[i,j]/(256*256)
                rgbArray[i,j,1] = (ima[i,j]%(256*256))/256
                rgbArray[i,j,2] = (ima[i,j]%(256*256))%256
                #print(rgbArray[i,j,0], rgbArray[i,j,1], rgbArray[i,j,2])

        img = Image.fromarray(rgbArray)
        img.save(output_dir + str(k)+ '.tif') #change name

        
        
input_dir  = '/home/user1/Desktop/full_stack/segmentation_all_labels/0/seg-0_0_0.npz'
output_dir = '/home/user1/Desktop/full_stack/segmentation_all_labels/segmentation_1_6_6_5000/'


#just_blue(input_dir, output_dir)
just_blue(input_dir, output_dir)

