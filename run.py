from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask!!!"

@app.route("/portfolio")
def portfolio():
    return "Portfolio!!!"

@app.route("/contact")
def portfolio():
    return "Send e-mail to me"

if __name__ == "__main__":
    app.run(debug=True)

