from flask import Flask, render_template, request
import os
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
UPLOADS = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOADS


@app.route("/home")
@cross_origin()
def run():
    return render_template("home.html")

@app.route("/")
@cross_origin()
def run1():
    return render_template("home.html")


@app.route("/home/receive", methods=['GET', 'POST'])
@cross_origin()
def receive():
    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            return render_template("errors/error.html")
        file = request.files['file']
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        filecontent = ''
        with open(filepath, 'r') as f:
            for line in f:
                filecontent += line
                filecontent += '\n'
            filecontent += "\n\n"
            filecontent += "\n\nCongrats content got updated!!"
        f.close()
        return filecontent
    return "fail"


if __name__ == "__main__":
    app.run()
