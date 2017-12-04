from flask import Flask, render_template

# Create an instance of Flask and save it to the "app" variable.
app = Flask(__name__)

# Map the URL of / (the root) to the function "index()"
@app.route("/")
def index():
	#When index() is run, render the template file at index.html
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

# app.run runs it on a local server. This tells it to show debugging messages.
if __name__ == "__main__":
	app.run(debug=True)
