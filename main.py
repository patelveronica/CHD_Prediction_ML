from flask import Flask, render_template, request, iedirect, url_for
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
    chd_user.insert_one({
       init_features
    })
    final_features = [np.array(init_features)]
    # make prediction
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text= f' {prediction}.')

if __name__ == "__main__":
    app.run(debug=True)