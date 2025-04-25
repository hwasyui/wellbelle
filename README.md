# 💡 WellBelle - Disease Detection and Prevention Chatbot

**WellBelle** is a machine-learning powered application that detects potential diseases based on user input symptoms and provides preventive measures. It uses a **Naive Bayes** classifier to predict diseases and generates dynamic responses that inform users about treatment and prevention.

## 🧠 Features
- **Symptom-Based Disease Detection**: Based on user input symptoms, WellBelle predicts the likely disease.
- **Dynamic Responses**: The chatbot generates human-like responses with details about the disease, treatment, and prevention.
- **Prevention Tips**: After diagnosing, it offers practical advice on how to prevent the condition in the future.

## 🧑‍🤝‍🧑 Collaborators

This project was developed collaboratively by the following team members:

| Name                  | GitHub                                          |
|-----------------------|------------------------------------------------|
| **Angelica Suti Whiharto** | [@hwasyui](https://github.com/hwasyui)         |
| **Intan Kumala Pasya**     | [@tannpsy](https://github.com/tannpsy)     |
| **Muh. Fakhri Hisyam Akbar**     | [@Grayzero15](https://github.com/Grayzero15)     |

---

## ⚙️ Installation and Setup

### Requirements:
- Python 3.8+
- Flask
- Scikit-learn
- spaCy
- OpenCV (optional for image processing)
- NumPy

### Setup Instructions:
1. Clone the repository:
    ```bash
    git clone https://github.com/hwasyui/wellbelle.git
    cd wellbelle
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the spaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Visit the app in your browser at `http://127.0.0.1:5000/`.

---

## 🧑‍⚕️ How It Works:
1. **Input Symptoms**: The user provides symptoms in a natural language format (e.g., "I have a fever and a headache").
2. **Model Prediction**: The application uses a **Naive Bayes** classifier to predict the likely disease based on the input.
3. **Response Generation**: The chatbot dynamically generates a response, detailing the disease, treatment options, and prevention tips.
4. **Personalized Prevention**: Along with diagnosis, the system offers tips on how to avoid the disease in the future.

---
