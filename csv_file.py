import pandas as pd#importing csv file


#reading csv file in pandas module
df = pd.read_csv("diabetes.csv")




#displaying data of csv file
print(df.head())

y = df["Dibetes"]
print(y)



#converting text to numeric data
from sklearn.preprocessing import LabelEncoder
le_FU = LabelEncoder()



#creating empty data frame
x = pd.DataFrame(columns = ["FS", "FU"])
print(x)

##now will add the Data
x["FS"] = df["Fasting sugar"]
x["FU"] = le_FU.fit_transform(df["Frequent Unination"])


print("now data will numeric",x)


##use random algorithium using randimforest 

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(x,y)## we have created succesfully our model

#check for user diabetes h ki nhi h
print(classifier.predict([[115,0]]))


#### here  i am  importing pickle module to use others file
import pickle
with open("my_model", "wb") as f :   ## its opening file if not exist then it 
        pickle.dump(classifier,f)



##open model_file
with open("my_model", "rb") as f :
    model = pickle.load(f)

    print(model.predict([[150,1]]))
