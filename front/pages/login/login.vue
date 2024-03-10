<template>  
  <div class="login-container">  
    <h2>登录</h2>  
    <form @submit.prevent="submitForm">  
      <div>  
        <label for="username">用户名:</label>  
        <input type="text" id="username" v-model="username" required>  
      </div>  
      <div>  
        <label for="password">密码:</label>  
        <input type="password" id="password" v-model="password" required>  
      </div>  
      <button type="submit">登录</button>  
    </form>  
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>  
  </div>  
</template>  
  
<script>  
import { ref } from 'vue';  
  
export default {  
	data() {  
		return {  
		  // 确保在这里定义了 username 属性  
		  username: '',  
		  password: '',
		  errorMessage: ''
		  // 其他数据属性...  
		};  
	},  
  setup() {  
    const username = ref('');  
    const password = ref('');  
    const errorMessage = ref('');  
    const submitForm = async () => {  
      // 假设这是向后端发送请求的函数  
      // 在实际开发中，你应该使用 axios 或 fetch 等库来发送请求  
      const isValidUser = await validateUser(username.value, password.value);  
      if (isValidUser) {  
        // 登录成功，你可以跳转到其他页面或进行其他操作  
        alert('登录成功！');  
        // 清除输入字段和错误信息  
        username.value = '';  
        password.value = '';  
        errorMessage.value = '';  
      } else {  
        // 登录失败，显示错误信息  
        errorMessage.value = '用户名或密码错误';  
      }  
    };  
  
    // 假设的验证用户函数  
    const validateUser = async (usernameInput, passwordInput) => {  
      // 在这里，我们只是简单地比较用户名和密码  
      // 在实际开发中，你应该发送请求到后端进行验证  
      return usernameInput === 'admin' && passwordInput === 'password';  
    };  
  
    // 返回响应式的数据和方法  
    return {  
      username,  
      password,  
      errorMessage,  
      submitForm  
    };  
  }  
};  
</script>  
  
<style scoped>  
.login-container {  
  display: flex;  
  flex-direction: column;  
  align-items: center;  
  justify-content: center;  
  height: 100vh;  
  padding: 20px;  
}  
  
.error-message {  
  color: red;  
  margin-top: 10px;  
}  
</style>