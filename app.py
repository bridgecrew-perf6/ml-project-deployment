import numpy as np
import flask
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('log_reg.pickle', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predicts():

    # int_features = [float(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # print(final_features)
    # prediction = model.predict(final_features)
    inputs = []

    inputs.append(request.form['age'])
    inputs.append(request.form['Anaemia'])
    inputs.append(request.form['creatinine_phosphokinase'])
    inputs.append(request.form['Diabetes'])
    inputs.append(request.form['ejection_fraction'])
    inputs.append(request.form['High_blood_pressure'])
    inputs.append(request.form['platelets'])
    inputs.append(request.form['serum_creatinine'])
    inputs.append(request.form['serum_sodium'])
    inputs.append(request.form['sex'])
    inputs.append(request.form['smoking'])

    final_inputs = [np.array(inputs)]
    prediction = model.predict(final_inputs)

    if(prediction[0] == 1):
        return render_template('index.html', predicted_result='Death occured')

    if(prediction[0] == 0):
        return render_template('index.html', predicted_result='Death not occured')


if __name__ == "__main__":
    app.run(debug=True)
