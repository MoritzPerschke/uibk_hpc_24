#!/bin/bash

#SBATCH --partition=lva
#SBATCH --job-name osu_benchmark
#SBATCH --exclusive
#SBATCH --error=errors/cores.log
#SBATCH --output=cores/latency/%j.log
#
#SBATCH --nodes=1
#SBATCH --ntasks=2

module load openmpi/3.1.6-gcc-12.2.0-d2gmn55
mpiexec --report-bindings --map-by core -n 2 ../osu_latency
