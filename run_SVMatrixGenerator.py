#!/bin/bash/python

# After actviating environment in O2 with conda activate SigProfiler

import os 
import sys 

from SigProfilerMatrixGenerator.scripts import SVMatrixGenerator as sv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 run.py [project]")
        sys.exit(1)

    project_name = sys.argv[1]
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "output", project_name)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Call your function
    generateSVMatrix(current_dir, project_name, output_dir)
