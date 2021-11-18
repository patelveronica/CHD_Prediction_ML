from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from config import mongo_uri
import pickle
import numpy as np

app = Flask(__name__, template_folder= 'Template')
model = pickle.load(open('model.pickle', 'rb'))
app.config['MONGO'] = mongo_uri
mongo = PyMongo(app)
chd_user = mongo.db.chd_user_db

@app.route('/')
def home():
    saved_user = chd_user.find()
    return render_template('index.html', saved_userr=saved_todos)

@app.route('/predict',methods=['POST'])
# @app.route('/predict')
def predict():
        
    # final_features = np.array([[0,20,0,0.0,0.0,0,1,0,110.0,110.0,70.0,22.0,70.0,100.0]])
    # prediction = model.predict(final_features)
    # retrive values from Form
    init_features = [x for x in request.form.values()]
    column_list = ['gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
       'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
       'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD']
    for index, item in enumerate(init_features):
        userinput = {}
        userinput[column_list[index]] = item
    chd_user.insert_one({
       userinput
    })
    final_features = [np.array(init_features)]
    # make prediction
    prediction = model.predict(final_features)

    return redirect(url_for('index.html'))

if __name__ == "__main__":
    app.run(debug=True)