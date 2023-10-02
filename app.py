from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Sample data (for demonstration purposes)
data = {"name": ""}


@app.route("/")
def index():
    return render_template("index.html", data=data)


@app.route("/get_data", methods=["GET"])
def get_data():
    return data["name"]


@app.route("/post_data", methods=["POST"])
def post_data():
    name = request.form.get("name")
    data["name"] = name
    return name


if __name__ == "__main__":
    app.run(debug=True)
