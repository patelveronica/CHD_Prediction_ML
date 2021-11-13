from flask import Flask, render_template, request
#from flask_cors import cross_origin
import pickle
import numpy as np

app = Flask(__name__, template_folder= 'Template')
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')    

# @app.route('/predict',methods=['POST'])
@app.route('/predict')
def predict():
        
    final_features = np.array([[0,20,0,0.0,0.0,0,1,0,110.0,110.0,70.0,22.0,70.0,100.0]])
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text= f' {prediction}.')

@app.route('/predict_api')
def predict_api():
    '''
    For direct API calls trought request
    '''
    final_features = np.array([[0,20,0,0.0,0.0,0,1,0,110.0,110.0,70.0,22.0,70.0,100.0]])
    prediction = model.predict(final_features)

    return (f'final_prediction: {prediction}')

if __name__ == "__main__":
    app.run(debug=True)