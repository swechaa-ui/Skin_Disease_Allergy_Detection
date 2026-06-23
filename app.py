from flask import Flask, render_template, request
import os

from modules.symptom_module import predict_symptom
from modules.ingredient_module import analyze_ingredients
from modules.recommendation import generate_recommendation
from modules.gps_module import get_nearby_dermatologists

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    symptoms = request.form["symptoms"]
    ingredients = request.form["ingredients"]
    lat = request.form.get("lat")
    lon = request.form.get("lon")

    # Predict disease from symptoms
    symptom_result = predict_symptom(symptoms)

    # Analyze skincare ingredients
    ingredient_result = analyze_ingredients(ingredients)

    # Generate recommendations
    recommendations = generate_recommendation(
        symptom_result,
        symptom_result,
        ingredient_result,
        1.0
    )

    # Find nearby dermatologists
    doctors = []
    if lat and lon:
        doctors = get_nearby_dermatologists(lat, lon)

    return render_template(
        "result.html",
        disease=symptom_result,
        confidence=100,
        symptom_result=symptom_result,
        ingredient_result=ingredient_result,
        recommendations=recommendations,
        doctors=doctors
    )


if __name__ == "__main__":
    app.run(debug=True)