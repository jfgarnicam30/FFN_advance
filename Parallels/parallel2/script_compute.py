import os


print("test starting" + ' \n' + ' \n')

layer = 3
raw = 8
column = 8

path = "/ibex/scratch/garnicj/parallel2"

for k in range(layer):    
  for i in range(raw):
          for j in range(column):
                  line = str(k) + '_' + str(i) + '_' + str(j) + '_' 
                  print("working on: " + line + ' \n' + ' \n')
                  command =  "/home/garnicj/ksl-fernando/fernando_env/bin/python -u " + path + "/ffn-master/compute_partitions.py \
  --input_volume " + path + "/training_microglia4/groundtruth_all_labels/all_labels_groundtruth_" + line + ".hdf5:stack \
  --output_volume " + path + "/training_microglia4/af_all_labels/af_all_labels_" + line +".h5:af \
  --thresholds 0.025,0.05,0.075,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9 \
  --lom_radius 24,24,24 \
  --min_size 10000"
                  os.system(command)	

print("finished")
