import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import os
import warnings
warnings.filterwarnings("ignore", message="Trying to unpickle estimator LogisticRegression from version")


# Load models
# Use raw string literals or escape backslashes in file paths
heart_disease_model_path =heart_disease_model_path = r"c:\Users\user\multiple disease prediction system\saved models\heart_disease_model.sav.sav"

lung_cancer_model_path =r"c:\Users\user\multiple disease prediction system\saved models\lung_cancer_model.sav.sav"
diabetes_model_path =r"c:\Users\user\multiple disease prediction system\saved models\diabetes_model.sav.sav"
# Verify file paths
print("Heart Disease Model Path:", heart_disease_model_path)
print("Lung Cancer Model Path:", lung_cancer_model_path)
print("Diabetes Model Path:", diabetes_model_path)

# Load models
heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
lung_cancer_model = pickle.load(open(lung_cancer_model_path, 'rb'))
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))


with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                        ["Heart Disease", "Lung Cancer", "Diabetes"],
                        icons=['heart-pulse', 'lungs', 'activity'],
                        default_index=0)

# HEART DISEASE PREDICTION PAGE
if selected == "Heart Disease":
    st.title("Heart disease prediction using ML")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Cp')
    with col1:
        trestbps = st.text_input('Trestbps')
    with col2:
        chol = st.text_input('Chol')
    with col3:
        fbs = st.text_input('Fbs')
    with col1:
        restecg = st.text_input('Restecg')
    with col2:
        thalach = st.text_input('Thalach')
    with col3:
        exang = st.text_input('Exang')
    with col1:
        oldpeak = st.text_input('Oldpeak')
    with col2:
        slope = st.text_input('Slope')
    with col3:
        ca = st.text_input('Ca')
    with col1:
        thal = st.text_input('Thal')
    
    # Convert inputs to float
    age = float(age) if age else 0
    sex = float(sex) if sex else 0
    cp = float(cp) if cp else 0
    trestbps = float(trestbps) if trestbps else 0
    chol = float(chol) if chol else 0
    fbs = float(fbs) if fbs else 0
    restecg = float(restecg) if restecg else 0
    thalach = float(thalach) if thalach else 0
    exang = float(exang) if exang else 0
    oldpeak = float(oldpeak) if oldpeak else 0
    slope = float(slope) if slope else 0
    ca = float(ca) if ca else 0
    thal = float(thal) if thal else 0

   

    # Code for heart disease prediction
    heart_disease_diagnosis = ''
    if st.button('Heart Disease Result'):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_disease_prediction[0] == 1:
            heart_disease_diagnosis = "The patient has heart disease."
        else:
            heart_disease_diagnosis = "The patient does not have heart disease."
    st.success(heart_disease_diagnosis)

#CODE FOR LUNG CANCER PREDICTION PAGE
if selected == "Lung Cancer":
    st.title("Lung Cancer prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.text_input('Gender', key='gender_input')
        Gender = float(Gender) if Gender else None
        YellowFingers = st.text_input('YellowFingers', key='yellow_fingers_input')
        YellowFingers = float(YellowFingers) if YellowFingers else None
        Fatigue = st.text_input('Fatigue', key='Fatigue_input')
        Fatigue = float(Fatigue) if Fatigue else None
        Allergy = st.text_input('Allergy', key='Allergy_input')
        Allergy = float(Allergy) if Allergy else None
        AlcoholConsuming = st.text_input('AlcoholConsuming', key='alcohol_consuming_input')
        AlcoholConsuming = float(AlcoholConsuming) if AlcoholConsuming else None
        ChestPain = st.text_input('ChestPain', key='chest_pain_input')
        ChestPain = float(ChestPain) if ChestPain else None
    with col2:
        Age = st.text_input('Age', key='age_input')
        Age = float(Age) if Age else None
        Anxiety = st.text_input('Anxiety', key='anxiety_input')
        Anxiety = float(Age) if Anxiety else None
        PeerPressure = st.text_input('PeerPressure', key='peer_pressure_input')
        PeerPressure = float(PeerPressure) if PeerPressure else None
        Coughing = st.text_input('Coughing', key='coughing_input')
        Coughing = float(Coughing) if Coughing else None
        ShortnessofBreath = st.text_input('ShortnessofBreath', key='shortness_of_breath_input')
        ShortnessofBreath = float(ShortnessofBreath) if ShortnessofBreath else None
    with col3:
        Smoking = st.text_input('Smoking', key='smoking_input')
        Smoking = float(Smoking) if Smoking else None
        ChronicDisease = st.text_input('ChronicDisease', key='chronic_disease_input')
        ChronicDisease = float(ChronicDisease) if ChronicDisease else None
        Wheezing = st.text_input('Wheezing', key='wheezing_input')
        Wheezing = float(Wheezing) if Wheezing else None
        SwallowingDifficulty = st.text_input('SwallowingDifficulty', key='swallowing_difficulty_input')
        SwallowingDifficulty = float(SwallowingDifficulty) if SwallowingDifficulty else None



    # Code for lung cancer prediction
    lung_cancer_diagnosis = ''
    if st.button('Lung Cancer Result'):
        lung_cancer_prediction = lung_cancer_model.predict([[Gender, Age, Smoking, YellowFingers, Anxiety , PeerPressure, ChronicDisease, Fatigue, Allergy, Wheezing, AlcoholConsuming, Coughing, ShortnessofBreath, SwallowingDifficulty, ChestPain]])
        if lung_cancer_prediction[0] == 1:
            lung_cancer_diagnosis = "The patient has lung cancer."
        else:
            lung_cancer_diagnosis = "The patient does not have lung cancer."
    st.success(lung_cancer_diagnosis)


#DIABETES PREDICTION PAGE
if selected == "Diabetes":
    st.title("Diabetes prediction using ML") 

    # Obtain user inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = float(st.text_input('Pregnancies', key='pregnancies_input_diabetes') or 0)
        SkinThickness = float(st.text_input('SkinThickness', key='skin_thickness_input_diabetes') or 0)
        DiabetesPedigreeFunction = float(st.text_input('DiabetesPedigreeFunction', key='dpf_input_diabetes') or 0)
    with col2:
        Glucose = float(st.text_input('Glucose', key='glucose_input_diabetes') or 0)
        Insulin = float(st.text_input('Insulin', key='insulin_input_diabetes') or 0)
        Age = float(st.text_input('Age', key='age_input_diabetes') or 0)
    with col3:
       BloodPressure = float(st.text_input('BloodPressure', key='blood_pressure_input_diabetes') or 0)
       BMI = float(st.text_input('BMI', key='bmi_input_diabetes') or 0)

    # Code for diabetes prediction
    diabetes_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Diagnosis Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = "The patient has diabetes."
        else:
            diabetes_diagnosis = "The patient does not have diabetes"
    st.success(diabetes_diagnosis)