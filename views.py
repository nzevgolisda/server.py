
from flask import Blueprint, render_template
views = Blueprint(__name__, "views")
@views.route("/")
def home():
    ## Here arter the self = index.html object
    ## we can set parameters like name = "name", 
    ## age = "age" etc, and render them in the html
    return render_template("index.html", name="Nikos", age="29") 

#def home2():
#    return "home page"