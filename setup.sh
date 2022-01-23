# Setup new conda env
conda create -n microarray python pip

# Enter the new environment
conda activate microarray

# Install the packages
pip3 install -r requirements.txt

# Start Jupyter Lab
jupyter-lab