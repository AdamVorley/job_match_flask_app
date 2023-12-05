# Job Match Application

This appliation has been developed for the deployment of a Machine Learning model which will match and return job roles in the tech industry based on a set of soft skills provided by the user.

The application folder includes the original Jupyter notebook in which the model is trained and tested, as well as the original dataset provided (jobs_and_skills.csv), and the manipulated dataset that was used to train the model (jobs_dataset_latest.csv). 

## Installation
The application will need to be run locally in a flask virtual environment

#### Prerequisites
- VSCode
- Python (3.12) installed on your machine

#### Reproduce environment and run project
- Open the project in VSCode
- In VSCode, open the command palette using Ctrl+Shift+P and select *Python: Create Environment*. Select *venv* and the Python environment you wish to use.
- Open a VSCode terminal and install flask in the virutal environment using:
```bash
pip install flask
```
- You should now be able to run the application using:
```bash
python -m flask run
```
- You will now be prompted to navigate to the localhost in the terminal

## Using the application
The application is made up of a simple interface which allows the user to select a set of soft skills through a list of checkboxes. After submitting their selection, the user will be directed to a page with the job role most closely matched to their skills, using the Machine Learning model that has been deployed.