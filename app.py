from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn
from sklearn.tree import DecisionTreeRegressor



app = Flask(__name__)
model = pickle.load(open('Rent_prediction_model.pkl', 'rb'))


@app.route("/", )
def hello():
    return render_template("index.html")


@app.route("/sub", methods=["POST"])
def submit():
    # Html to py
    if request.method == "POST":
        name = request.form["Username"]

    return render_template("sub.html", n=name)


@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        Bedroom = float(request.form['Bedroom'])
        Area = float(request.form['Area'])
        Bathroom = float(request.form['Bathroom'])
        BHK = int(request.form['BHK'])
        RK = int(request.form['RK'])
        Apartment = int(request.form['Apartment'])
        IndependentFloor = int(request.form['IndependentFloor'])
        IndependentHouse = int(request.form['IndependentHouse'])
        PentHouse = int(request.form['PentHouse'])
        StudioApartment = int(request.form['StudioApartment'])
        Villa = int(request.form['Villa'])
        FullFurniture = int(request.form['FullFurniture'])
        SemiFurniture = int(request.form['SemiFurniture'])
        Unfurnished=int(request.form['Unfurnished'])

        input = [Bedroom, Area, Bathroom, BHK, RK, Apartment, IndependentFloor, IndependentHouse, PentHouse, StudioApartment, Villa, FullFurniture, SemiFurniture, Unfurnished]
        last_input = tuple(input)
        input_numpy=np.asarray(last_input)
        input_reshape=input_numpy.reshape(1,-1)
        prediction = model.predict(input_reshape)

        return render_template('predict.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
