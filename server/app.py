from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello():
    return "Hello there!"

@app.route("/api/get_location_names", methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input format"}), 400
        
        total_sqft = float(data.get('total_sqft', 0))
        location = data.get('location', "")
        bhk = int(data.get('bhk', 0))
        bath = int(data.get('bath', 0))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({'estimated_price': estimated_price})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting server")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=8080)