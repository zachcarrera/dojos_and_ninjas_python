from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojos_model import Dojo


# route to the dojos page
@app.route("/dojos")
def dojos():
    print("dojo query")
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)


# form submission to make a new dojo
@app.route("/new_dojo", methods=["POST"])
def new_dojo():
    print(request.form)
    print("adding dojo")
    Dojo.save(request.form)
    return redirect("/dojos")


# route to display a dojo and the ninjas associated with it
@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    print("show individual dojo", dojo_id)
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template("show_dojo.html", dojo=dojo)

