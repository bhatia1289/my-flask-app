from flask import Flask, request, jsonify
import pandas as pd
import pickle
app = Flask(__name__)

#define endpoint
@app.route('/predict', methods =['POST'])
def get_prediction():
    baby_data = request.get_json()
    
    #convert into dataframe
    baby_df = pd.DataFrame(baby_data)
    
    #load machine learning model
    with open('model/model.pkl','rb') as obj:
        model = pickle.load(obj)
        
    #make predictions
    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]),2)
    
    #return response in json format
    response = {"prediction": prediction}
    return jsonify(response)
    
if __name__ == '__main__':
    app.run(debug=True)