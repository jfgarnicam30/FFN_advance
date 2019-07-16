#!/bin/bash
#SBATCH -N 1
##SBATCH --partition=debug
#SBATCH --partition=batch
#SBATCH -J build_all_l1_2
#SBATCH -o build_all_l1_2.%J.out
#SBATCH -e build_all_l1_2.%J.err
#SBATCH --mail-user=javierfernando.garnicamolina@kaust.edu.sa
#SBATCH --mail-type=ALL
#SBATCH --time=5-00:00:00
#SBATCH --mem=116G
#SBATCH --gres=gpu:1
#SBATCH --constraint=[v100]


module load anaconda3
source activate /home/garnicj/ksl-fernando/fernando_env/


#run the application
/home/garnicj/ksl-fernando/fernando_env/bin/python -u /ibex/scratch/garnicj/parallel4/training_microglia4/script_coordinates.py
