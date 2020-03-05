from flask import Flask
from random import *

app = Flask(__name__)

@app.route("/")
def main():
     x = randint(1,1000000)
    txt = "Random Number: {}"
    return txt.format(x)
    
if __name__ == "__main__":
    app.run(debug=True)
