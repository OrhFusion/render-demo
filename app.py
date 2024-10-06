from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and encoders
model = joblib.load('model.pkl')
gender_encoder = joblib.load('gender_encode')
smoking_history_encoder = joblib.load('smoking_history_encode')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        gender = request.form['gender']
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        smoking_history = request.form['smoking_history']
        bmi = float(request.form['bmi'])
        HbA1c_level = float(request.form['HbA1c_level'])
        blood_glucose_level = int(request.form['blood_glucose_level'])
        
        # Encode gender and smoking history
        gender_encoded = gender_encoder.transform([gender])[0]
        smoking_history_encoded = smoking_history_encoder.transform([smoking_history])[0]

        # Create array of features
        features = np.array([[age, gender_encoded, hypertension, heart_disease, smoking_history_encoded, bmi, HbA1c_level, blood_glucose_level]])
        
        # Make prediction
        prediction = model.predict(features)

        # Output
        if prediction == 1:
            result = "The model predicts that the patient is likely to have diabetes."
        else:
            result = "The model predicts that the patient is unlikely to have diabetes."
        
        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
