from flask import Flask, request, jsonify  
import json  
from flask_cors import CORS
app = Flask(__name__)  
# 初始化 CORS，并设置允许所有源进行访问
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/register', methods=['POST'])  
def register():
    data = {
		"a":1213,
		"b":3346,
		"c":4566
    }
    return jsonify(data)
  
if __name__ == '__main__':  
    app.run(debug=True)