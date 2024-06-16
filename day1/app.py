from flask import Flask
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to the home pg</h1>"

@app.route("/welcome/<names>")
def welcome(names):
    return f"HI {names}, how are u?"
@app.route("/add/<int:num>")
def add(num):
    return f"INput is {num} , output is {num+27}"

@app.route("/add_two/<int:num1>/<int:num2>")
def add_two(num1,num2):
    return f" output is {num1+num2}"
       
@app.route("/about")
def about():
    return "Welcome to about pg"
if __name__ =="__main__":
    app.run(debug=True)