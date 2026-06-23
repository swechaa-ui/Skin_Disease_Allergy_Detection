import pickle

with open("models/symptom_analysis_pipeline.pkl", "rb") as f:
    symptom_model = pickle.load(f)

def predict_symptom(text):
    return symptom_model.predict([text])[0]
