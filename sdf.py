import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("used_car_clean.csv").head(10)



f = data.drop('Price_Class', axis=1)
t = data["Price_Class"]

Xtrain, Xtest,Ytrain,Ytest = train_test_split(f,t, train_size=0.8,random_state=0)

print(Xtrain)