#team sleep dep from break: Helena Williams and William Yin
#SoftDev
#K19: A RESTful Journey Skyward
#2021-04-05

from flask import Flask
from flask import render_template
from flask import request
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    importantStuf = []
    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=eFspEIGe644e4mmcvHJj8TX61jV1UczOrxejCQAx') as response:
        importantStuf = response.read()
    deserialized = json.loads(importantStuf)
    return render_template('main.html', image = deserialized["hdurl"], desc = deserialized["explanation"])


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
