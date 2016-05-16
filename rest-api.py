from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return "Congratulations! You connected to the server."

@app.route('/createOrder', methods=['POST'])
def createOrder():

        if not request.json or not 'partNumber' in request.json:
                success = 0
                message = 'Invalid request'

        else:
                success = 1
                message = 'Part Number ' + request.json['partNumber'] + ' successfully ordered.'
        
        returnObject = {
                'success': success,
                'message': message
        }

        return jsonify({'returnObject': returnObject})

if __name__ == '__main__':
	app.run(host='0.0.0.0')
