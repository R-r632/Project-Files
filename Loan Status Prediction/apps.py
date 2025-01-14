from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load('loan_status_predictor_model')

# Route for the HTML page
@app.route('/')
def index():
    return render_template('indexx.html')

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse form data from the request
        data = {
            "Gender": float(request.form['Gender']),
            "Married": float(request.form['Married']),
            "Dependents": float(request.form['Dependents']),
            "Education": float(request.form['Education']),
            "Self_Employed": float(request.form['Self_Employed']),
            "ApplicantIncome": float(request.form['ApplicantIncome']),
            "CoapplicantIncome": float(request.form['CoapplicantIncome']),
            "LoanAmount": float(request.form['LoanAmount']),
            "Loan_Amount_Term": float(request.form['Loan_Amount_Term']),
            "Credit_History": float(request.form['Credit_History']),
            "Property_Area": float(request.form['Property_Area'])
        }

        # Convert input data to a DataFrame
        df = pd.DataFrame([data])

        # Make a prediction
        prediction = model.predict(df)

        # Generate the result message
        result_message = "Loan Approved" if prediction[0] == 1 else "Loan Not Approved"

        return render_template('index.html', prediction=result_message)
    except Exception as e:
        return render_template('index.html', error=str(e))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
