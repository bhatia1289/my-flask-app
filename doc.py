from flask import Flask, render_template, request,jsonify
import pandas as pd

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
        # return "we have recieved your file"

        ##read file
        df = pd.read_csv("userfile/employee_attrition_test.csv")
        print(df.head())

        #basic stats :min , max, count, average of age
        min_age = float(df['Age'].min())
        max_age = float(df['Age'].max())
        total_employees = float(df['Age'].count())
        avg_Age = float(df['Age'].mean())

        response = {"Min Age": min_age,
                    "Max Age": max_age,
                    "Total Employees": total_employees,
                    "Average Age": avg_Age}
        return jsonify(response)
    else:
        return "upload a csv file only."


if __name__ == "__main__":
    app.run(debug=True)
