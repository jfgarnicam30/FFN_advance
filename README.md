# FFN_advance
You will find some scripts coded to run the different steps of FFN (https://github.com/google/ffn). Some of these scripts are written on the Jupyter Notebook, so... in order to make easy the explanation of these codes I suggest you download and install a jupyter notebook.
Below I describe the requirements of each step of the FFN pipeline.

## Training
The training process is formed by three stages, the first two are in charge of generating training coordinate files for a labeled dataset stored in HDF5 files. These are compute_partitions.py, build_coordidates.py, stage_1 and stage_ 2, respectively. Stage_3 is the training itself. The python notebook named stages_1_2_3.ipynb describes the scripts coded to run these stages.

### Important notes:

- The goundtruth files are HDF5 files. A HDF5  is a container for two kinds of objects: datasets, which are array-like collections of data, and groups, which are folder-like containers that hold datasets and other groups. On python, a HDF5 is a kind of dictionary. Then, it has several keys. Each key represents a diferent dataset. Groundtruth datasets are storaged under the name of “stack” while Grayscale_maps are storaged under the name of “raw”. Be careful to use this notation in order to avoid errors.
- To create HDF5 files from .TIF datasets (which is the most common dataset used on the group) use the python notebook named create_hdf5_files.ipynb. It has different kinds of create these hdf5 files. 
- Watch out!, the background of the images in the groundtruth datasets is white while the segmentation areas are black.

It is very important run stage 1, 2 on GPUs. If they are run on CPUs there will be incompatibility problems in stage 3.

In order to replicate the work  carried out by Google in the FFN training, our dataset was split into sub-volumes of 500 images of 500x500 pixels each one.  To make paralell the training I made 6 groups (each group has 32 sub-volumes), and each group run in a single GPU. It is possible make more groups in order to make faster the training. Each group was set up in a specific  directory (See files Parallel1, Parallel2, Parallel3, Parallel4, Parallel5, Parallel6 ). 

Each file contains a ffn_master file with all the scripts related to FFN algorithm. The only script which is different to the original one (the one downloaded from Google) is the `train.py`, this one was modified to create an output file. If you want to change the output path, go to the line related on this script and write the path you need. 
```
flags.DEFINE_string('train_dir', 
    '/ibex/scratch/garnicj/parallel2/training_microglia4/models_all_labels', 
    'Path where checkpoints and other data will be saved.')
```

The Parallel files contains another directory  called “training_microglia4”. This contains the scripts necessary to run the algorithm on IBEX. Grayscale maps, groundtruth, af and coordinates directories are in Parallel2. Refer to the Readme.md on Paralle2 to read the explanation about the different files and scripts in the several Parallel directories. 

Key notes on the different stages of FFN are described on the README of Parallels
