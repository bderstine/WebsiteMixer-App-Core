from flask import Flask, Response, session, request, url_for, redirect, render_template, abort, g, send_from_directory
from websitemixer import app

@app.route('/')
def home():
    return render_template("Base/index.html")
