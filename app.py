from flask import Flask
from flask import render_template
from networkCheck import *
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    update()
    return render_template("index.html", data=chartData, color1=random.choice(["#E24E42","#E9B000","#EB6E80","#008F95"]), color2="#000", color3="white", networkName="Resnet") # Render the site with the current data

if __name__ == '__main__':
    app.secret_key="Secret key"
    app.run(debug = True)
