import os
import logging
from pathlib import Path

# Set up logging to both console and file
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)  # Create logs folder if it doesn't exist

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:', handlers=[
    logging.StreamHandler(),  # Output to console
    logging.FileHandler(os.path.join(log_folder, 'logfile.log'))  # Output to file or log folder
])


project_name = "src"

list_of_files = [
    # main folders
    f"incomepredictor/{project_name}/__init__.py",
    f"research/__init__.py",

    # src subfolders
    f"incomepredictor/{project_name}/components/__init__.py",
    f"incomepredictor/{project_name}/utils/__init__.py",
    f"incomepredictor/{project_name}/config/__init__.py",
    f"incomepredictor/{project_name}/pipeline/__init__.py",
    f"incomepredictor/{project_name}/entity/__init__.py",
    f"incomepredictor/{project_name}/constants/__init__.py",

    # src subfolders tree
    f"incomepredictor/{project_name}/utils/common.py",
    f"incomepredictor/{project_name}/config/configuration.py",
    f"incomepredictor/{project_name}/entity/config_entity.py",



    # yaml files/folders
    "params.yaml",
    "schema.yaml",
    "config/config.yaml",

    # .py files
    "setup.py",
    "app.py",
    "main.py",

    #other files and folders
    "Dockerfile",
    "requirements.txt",
    "templates/index.html",
    

]

for filepath in list_of_files:
    filepath=Path(filepath)

    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")

    else:
        logging.info(f"File: {filepath} already exists")

