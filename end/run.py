from loginandregister import init_login_register_flask

init_login_register_app = init_login_register_flask()  
  
if __name__ == '__main__':  
    init_login_register_app.run(debug=True)