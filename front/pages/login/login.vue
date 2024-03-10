<template>  
  <div id="login-container" class="container">  
    <div class="login-form">  
      <h2 class="login-title">Welcome Back!</h2>  
      <form >  
        <div class="form-group">  
          <label for="username" class="sr-only">Username</label>  
          <input  
            type="text"  
            id="username"  
            v-model="username"  
            class="form-control"  
            placeholder="Username"  
            required  
            auto-focus  
          >  
        </div>  
        <div class="form-group">  
          <label for="password" class="sr-only">Password</label>  
          <input  
            type="password"  
            id="password"  
            v-model="password"  
            class="form-control"  
            placeholder="Password"  
            required  
          >  
        </div>  
        <button @click ="login" type="submit" class="btn btn-primary btn-block">  
          Login  
        </button>  
      </form>  
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>  
    </div>  
  </div>  
</template>  
  
<script>  
export default {  
  data() {  
    return {  
      username: '',  
      password: '',  
      errorMessage: ''  
    };  
  },  
  methods: {  
    login() {  
      // 这里应该是发送登录请求到服务器的代码  
      // 示例中仅做模拟处理    
      if (this.username === 'admin' && this.password === 'password') {  
        // 登录成功处理，例如跳转到其他页面  
        // this.$router.push('/dashboard'); // 假设你使用了 Vue Router 
		alert("登录成功");
		console.log('登录成功！');  
        this.errorMessage = ''; // 清空错误信息  
      } else {  
        // 登录失败处理  
        this.errorMessage = 'Invalid username or password';  
      }  
    }  
  }  
};  
</script>  
  
<style scoped>  
.container {  
  display: flex;  
  justify-content: center;  
  align-items: center;  
  height: 100vh;  
  background-color: #f5f5f5;  
}  
  
.login-form {  
  width: 350px;  
  padding: 20px;  
  background-color: #ffffff;  
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);  
  border-radius: 4px;  
}  
  
.login-title {  
  font-size: 24px;  
  text-align: center;  
  margin-bottom: 20px;  
}  
  
.form-group {  
  margin-bottom: 15px;  
}  
  
.form-control {  
  display: block;  
  width: 100%;  
  padding: 10px;  
  font-size: 16px;  
  line-height: 1.5;  
  color: #495057;  
  background-color: #fff;  
  background-clip: padding-box;  
  border: 1px solid #ced4da;  
  border-radius: 4px;  
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;  
}  
  
.form-control:focus {  
  border-color: #80bdff;  
  outline: 0;  
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);  
}  
  
.btn {  
  display: inline-block;  
  font-weight: 400;  
  color: #fff;  
  text-align: center;  
  vertical-align: middle;  
  user-select: none;  
  background-color: #007bff;  
  border: 1px solid transparent;  
  padding: 0.375rem 0.75rem;  
  font-size: 1rem;  
  line-height: 1.5;  
  border-radius: 0.25rem;  
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;  
}  
  
.btn:hover {  
  cursor: pointer;  
  background-color: #0056b3;  
}  
  
.btn-block {  
  display: block;  
  width: 100%;  
}  
  
.error-message {  
  color: #dc3545;  
  font-size: 14px;  
  text-align: center;  
  margin-top: 10px;  
}  
  
/* 隐藏辅助性文本标签 */  
.sr-only {  
  position: absolute;  
  width: 1px;  
  height: 1px;  
  padding: 0;  
  margin: -1px;  
  overflow: hidden;  
  clip: rect(0, 0, 0, 0);  
  white-space: nowrap;  
  border: 0;  
}  
</style>