![Home Page](https://github.com/OrhFusion/Diabetes-Prediction-Model/blob/prediction/Images/Home.png)


![Form Page](https://github.com/OrhFusion/Diabetes-Prediction-Model/blob/prediction/Images/Form.png)


## Machine Learning Experiment Tracking and Deployment with MLflow

This project showcases the full cycle of a machine learning pipeline, focusing on **experiment tracking, model deployment, and containerization**. The combination of **MLflow** for tracking, **Flask** for serving, and **Docker** for seamless execution makes it a powerful and efficient solution.

### Experiment Tracking with MLflow:
- Effortlessly log and track **experiments, metrics, and models** using MLflow.
- Gain insights into model performance with detailed logs of each experiment iteration.
- Keep track of model improvements, and compare metrics over time to ensure the best-performing model is deployed.

### Model Deployment:
- Save your trained model and associated encoders with **joblib** for efficient loading during prediction.
- Build an intuitive **Flask web application** to allow users to submit inputs and receive predictions instantly.
- From user inputs to real-time predictions, the web app provides a smooth and interactive experience.

### Dockerfile:
- Simplify model deployment with Docker. Forget about manually setting up environments and libraries!
- Simply pull the Docker image from DockerHub, and run the model in a **completely self-contained environment**.
- No need to worry about dependencies or package installation—just **copy and paste the DockerHub link** (available at the end of the notebook) into your terminal, and the model is ready to go!


## This is a Basic End-to-End Diabetes Prediction Model

The notebook provides a comprehensive example of a machine learning pipeline, from data exploration to deployment, enabling users to understand and replicate the process for similar tasks, especially focusing on diabetes prediction based on patient features.

### Pull Image from DockerHub:  
**docker pull orhfusion/diabetes-predict-model**

*Run without installing any dependencies & no need to create an environment for it...*

### Or you can refer to my GitHub repository to get the files:  
[https://github.com/OrhFusion/Diabetes-Prediction-Model.git](https://github.com/OrhFusion/Diabetes-Prediction-Model.git)

The repository contains:
- **Flask**
- **HTML**
- **Dockerfile**
- **app.py**
- **Details**
- **Dependencies (requirements.txt)**

### Exposed:  
**Port**: 5000

---

### Dataset Preview (Diabetes Dataset)

| gender | age  | hypertension | heart_disease | smoking_history | bmi   | HbA1c_level | blood_glucose_level | diabetes |
|--------|------|--------------|---------------|-----------------|-------|-------------|---------------------|----------|
| 0      | 80.0 | 0            | 1             | 4               | 25.19 | 6.6         | 140                 | 0        |
| 0      | 54.0 | 0            | 0             | 0               | 27.32 | 6.6         | 80                  | 0        |
| 1      | 28.0 | 0            | 0             | 4               | 27.32 | 5.7         | 158                 | 0        |
| 0      | 36.0 | 0            | 0             | 1               | 23.45 | 5.0         | 155                 | 0        |
| 1      | 76.0 | 1            | 1             | 1               | 20.14 | 4.8         | 155                 | 0        |
| 0      | 20.0 | 0            | 0             | 4               | 27.32 | 6.6         | 85                  | 0        |






![Footer](https://github.com/OrhFusion/Diabetes-Prediction-Model/blob/prediction/Images/Footer.png)
