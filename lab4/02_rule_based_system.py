def medical_advice(symptoms):
    # Educational rule example only; it is not a diagnosis.
    if "fever" in symptoms and "cough" in symptoms:
        return "Possible flu-like illness. Consider medical advice."
    if "headache" in symptoms and "tiredness" in symptoms:
        return "Rest and hydration may help; seek advice if it continues."
    if "sneezing" in symptoms:
        return "Could be an allergy or common cold."
    return "No matching rule. More information is needed."

entered = input("Enter symptoms separated by commas: ").lower()
symptoms = {item.strip() for item in entered.split(",") if item.strip()}
print(medical_advice(symptoms))
