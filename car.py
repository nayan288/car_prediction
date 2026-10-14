import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

car_data = pd.read_csv("used_car_clean.csv")

# f = car_data[["Brand","Model","Location","Fuel_Type","Transmission","Owner_Type","Year","Car_Age","Kilometers_Driven","Mileage","Engine","Power","Seats","Price","Has_New_Price"]]
f = car_data.drop('Price_Class', axis=1)
t = car_data["Price_Class"]

Xtrain, Xtest, Ytrain, Ytest = train_test_split(f,t,train_size=0.8,random_state=54) 

model = RandomForestClassifier()

model.fit(Xtrain,Ytrain)
joblib.dump(model,"model.joblib", compress=3)

data = np.array([[9,2010,72000,0,0,1,26.6,998.0,58.16,5.0,1.75,17,616,16,0]])

print(model.predict(data))
    