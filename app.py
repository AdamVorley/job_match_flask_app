from flask import Flask, request, redirect, render_template, url_for
import pickle
import pandas as pd
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

app = Flask(__name__)

model = pickle.load(open('svc_model.pkl', 'rb'))
dataset = pd.read_csv('jobs_dataset_latest.csv')

@app.route("/")
def home():
    return "Test"


@app.route("/skillmatch/", methods=['GET', 'POST'])
def skill_picker():
    if request.method == 'POST':
        selected_skills = request.form.getlist('skills')
        # checking we have retrieved all the selected skills from the form
        #print(selected_skills)
        # start with all values in the array at 0
        skills_index = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # now update the index for each selected value to 1 - ready to be passed to the model
        for i in selected_skills:
            skills_index[int(i)] = 1
        # the array now represents the selected values in 0 and 1 
        #print(skills_index)
        return redirect(url_for('predict', selected=skills_index))

    return render_template(
        "skills_picker.html"
    )

@app.route("/skills/<selected>", methods=['GET', 'POST'])
def predict(selected):
    # mapped Ids of each role
    mapped_roles = {0: 'Account Manager',
1: 'Analyst',
2: 'Architect',
3: 'Consultant',
4: 'Designer',
5: 'Developer',
6: 'Digital Marketing Executive',
7: 'Engineer',
8: 'Project Manager',
9: 'Technical Manager',
10: 'Technician'
}
    skills = selected  
    skills = skills.replace('[', "")
    skills = skills.replace(']', "")
    skills = skills.split(',')
 #   print("Datatype:")
 #   print(type(skills))
    features = ['literacy','problem_solving','organised','collaboration','communication','analytical','maths','leadership','time_management','fast_learner','creative','attention_to_detail','motivated','adaptable','decision_making','project_management','customer_service'] 
    
    # get the prediction
    prediction = model.predict(pd.DataFrame([skills]))

    # map the prediction to the relevant string
    prediction_string = mapped_roles[prediction[0]]

    # pass the predicted role to the results page
    return render_template(
        "result.html",result=prediction_string)