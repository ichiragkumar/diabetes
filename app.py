from flask import Flask
import pickle
import sklearn
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        FS = int(request.form["FS"])
        FU = int(request.form["FU"]) 
        ## load model here
        with open("my_model", "rb") as f:
            model = pickle.load(f)
            
            
        result = model.predict([[FS, FU]])    
        if result[0] == "YES":
            return render_template("home.html", data=["Sorry You might Have Diabeted Consult To Doctor", "red"])
        else:
            return render_template("home.html", data=["Congratulations you Dont Have Diabetes", "green"])
    else:        
        return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/profile/<string:name>")## to make an variable here inside app.route()
#3 to recieve url parameter reciveve karne ke lie
def profile_name(name):
    return "hii url " + str(name)


@app.route("/profile/<int:id>")## to make an variable here inside app.route()
#3 to recieve url parameter reciveve karne ke lie
def profile_id(id):
    return "your are requested with user " + str(id)


# @app.route("/predict",methods=["POST"])
# def submitt_post():
#     if request.method == "POST":
#         FS = int(request.form["FS"])
#         FU = int(request.form["FU"])
        
        
        
#         ## load model here
#         with open("my_model", "rb") as f:
#             model = pickle.load(f)
            
            
#         print(FS, FU)
#         result = model.predict([[FS, FU]])    
#         if result[0] == "YES":
#             return "sorry You Might Have Diabetes"
#         else:
#             return "Congratulations You dont haveDiabetes"
#     else:
#         return "something went wrong"
    


if __name__ == "__main__":
    app.run(debug=True)## port 6000 you can change