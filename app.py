from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and feature names
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        try:
            # Get feature inputs from form
            input_data = [float(request.form[feature]) for feature in feature_names]
            input_array = np.array(input_data).reshape(1, -1)
            prediction = int(model.predict(input_array)[0])

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", feature_names=feature_names, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
