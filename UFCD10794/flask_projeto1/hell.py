from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world_bs():
    return "<p>Hello, World!</p>"

@app.route('/<nome>')
def hello_world(nome: str):
    return f"<h3><b><i>Hello, World! {nome}</i></b></h3>"

@app.route('/teste')
def RunIndex():
    return render_template('index.html')