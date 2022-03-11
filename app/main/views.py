from flask import render_template
from . import main

@app.route('/')
def index():
    return '<h1>Welcom to zac-master blog</h1>'