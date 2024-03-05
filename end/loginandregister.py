# 后端使用flask框架来进行路由管理以及处理请求
# request用于获取客户端发送的 HTTP 请求信息
# jsonify 用于将 Python 对象转换成 JSON 格式
from flask import Flask, request, jsonify  
import json  
from flask_cors import CORS

def init_login_register_flask():
	app = Flask(__name__)  
	# 初始化 CORS，并设置允许所有源进行访问
	CORS(app, resources={r"/*": {"origins": "*"}})
	@app.route('/login', methods=['POST'])  
	def login():
		# 获取前端POST来的json数据
		data = request.get_json()
		username = data.get('username')  
		password = data.get('password')
		ret = 0
		# 查询账号密码，返回登陆信息是否校验通过
		if 'admin' == username and '123456' == password :
			ret = 1
		else :
			ret = 0
		return ret
	@app.route('/register', methods=['POST']) 
	def register():
		# 获取前端POST来的json数据
		data = request.get_json()
		username = data.get('username')  
		password = data.get('password')
		registerId = data.get('regitsterId')
		res = {
			"ret" : "注册失败"
		}
		# 写入数据库
		if '2333' == registerId :
			res.ret = "注册成功"
			
		return jsonify(res)
	return app