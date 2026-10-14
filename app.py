from flask import Flask,request,render_template
import joblib

model = joblib.load('model.joblib')

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def car():
    if request.method == "POST":
        
        Location = request.form.get("Location")
        Year = request.form.get("Year")
        Kilometers_Driven = request.form.get("Kilometers_Driven")
        Fuel_Type = request.form.get("Fuel_Type")
        Transmission = request.form.get("Transmission")
        Owner_Type = request.form.get("Owner_Type")
        Mileage = request.form.get("Mileage")
        Engine = request.form.get("Engine")
        Power = request.form.get("Power")
        Seats = request.form.get("Seats")
        Price = request.form.get("Price")
        Brand = request.form.get("Brand")
        Model = request.form.get("Model")
        Car_Age = request.form.get("Car_Age")
        Has_New_Price = request.form.get("Has_New_Price")
        data = [[Location,Year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats,Price,Brand,Model,Car_Age,Has_New_Price]]
        Price_Class = model.predict(data)
        pred = Price_Class[0]
        price = {
                   0: "0.44 - 3.50 Lakh",
                   1: "3.50 - 5.64 Lakh",
                   2: "5.64 - 9.95 Lakh",
                   3: "9.95 - 160.00 Lakh"
                }
        name = ["Budget","Mid","Premium","Luxury"]
        return render_template("index.html" , result = f"your car has value of {price[pred]} and type: {name[pred]}")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")








