from flask import Flask, request, redirect, render_template, url_for, flash 
import pickle
import pandas as pd
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

app = Flask(__name__)

# load the model
model = pickle.load(open('svc_model.pkl', 'rb'))
#dataset = pd.read_csv('jobs_dataset_latest.csv')

@app.route("/")
def home():
    return redirect(url_for('skill_picker'))

@app.route("/skillmatch/", methods=['GET', 'POST'])
def skill_picker():
    if request.method == 'POST':
        # retrieve the selected skills from the form
        selected_skills = request.form.getlist('skills')
        # start with all values in the array at 0
        skills_index = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # now update the index for each of the selected values to 1 - ready to be passed to the model
        for i in selected_skills:
            skills_index[int(i)] = 1
        # the array now represents the selected values in 0 and 1 

        # check at least one skill has been selected - return error message if not
        if skills_index == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
            return render_template("skills_picker.html", error='Please select skills')
            
        # call the predict method, passing in the selected skills array    
        return redirect(url_for('predict', selected=skills_index))

    return render_template(
        "skills_picker.html"
    )

@app.route("/skills/<selected>", methods=['GET', 'POST'])
def predict(selected):
    # mapped Ids of each role
    mapped_roles = {0: 'Account Manager',
1: 'Analyst',
2: 'Technical Architect',
3: 'Consultant',
4: 'Designer',
5: 'Software Developer',
6: 'Digital Marketing Executive',
7: 'Software Engineer',
8: 'Project Manager',
9: 'Technical Manager',
10: 'Technician'
}
    # format the data to be passed into the model
    skills = selected
    skills = skills.replace('[', "")
    skills = skills.replace(']', "")
    skills = skills.split(',')
    
    # get the prediction
    prediction = model.predict(pd.DataFrame([skills]))

    # map the prediction to the relevant string
    prediction_string = mapped_roles[prediction[0]]

    # start again button click
    if request.method == 'POST':
        return redirect(url_for('skill_picker'))

    # pass the predicted role to the results page
    return render_template(
        "result.html",result=prediction_string)