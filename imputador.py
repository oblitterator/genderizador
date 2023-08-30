from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo y el vectorizador
clf = joblib.load("modelo_nombre_sexo.pkl")
vectorizer = joblib.load("vectorizador_nombre_sexo.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    # Asegurarse de que se envíe el nombre en el cuerpo de la solicitud
    data = request.get_json(force=True)
    nombre = data.get("nombre", None)
    if not nombre:
        return jsonify({"error": "El nombre es requerido"}), 400
    
    # Vectorizar el nombre y predecir el sexo
    nombre_vectorizado = vectorizer.transform([nombre])
    prediction = clf.predict(nombre_vectorizado)[0]
    sexo = 'M' if prediction == 0 else 'F'
    
    return jsonify({"nombre": nombre, "sexo": sexo})

if __name__ == "__main__":
    app.run(debug=True)
