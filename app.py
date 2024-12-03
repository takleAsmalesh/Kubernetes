from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name", "World")
        return f"<h1>Hello, {name}!</h1>"
    return '''
        <form method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <button type="submit">Greet Me!</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
