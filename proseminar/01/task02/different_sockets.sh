#!/bin/bash

#SBATCH --partition=lva
#SBATCH --job-name osu_benchmark
#SBATCH --exclusive
#SBATCH --error=/dev/null
#SBATCH --output=bandwidth/sockets.log
#
#SBATCH --nodes=1
#SBATCH --ntasks=2

module load openmpi/3.1.6-gcc-12.2.0-d2gmn55
mpiexec --map-by socket ../osu_bw
