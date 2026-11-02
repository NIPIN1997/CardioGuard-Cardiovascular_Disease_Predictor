# CardioGuard 
A web application that predicts the risk of developing cardio vascular diseases using machine learning.

## Data
The columns of the dataset are:
1. **id** - Unique identifier for each patient
2. **age** - Age of patient in days
3. **gender** - Gender of the patient. Categorical variable(1: Female, 2: Male)
4. **height** - Height of the patient in centimeters
5. **weight** - Weight of the patient in kilograms
6. **ap_hi** - Systolic blood pressure
7. **ap_lo** - Diastolic blood pressure
8. **cholesterol** - Cholesterol levels. Categorical variable(1: Normal, 2: Above Normal, 3: Well Above Normal).
9. **gluc** - Glucose levels. Categorical variable (1: Normal, 2: Above Normal, 3: Well Above Normal).
10. **smoke** - Smoking status. Binary variable (0: Non-smoker, 1: Smoker).
11. **alco** - Alcohol intake. Binary variable (0: Does not consume alcohol, 1:Consumes Alcohol)
12. **active** - Physical activity. Binary variable (0: Not physically active, 1: Physically active)
13. **cardio** - Presence or absence of cardiovascular disease. Binary variable (0: Absence, 1: Presence).Target variable.
14. **age_years** - Age of the patient in years(derived from age)
15. **bmi** - Body Mass Index, derived from weight and height.
16. **bp_category** - Blood pressure category based on ap_hi and ap_lo. Categories include "Normal", "Elevated", "Hypertension Stage 1", "Hypertension Stage 2", and "Hypertensive Crisis".
17. **bp_category_encoded** -  Encoded form of bp_category for machine learning purposes.

## Preprocessing
The following preprocessing steps were performed on the dataset.
1. Checking for duplicate rows. (There were no duplicate rows in the dataset)
2. Checking for missing values. (There were no missing values in the dataset)
3. Outlier were identified using the IQR method and the outliers were removed.
4. Skewness of features were checked, only ap_hi was positively skewed but since it is a medical parameter no transformation was applied to this column.
5. The columns age, bp_category and id were removed.
6. The bp_category column was encoded using OrdinalEncoder.
7. The dataset was scaled using StandardScaler.

## Model Training
Multiple classification models were trained using the dataset and the performance parameters were calculated for each model. Based on accuracy the two best models were LGBM Classifier and Voting Classifier.

## Hyper Parameter Tuning
The two models selected were subjected to hyperparameter tuning and LGBM Classifier was identified as the best model based on accuracy.

## Saving the Model
The trained model and scaler was saved.

## User Interface
A user interface for this application was created using streamlit.

## Deployment
The app has been deployed using Streamlit Community Cloud.

url - https://cardioguard-cardiovasculardiseasepredictor-gy7gycg8ykkabhgwjwu.streamlit.app/