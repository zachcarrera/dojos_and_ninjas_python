from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo



# route to display a from to create a ninja
@app.route("/ninjas")
def new_ninja():

    # query for a list of all dojos so that 
    # we can select from them in the form
    dojos = Dojo.get_all()
    return render_template("new_ninja.html",dojos=dojos)



# form submission to make a new ninja
@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    print("query db and insert new ninja here")
    Ninja.save(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")