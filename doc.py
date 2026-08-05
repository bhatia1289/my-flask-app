from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('docform.html')

@app.route('/upload', methods = ['POST'])
def get_data():
    file = request.files['file']
    print("this is what it contains :", request.files)
    print("file :", file)

    if file.filename.endswith('.csv'):
        path = "userfile/" + file.filename
        file.save(path)
        return "we have recieved your file"
    else:
        return "upload a csv file only."


if __name__ == "__main__":
    app.run(debug=True)
