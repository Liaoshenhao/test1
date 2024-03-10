<template>  
  <div class="login-container">  
    <h2>登陆</h2>  
    <form @submit.prevent="handleSubmit">  
      <div>  
        <label for="username">用户名:</label>  
        <input type="text" id="username" v-model="username" required>  
      </div>  
      <div>  
        <label for="password">密码:</label>  
        <input type="password" id="password" v-model="password" required>  
      </div>  
      <button type="submit">登陆</button>  
    </form>  
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>  
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
    handleSubmit() {  
      // 这里你可以添加实际的登陆逻辑，比如向后端发送请求验证用户名和密码  
      // 这里只是一个简单的示例，直接比较用户名和密码是否匹配  
      if (this.username === 'admin' && this.password === 'password') {  
        // 登陆成功，你可以跳转到其他页面或进行其他操作  
        alert('登陆成功！');  
      } else {  
        // 登陆失败，显示错误信息  
        this.errorMessage = '用户名或密码错误';  
      }  
    }  
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