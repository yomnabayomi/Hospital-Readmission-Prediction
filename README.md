# Hospital Readmission Prediction

## Project Overview
The **Hospital Readmission Prediction** project aims to predict whether a patient is likely to be readmitted within 30 days after discharge based on historical medical records. This helps hospitals improve patient care, reduce unnecessary readmissions, and optimize resource allocation.

## Features & Dataset
- Dataset includes patient demographics, diagnoses, medications, admission/discharge data, and readmission outcomes.  
- Key features:
  - Patient demographics (age, gender)
  - Diagnosis codes
  - Medications prescribed
  - Admission and discharge details
  - Historical readmission events

## Methodology
1. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical variables
   - Resampling imbalanced data using SMOTE
2. **Exploratory Data Analysis (EDA)**
   - Identifying important features influencing readmission
   - Visualizing distributions, correlations, and trends
3. **Model Training**
   - Logistic Regression
   - Random Forest Classifier
   - Decision Tree Classifier
4. **Evaluation**
   - Accuracy, Precision, Recall, F1-score
   - Comparison of models to select the best-performing one

## Key Contributions
- Developed a machine learning model to predict hospital readmissions using structured patient data (diagnoses, medications, admission history).  
- Implemented and tuned a **Decision Tree classifier**, evaluating accuracy, recall, and precision, and visualized the tree to interpret feature splits and improve         explainability.  
- Collaborated on model comparison with **Logistic Regression** and **Random Forest** to assess trade-offs in performance and interpretability.  
- Conducted data preprocessing including missing value handling, encoding, and resampling (SMOTE).  
- Performed exploratory data analysis (EDA) to uncover insights on factors contributing to hospital readmission.  

## Tools & Libraries
- Python (Pandas, NumPy)
- Scikit-learn (for ML models)
- Matplotlib & Seaborn (for visualization)
