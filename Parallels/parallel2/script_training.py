import os

print(' \n' + ' \n' + "Training starting" + ' \n' + ' \n')

layer = 3
raw = 8
column = 8

path_constant = "/ibex/scratch/garnicj/parallel2"
path = "/ibex/scratch/garnicj/parallel2"

for k in range(layer):
    for i in range(column):
            for j in range(column):
                    if(i==j and k==1 and i<4):
                       continue
                    line = str(k) + '_' + str(i) + '_' + str(j) + '_' 
                    print("working on: " + line + ' \n' + ' \n')
                    command = ( "/home/garnicj/ksl-fernando/fernando_env/bin/python -u " + path_constant + "/ffn-master/train.py \\\
    --train_coords " + path + "/training_microglia4/tf_record_all_labels/tf_record_all_labels_" + line +" \\\
    --data_volumes validation1:" + path_constant + "/training_microglia4/grayscale_maps_all_labels/grayscale_maps_" + line +".hdf5:raw \\\
    --label_volumes validation1:" + path + "/training_microglia4/groundtruth_all_labels_uint8/all_labels_groundtruth_" + line +".hdf5:stack \\\
    --model_name convstack_3d.ConvStack3DFFNModel \\\
    --model_args \"{\\\"depth\\\": 12, \\\"fov_size\\\": [33, 33, 33], \\\"deltas\\\": [8, 8, 8]}\" \\\
    --image_mean  128 \\\
    --image_stddev 33") 
                    os.system(command)
