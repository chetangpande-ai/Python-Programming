# Setup python virtual env
## `-p` or `--prefix`: Lets you specify the **full path** where the environment will be created.
conda create -p environment_name python=3.12

## `-n` or `--name`: Lets you specify an **environment name**. Conda stores it in its default environments folder.
conda create -n environment_name python 3.12

## List all python env available on your machine
conda env list

# Activate venv 
conda activate environment_name

# create requirements.txt with required python modules
pip install -r requirements.txt
pip install library_name
