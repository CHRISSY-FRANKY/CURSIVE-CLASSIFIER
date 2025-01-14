print("WELCOME TO CURSIVE CLASSIFIER!")
print("I AM GOING TO SLEEP, I OPEN TOMORROW")
print("DANG, FLASK NOW HAS HOT RELOAD!")
from flask import Flask

app = Flask(__name__) # our flask app is created

@app.route('/')
def index():
    return """
    <h1>WELCOME TO CURSIVE CLASSIFIER!</h1>
    <br>
    <h2>Designed by Chrissy Franky</h2>
    <h3>Powered by CONDA</h3>
    <h3>Powered by PyTorch</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)