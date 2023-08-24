from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load your pre-trained regression model
        model = pickle.load(open("model.pkl", "rb"))

        # Get input values from the form
        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        residual_sugar = float(request.form['residual_sugar'])
        chlorides = float(request.form['chlorides'])
        freesulfurdioxide = int(request.form['freesulfurdioxide'])
        totalsulfurdioxide = int(request.form['totalsulfurdioxide'])
        density = float(request.form['density'])
        ph = float(request.form['ph'])
        sulphates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])

        # Perform prediction
        features = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, freesulfurdioxide, totalsulfurdioxide, density, ph, sulphates, alcohol]).reshape(1, -1)
        prediction = model.predict(features)

        # Return the prediction as a response
        if prediction[0] == 1:
            result = 'Good Quality Wine'
        else:
            result = 'Bad Quality Wine'

        return render_template('index.html', result=result)

    except Exception as e:
        error_message = f"Prediction failed. Error: {str(e)}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)