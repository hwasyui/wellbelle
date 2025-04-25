from flask import Flask, render_template, request, jsonify
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import spacy
import random

# Load spaCy model for advanced NLP
nlp = spacy.load("en_core_web_sm")

# Flask app setup
app = Flask(__name__, static_folder="static", template_folder="templates")

# Load the dataset
with open("dataset/diseases.json") as file:
    diseases = json.load(file)

# Preprocess dataset
symptoms_data = [d["all_symptoms"] for d in diseases]
labels = [d["disease"] for d in diseases]

# Train the Naive Bayes model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(symptoms_data)
model = MultinomialNB()
model.fit(X, labels)

# Save the model and vectorizer for reuse
with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

# Dynamic response templates
RESPONSE_TEMPLATES = {
    "introduction": [
        "Hmm, based on your symptoms, it seems like you might be dealing with {disease}. Let me tell you more about it.",
        "After analyzing your symptoms, I think {disease} could be the issue. Here's what I found.",
        "It looks like {disease} might be the cause of your symptoms. Let me explain.",
        "From what you've described, {disease} seems to be the likely condition. Here's some information."
    ],
    "description": [
        "This condition is typically characterized by {description}",
        "People with this condition often experience {description}",
        "The main features of this condition include {description}",
        "Here's a bit more about it: {description}"
    ],
    "treatment": [
        "For treatment, I recommend {treatment}",
        "You might want to try {treatment} to manage this condition",
        "The usual approach to treating this is {treatment}",
        "Here's what you can do: {treatment}"
    ],
    "prevention": [
        "To prevent this in the future, consider {prevention}",
        "You can avoid this by {prevention}",
        "Prevention tips include {prevention}",
        "Here are some ways to prevent it: {prevention}"
    ],
    "closing": [
        "I hope this helps! Let me know if you have more questions.",
        "Feel free to ask if you need further assistance.",
        "Take care, and don't hesitate to reach out if you need more info.",
        "I'm here to help if you have any other concerns."
    ]
}

# Function to generate a dynamic, human-like response
def generate_response(disease_info):
    # Randomly select templates for each part
    introduction = random.choice(RESPONSE_TEMPLATES["introduction"]).format(disease=disease_info["disease"])
    description = random.choice(RESPONSE_TEMPLATES["description"]).format(description=disease_info["description"])
    treatment = random.choice(RESPONSE_TEMPLATES["treatment"]).format(treatment=disease_info["treatment"])
    prevention = random.choice(RESPONSE_TEMPLATES["prevention"]).format(prevention=disease_info["prevention"])
    closing = random.choice(RESPONSE_TEMPLATES["closing"])

    # Combine all parts into a single response
    response = f"{introduction} {description} {treatment} {prevention} {closing}"
    return response

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_diagnosis", methods=["POST"])
def get_diagnosis():
    data = request.get_json()
    symptoms = data.get("symptoms", "")
    if not symptoms:
        return jsonify({"error": "Please provide your symptoms."})

    # Load the model and vectorizer
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    # Transform user symptoms into vector
    user_symptoms_vector = vectorizer.transform([symptoms])
    prediction = model.predict(user_symptoms_vector)
    predicted_disease = prediction[0]

    # Fetch details of predicted disease
    for disease in diseases:
        if disease["disease"] == predicted_disease:
            response = generate_response(disease)
            return jsonify({"response": response})
    
    return jsonify({"error": "Could not identify the disease. Please try again."})

if __name__ == "__main__":
    app.run(debug=True)