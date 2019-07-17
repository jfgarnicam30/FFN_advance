#!/usr/bin/env python
# coding: utf-8

# # Scripts

# We can devide the FFN training process in three stages, the first two are in charge of generating training coordinate files for a labeled dataset stored on HDF5 files. These are compute_partitions.py, build_coordidates.py, stage_1 and stage_ 2, respectively. Stage_3 is the training itself.
# 
# Next scripts launch the scripts related to the different stages. A string called "command" is executed by the shell. This command change in each iteration according three variables l,i and j. These three numbers represent a coordinate of each subvolume in our data_set. Our data_set was split in 8x8x3 = 192 subvolumes. Each one has 500 images, each image is 500x500 pixels. So, each subvolume is 500x500x500. l is the layer, i is the row and j is the column. 
# 
# The objective with these scripts is launching the stage_1 _2 and _3 over several subvolumes automatically. These scripts can be run from different directories in order to run the full pipeline in a "parallel" manner.

# # Stage_1: Compute partitions

# In[ ]:


print("Compute starting" + ' \n' + ' \n')

layer = 2
raw = 3
column = 3

path = "/ibex/scratch/garnicj/parallel4"
    
for i in range(3):
        for j in range(3):
                line = str(layer) + '_' + str(raw+i) + '_' + str(column+j) + '_' 
                print("working on: " + line + ' \n' + ' \n')
                command =  "/home/garnicj/ksl-fernando/fernando_env/bin/python -u " + path + "/ffn-master/compute_partitions.py --input_volume " + path + "/training_microglia4/groundtruth/groundtruth_" + line + ".hdf5:stack --output_volume " + path + "/training_microglia4/af/af_" + line +".h5:af --thresholds 0.025,0.05,0.075,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9 --lom_radius 24,24,24 --min_size 10000"


# # Stage_2: Build Coordinates

# In[ ]:


print(' \n' + ' \n' + "Build coordinates starting" + ' \n' + ' \n')

layer = 0
raw = 3
column = 3

path = "/ibex/scratch/garnicj/parallel2"
    
for i in range(3):
        for j in range(3):
                line = str(layer) + '_' + str(raw+i) + '_' + str(column+j) + '_' 
                print("working on: " + line + ' \n' + ' \n')
                command = ("/home/garnicj/ksl-fernando/fernando_env/bin/python -u " + path + "/ffn-master/build_coordinates.py --partition_volumes validation1:" + path + "/training_microglia4/af_" + line +".h5:af --coordinate_output " + path + "/training_microglia4/tf_record/tf_record_" + line +" --margin 24,24,24")


# # Stage_3: Training 

# In[3]:


import os

print(' \n' + ' \n' + "Training starting" + ' \n' + ' \n')

layer = 3
raw = 3
column = 3

path_constant = "/ibex/scratch/garnicj/parallel2"
path = "/ibex/scratch/garnicj/parallel2"

model_args = ""

for k in range(layer):
    if(k==0): 
        path = "/ibex/scratch/garnicj/parallel2"
    if(k==1): 
        path = "/ibex/scratch/garnicj/parallel3"
    if(k==2): 
        path = "/ibex/scratch/garnicj/parallel4"
    for i in range(raw):
            for j in range(column):
                    line = str(k) + '_' + str(raw+i) + '_' + str(column+j) + '_' 
                    print("working on: " + line + ' \n' + ' \n')
                    command = ( "/home/garnicj/ksl-fernando/fernando_env/bin/python -u " + path_constant + "/ffn-master/train.py \\    --train_coords " + path + "/training_microglia4/tf_record/tf_record_" + line +" \\    --data_volumes validation1:" + path + "/training_microglia4/grayscale_maps/grayscale_maps_" + line +".hdf5:raw \\    --label_volumes validation1:" + path + "/training_microglia4/groundtruth/groundtruth_" + line +".hdf5:stack \\    --model_name convstack_3d.ConvStack3DFFNModel \\    --model_args \"{\\\"depth\\\": 12, \\\"fov_size\\\": [33, 33, 33], \\\"deltas\\\": [8, 8, 8]}\" \\    --image_mean  128 \\    --image_stddev 33") 
                    #print(command)  


# In[ ]:





# In[ ]:




