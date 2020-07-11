import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template
model = joblib.load('marriage_age_predictor.pkl')
print(model.predict([[1,2,5,6,5,175]]))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        myDict = request.form
        gender = int(myDict['gender'])
        religion = int(myDict['religion'])
        caste = int(myDict['caste'])
        mother_tongue = int(myDict['mother_tongue'])
        country = int(myDict['country'])
        Height_CM = int(myDict['Height_CM'])
        predict = model.predict([[gender, religion, caste, mother_tongue, country, Height_CM]])
        final = int(round(predict[0]))
        return render_template('index.html', ans = " Your predicted age of Marriage is {}".format(final))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
        