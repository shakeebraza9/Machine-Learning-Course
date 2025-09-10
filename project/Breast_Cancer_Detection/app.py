from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

# loading model
model = pickle.load(open('model.pkl', 'rb'))

# flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    features = request.form['feature']

    # Saare newline aur extra space ko ek space me badlo
    features = features.replace("\n", " ").replace("\r", " ")
    features = features.replace("  ", " ").strip()

    # Space aur comma dono handle karo
    if "," in features:
        features = features.split(",")
    else:
        features = features.split(" ")

    # Har value ko float me badlo aur empty string hatao
    features = [f for f in features if f.strip() != ""]
    np_features = np.asarray(features, dtype=np.float32)

    # Prediction
    pred = model.predict(np_features.reshape(1, -1))
    message = ['Cancrouse' if pred[0] == 1 else 'Not Cancrouse']
    return render_template('index.html', message=message)



if __name__ == '__main__':
    app.run(debug=True)