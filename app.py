import os
import pickle
import pandas as pd

from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

current_path = os.path.dirname(os.path.realpath(__file__))
pickle_in = open(f"{current_path}/model.pkl", "rb")
rf = pickle.load(pickle_in)


@app.route("/")
def index() -> str:
    """
    Home
    """
    return "Welcome All!!"


@app.route("/predict", methods=["GET"])
def predict_note():
    """Let's Authenticate the Banks Note
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values
    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = rf.predict([[variance, skewness, curtosis, entropy]])
    return "This is my prediction" + str(prediction)


@app.route("/predict_file", methods=["POST"])
def predict_file():
    """Predict File Output
    ---
    parameters:
      - name: test
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values
    """
    df_test = pd.read_csv(request.files.get("test"))
    file_prediction = rf.predict(df_test)
    return "Predcted values of test file is" + str(list(file_prediction))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
