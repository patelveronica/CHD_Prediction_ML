from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder= 'Template')
model = pickle.load(open('model.pickle', 'rb'))

# create app route
@app.route('/')
def home():

    # read the csv file
    prediction_information = pd.read_csv("result.csv")
    # model_list = []
    # for information in prediction_information.iloc[0]:
    #     model_list.append(information)
    # model_list = [float(x) for x in model_list]    
    final_features = np.array(prediction_information.to_numpy())
    #make prediction
    prediction = model.predict(final_features)
            
    return render_template('index.html', prediction_text = prediction)

@app.route('/predict',methods=['POST'])
def predict():
    init_features = [x for x in request.form.values()]
    column_list = ['male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds',
       'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
       'diaBP', 'BMI', 'heartRate', 'glucose']
    results = pd.DataFrame([init_features], columns = column_list)
    results.to_csv("result.csv", index = False)
    for index, item in enumerate(init_features):
        userinput = {}
        userinput[column_list[index]] = item

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)