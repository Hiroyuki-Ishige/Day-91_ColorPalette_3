from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import random
from flask_bootstrap import Bootstrap
import os
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

        #extract data
        file = request.files['file']

        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        return redirect(url_for("uploaded_file", filename=file.filename))
    elif request.method == 'GET':
        return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

# TODO show uploaed file on upload.html
