from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/ask", methods=["GET", "POST"])
def ask():
	value = request.args.get("resp")
	return value

if __name__ == '__main__':
	app.run(debug=True)