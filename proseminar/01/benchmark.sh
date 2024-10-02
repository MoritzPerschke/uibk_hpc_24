#!/bin/bash

# Name your job to be able to identify it later
#SBATCH --job-name osu_benchmark
# Execute job in the partition "lva" unless you have special requirements.
#SBATCH --partition=lva
# Redirect output stream to this file
#SBATCH --output=results/latency/different_nodes.log
# Redirect error stream to this file
#SBATCH --error=/dev/null
# Maximum number of tasks (=processes) to start in total
#SBATCH --ntasks=2
# Maximum number of tasks (=processes) to start per node
#SBATCH --ntasks-per-node=1
# Same Socket on one node
#SBATCH --nodes=2
##SBATCH --cpus-per-task=1
# Enforce exclusive node allocation, do not share with other jobs
#SBATCH --exclusive

module load openmpi/4.1.4-gcc-12.2.0-6gebvs6
mpiexec -n $SLURM_NTASKS ./osu_latency
