from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Create Flask App
app = Flask(__name__)


# Create API routing call
@app.route('/predict_weight', methods=['POST']) # decorator
def predict_weight():
    
    # Get JSON Request
    feat_data = request.json
    # Convert JSON request to Pandas DataFrame
    df = pd.DataFrame(feat_data)
    # Match Column Names
    df = df.reindex(columns=col_names)
    # Get prediction
    prediction = list(model.predict(df))
    # Return JSON version of Prediction
    return jsonify({'your fish weight': str(prediction)})

        

if __name__ == '__main__':

    # LOADS MODEL AND FEATURE COLUMNS
    model = joblib.load("fish_lr_model.pkl") 
    col_names = joblib.load("col_names.pkl") 

    app.run(debug=True)