#!/bin/bash

#SBATCH --partition=lva
#SBATCH --job-name osu_benchmark
#SBATCH --exclusive
#SBATCH --error=errors/mpi_bandwidth.log
#SBATCH --output=mpi_bandwidth.log
#SBATCH --nodes=2
##SBATCH --ntasks=2

module load openmpi/3.1.6-gcc-12.2.0-d2gmn55
mpiexec --map-by node ../../osu_bw
