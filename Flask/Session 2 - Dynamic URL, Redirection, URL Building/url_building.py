import time 
from flask import Flask , redirect, url_for
app=Flask("__name__")


@app.route("/")
def home():
    return "<h1>Welcome to the home page!</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        time.sleep(1)
        return redirect(url_for("passed",sname=name,marks=num))
        

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1> congrats, {sname.title} have passed with {marks}"


@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry, {sname.title} you have failed you score only this {marks}"


if __name__=="__main__":
    app.run(debug=True)