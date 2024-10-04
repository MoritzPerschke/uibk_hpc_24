#!/bin/bash

#SBATCH --partition=lva
#SBATCH --job-name test
#SBATCH --output=slurm_bandwith.log
#SBATCH --error=errors/slurm_bandwidth.log
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive

module load openmpi/3.1.6-gcc-12.2.0-d2gmn55
mpiexec -n $SLURM_NTASKS ../../osu_bw
