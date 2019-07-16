## Files contained in each Parallel directory.

As It was mentioned previously, the training process was carried out with our data on six GPUs. Each Parallel directory contains the files necessary to run the training. These files are grouped in two directories:
- ffn-master, contains all the scripts required to run the FFN algorithm. The only change did to this files was the one to the train.py file to get an output file (this change is described on the general readme). Because of storage limitations, the only file in this directory is train.py, the rest of the files can be downloaded from the FFN repository.
- training_microglia4, contains four files related to the second stage of the training (build_coordinates). The *.err* and *.out* files are the **notifications** of the second stage from Ibex. *jobscript_build_coordinates.sh* is the file submitted to IBEX to run our program. *script_soordinates.py* is a script called by *jobscript_build_coordinates.sh* to manage the input and ouput of the second stage.

## IBEX: Key notes 
IBEX is a cluster of CPUs and GPUs created to be used by the KAUST community interested on carrying on demanding computational tasks. The most relevant information to this project is described below. However, It is recommendable check the web-page of IBEX https://www.hpc.kaust.edu.sa/ibex . 
The way to access to this cluster is opening a console on your PC and typing: 

```
ssh user_name@vlogin.ibex.kaust.edu.sa
```

where user_name is the user name that KAUST provided you. The kind of login (ilogin, **vlogin**, glogin) depends on if you want use GPUs or CPUs, large or normal memory nodes or kind of GPUs. In this case *vlogin* is the login used to access to GPUs Volta 100 which work have 350 Gb of memory (It is strongly recommendable working on this login to avoid memory problems). Once you are on IBEX is also recommendable work from the path */ibex/scratch/user-name/* which provide a new and faster storage. To run a python script on IBEX is necessary code a script like this:

```

#!/bin/bash
#SBATCH -N 1
##SBATCH --partition=debug
#SBATCH --partition=batch
#SBATCH -J train_all
#SBATCH -o train_all.out
#SBATCH -e train_all.%J.err
#SBATCH --mail-user=javierfernando.garnicamolina@kaust.edu.sa
#SBATCH --mail-type=ALL
#SBATCH --time=5-00:00:00
#SBATCH --mem=100G
#SBATCH --gres=gpu:1
#SBATCH --constraint=[v100]



module load anaconda3
source activate /home/garnicj/ksl-fernando/fernando_env/

#run the application
/home/garnicj/ksl-fernando/fernando_env/bin/python -u /ibex/scratch/garnicj/parallel2/training_microglia4/script_training.py

```
