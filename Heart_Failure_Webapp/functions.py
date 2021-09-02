# convert non-numeric inputs
def convert(feature):
    features = request.POST.get(feature)
    if features == 'Yes':
        features = 1
    elif features == 'No':
        features = 0
    else:
        features = 0

    return features

# get prediction
def getPrediction(age, anaemia, diabetes, high_blood_pressure, serum_creatinine, smoking):
    import pickle
    # loading saved model
    with open('Heart_Failure_Webapp/saved_model.sav', 'rb') as model_file:
        model = pickle.load(model_file)
    # loading saved scaler
    with open('Heart_Failure_Webapp/scaler.sav', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
        
    # prediction
    prediction = model.predict(scaler.transform(
        [[age, anaemia, diabetes, high_blood_pressure, serum_creatinine, smoking]]
        ))

    if prediction == 1:
        return 'Patient is likely to suffer a heart failure 😢'
    elif prediction == 0:
        return 'Patient is safe from heart failure! 🥳🎉'
    else:
        return 'Error: Prediction failed. Try again.'