from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def indexhahaha():
	return "<h1>HAlo selamat sore</h1>!"


if __name__ == '__main__':
	app.run(debug=True)