import pickle

with open("models/ingredient_analysis_pipeline.pkl", "rb") as f:
    ingredient_model = pickle.load(f)

def analyze_ingredients(text):
    return ingredient_model.predict([text])[0]
