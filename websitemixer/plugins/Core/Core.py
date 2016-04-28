from flask import render_template
from websitemixer import app

@app.route('/')
def home():
    return render_template("Core/index.html")
