from flask import Flask
from flask import render_template
from networkCheck import *
import random, subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    update()

    try:
        sp = subprocess.check_output('iwgetid')
        wifiName = sp.split('"')[1]
    except:
        wifiName = "Not Connected"

    return render_template(
    "index.html",
    data=chartData,
    color1=random.choice(["#E24E42","#E9B000","#EB6E80","#008F95"]),
    color2="#000",
    color3="white",
    networkName=wifiName
    ) # Render the site with the current data

if __name__ == '__main__':
    app.secret_key="Secret key"
    app.run(debug = True)
