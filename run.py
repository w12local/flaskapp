from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask!!!"

@app.route("/portfolio")
def portfolio():
    return "Portfolio!!!"

if __name__ == "__main__":
    app.run(debug=True)

