from flask import Flask, redirect,url_for
import time
app=Flask(__name__)

@app.route("/")
def home():
    return f"home"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"Congo u{sname.title()} have passed{marks}"
@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"Sorry ut{sname.title()} have failed{marks} "
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed",sname=name,marks=num))
        
    else:
        time.sleep(1)
        return redirect(url_for("passed",sname=name,marks=num))
if __name__ =="__main__":
    app.run(debug=True)