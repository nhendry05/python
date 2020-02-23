from flask import Flask
from flask import render_template, redirect, send_from_directory, request, url_for
import os
from uuid import uuid4

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods = ["POST"])
def upload_photo():
    target = os.path.join(APP_ROOT, 'images')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for photo in request.files.getlist("cover_photo"):
        print(photo)
        filename = photo.filename
        destination = "/".join([target, filename])
        print(destination)
        photo.save(destination)

    return render_template("output.html", image_name=filename)

@app.route("/upload/<filename>")
def send_cover(filename):
    return send_from_directory("images", filename)
if __name__ == "__main__":
    app.run(debug=True)
