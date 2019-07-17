#!/bin/bash
#SBATCH -N 1
##SBATCH --partition=debug
#SBATCH --partition=batch
#SBATCH -J infer_l0_i6_j6_quarter
#SBATCH -o infer_l0_i6_j6_quarter.%J.out
#SBATCH -e infer_l0_i6_j6_quarter.%J.err
#SBATCH --mail-user=javierfernando.garnicamolina@kaust.edu.sa
#SBATCH --mail-type=ALL
#SBATCH --time=48:00:00
#SBATCH --mem=200G
#SBATCH --gres=gpu:1
#SBATCH --constraint=[v100]



module load anaconda3
source activate /home/garnicj/ksl-fernando/fernando_env/

#run the application
/home/garnicj/ksl-fernando/fernando_env/bin/python -u  /ibex/scratch/garnicj/parallel2/ffn-master/run_inference.py \
    --inference_request="$(cat /ibex/scratch/garnicj/parallel2/ffn-master/inference_sample.txt)" \
    --bounding_box 'start { x:0 y:0 z:0 } size { x:500 y:500 z:500 }'

