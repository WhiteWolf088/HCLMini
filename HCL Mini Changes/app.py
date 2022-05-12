from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn
from sklearn.tree import DecisionTreeRegressor
import itertools



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
        Type=int(request.form['Type'])
        HouseType=int(request.form['HouseType'])
        Furniture=int(request.form['Furniture'])

        input=[Bedroom, Area, Bathroom, Type, HouseType, Furniture]
        input_2 = [Bedroom, Area, Bathroom, Type]
        input_HT=[Bedroom, Area, Bathroom, Type, HouseType]
        Type=[]
        if input_2[3]==0:
            input_2.pop()
            input_2.append(1)
            input_2.append(0)
        elif input_2[3]==1:
            input_2.pop()
            input_2.append(0)
            input_2.append(1)
        input_3=input_2+Type
        if input_HT[4]==0:
            input_3.append(1)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
        elif input_HT[4]==1:
            input_3.append(0)
            input_3.append(1)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
        elif input_HT[4]==2:
            input_3.append(0)
            input_3.append(0)
            input_3.append(1)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
        elif input_HT[4]==3:
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(1)
            input_3.append(0)
            input_3.append(0)
        elif input_HT[4]==4:
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(1)
            input_3.append(0)
        elif input_HT[4]==5:
            input_3.append(0)
            input_3.append(1)
            input_3.append(0)
            input_3.append(0)
            input_3.append(0)
            input_3.append(1)
        if input[5] == 0:
            input_3.append(1)
            input_3.append(0)
            input_3.append(0)

        elif input[5] == 1:
            input_3.append(0)
            input_3.append(1)
            input_3.append(0)
        elif input[5] == 2:
            input_3.append(0)
            input_3.append(0)
            input_3.append(1)

        last_input = tuple(input_3)
        input_numpy=np.asarray(last_input)
        input_reshape=input_numpy.reshape(1,-1)
        prediction = model.predict(input_reshape)

        return render_template('predict.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
