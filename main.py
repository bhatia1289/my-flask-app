##import flask
from flask import Flask, jsonify, render_template

#create flask instance
app = Flask(__name__)

#define function and route
# @app.route('/')
# def home():
#     return "Welcome to my website"

@app.route('/about')
def about():
    data = "my name is abhishek bhatia"
    return data

@app.route('/data')
def data():
    user_data = {"name": "Abhishek",
                 "Age" : 21}
    return jsonify(user_data)

# @app.route('/')
# def home_page():
#     name = "Abhishek"
#     return render_template('index.html', name = name)

@app.route('/', methods =['GET'])
def home():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    return "we have recieved your information"


#trigger the flask app
if __name__ == "__main__":
    app.run(debug= True)