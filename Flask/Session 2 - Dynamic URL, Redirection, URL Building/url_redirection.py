import time 
from flask import Flask , redirect, url_for
app=Flask("__name__")


@app.route("/")
def home():
    return "<h1>Welcome to the home page!</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        return redirect(url_for("passed"))
        

@app.route("/pass")
def passed():
    return "<h1> congrats, you have passed"


@app.route("/fail")
def failed():
    return "<h1>Sorry, you have failed"


if __name__=="__main__":
    app.run(debug=True)