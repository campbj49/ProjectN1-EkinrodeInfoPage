"""Flask app for Ekinrode Page"""

from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenz"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

@app.route("/")
def start():
    """Render landing page"""  
    return render_template("start.html",
        title = "Ekinrode",
        header = "Dr. Ekinrode's Office")
    
