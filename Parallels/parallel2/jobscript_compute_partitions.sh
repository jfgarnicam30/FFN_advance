#!/bin/bash
#SBATCH -N 1
##SBATCH --partition=debug
#SBATCH --partition=batch
#SBATCH -J compute_all
#SBATCH -o compute_all.%J.out
#SBATCH -e compute_all.%J.err
#SBATCH --mail-user=javierfernando.garnicamolina@kaust.edu.sa
#SBATCH --mail-type=ALL
#SBATCH --time=05:00:00
#SBATCH --mem=150G
#SBATCH --gres=gpu:1
#SBATCH --constraint=[v100]


module load anaconda3
source activate /home/garnicj/ksl-fernando/fernando_env/



#run the application
/home/garnicj/ksl-fernando/fernando_env/bin/python -u /ibex/scratch/garnicj/parallel2/training_microglia4/script_compute.py
