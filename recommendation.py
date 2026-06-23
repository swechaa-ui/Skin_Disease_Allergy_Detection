def generate_recommendation(image_result, symptom_result, ingredient_result, confidence):

    final_disease = image_result if confidence > 0.75 else symptom_result

    food_data = {
        "atopic_dermatitis": {
            "eat": ["Omega-3 foods", "Spinach", "Probiotics"],
            "avoid": ["Dairy", "Spicy food"]
        },
        "urticaria_hives": {
            "eat": ["Green vegetables", "Rice"],
            "avoid": ["Seafood", "Nuts"]
        }
    }

    recommendation = {
        "final_disease": final_disease,
        "ingredient_status": ingredient_result,
        "foods_to_eat": food_data.get(final_disease, {}).get("eat", []),
        "foods_to_avoid": food_data.get(final_disease, {}).get("avoid", [])
    }

    return recommendation
