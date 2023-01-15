from flask import Flask, request, jsonify
import pickle
import pandas as pd

# init
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Test 123</h1>"

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    return model

burnout_model = open_model("burnout_pipe.pkl")

def burnout_inference(data, model=burnout_model):
    """
    input : list with length 5 --> ['Gender', 'WFH', 'Designation', 
                                    'Resource Allocation', 'Mental Fatigue Score']
    output : predicted value : (idx, label)
    """
    columns = ['gender', 'wfh', 'designation', 'resource', 'mental_score']
    data = pd.DataFrame(data, columns=columns)
    res = model.predict(data)
    return res[0]

@app.route("/burnout")
def burnout_predict():
    args = request.args
    gender = args.get("gender", type=object, default='Male')
    wfh = args.get("wfh", type=object, default='No')
    designation = args.get("designation", type=int, default=0)
    resource = args.get("resource", type=int, default=1)
    mental_score = args.get("mental_score", type=float, default=0)
    new_data = [gender, wfh, designation,
                resource, mental_score]
    value = burnout_inference(new_data)
    response = jsonify(result=(round(float(value),2)))
    return response    

# @app.route("/burnout", methods=['POST'])
# def burnout_predict():
#    args = request.json
#    gender = args.get("gender")
#    wfh = args.get("wfh")
#    designation = args.get("designation")
#    resource = args.get("resource")
#    mental_score = args.get("mental_score")
#    new_data = [gender, wfh, designation,
#                resource, mental_score]
#    value = burnout_inference(new_data)
#    response = jsonify(value)
#    return response


# app.run(debug=True)