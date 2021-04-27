from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask!!!"

@app.route("/portfolio")
def portfolio():
    return "Portfolio!!!"

@app.route("/contact")
def contact():
    return "Send e-mail to me"

@app.route("/blog")
def blog():
    return "blog"

if __name__ == "__main__":
    app.run(debug=True)

