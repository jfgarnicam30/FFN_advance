import os

print(' \n' + ' \n' + "Build coordinates starting" + ' \n' + ' \n')

layer = 1
raw = 0
column = 0

path = "/ibex/scratch/garnicj/parallel3"
constant_path = "/ibex/scratch/garnicj/parallel2"    

for i in range(4):
        for j in range(8):
                line = str(layer) + '_' + str(raw+i) + '_' + str(column+j) + '_' 
                print("working on: " + line + ' \n' + ' \n')
                command = ("/home/garnicj/ksl-fernando/fernando_env/bin/python -u " + path + "/ffn-master/build_coordinates.py \
--partition_volumes validation1:" + constant_path + "/training_microglia4/af_all_labels/af_all_labels_" + line +".h5:af \
--coordinate_output " + constant_path + "/training_microglia4/tf_record_all_labels/tf_record_all_labels_" + line +" \
--margin 24,24,24")
                os.system(command)
