from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import random
from flask_bootstrap import Bootstrap
import os
from extract_color import extract_color
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./uploads"
# Restrict file extention
ALLOWED_EXTENTIONS = set(["png", "jpg", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
bootstrap = Bootstrap(app)  # tie app to bootstrap


def allowed_file(filename):
    # check if there is . in file name
    # 1 if OK, 0 if NG
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENTIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        # extract data
        file = request.files['file']

        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        # to create modified image
        modified_img = extract_color(input_image=file.filename, resize=300, tolerance=30, zoom=6)
        print(modified_img)

        return render_template('index.html', filename=file.filename, modified_img=modified_img)
    elif request.method == 'GET':
        return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

# TODO continue upgrading extract_clor.py
