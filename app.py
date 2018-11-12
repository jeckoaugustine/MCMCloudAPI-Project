from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/calculate", methods=['GET'])
def calculator():
    firstValue=request.args.get('firstValue', type=int)
    secondValue=request.args.get('secondValue', type=int)
    opr=request.args.get('operation', type=str)
    if (opr=='add'):
        answer=firstValue+secondValue
    elif (opr=='sub'):
        answer=firstValue-secondValue
    elif (opr=='mul'):
        answer=firstValue*secondValue
    elif (opr=='div'):
        answer=int(firstValue/secondValue)
    else:
        answer="Invalid Operator"
    
    return jsonify({'output':answer}) 

@app.route("/")
def home():
    return("Home Page Successful")