<template>
  <v-container class="fill-height">
    <v-card class="login-form" elevation="10">
      <v-card-title class="justify-center">
        <v-icon large class="avatar-icon custom-avatar-icon">mdi-account-circle</v-icon>
        <span class="login-title">LOGIN</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="submitForm">
          <div class="field-label">E-MAIL</div>
          <v-text-field v-model="email" variant="solo"></v-text-field>
          <div class="field-label">PASSWORD</div>
          <v-text-field v-model="password" type="password" variant="solo"></v-text-field>
          <router-link to="/user">
            <v-btn type="submit" color="#76ABAE" block large class="rounded-btn black-text-btn">Login</v-btn>
          </router-link>
        </v-form>
      </v-card-text>
      <div class="horizontal-line"></div>
      <v-card-actions class="justify-center action-buttons">
        <v-btn text class="helper-buttons white-text uppercase-text">Forgot Password?</v-btn>
        <v-btn text class="helper-buttons white-text uppercase-text">Do not have an account?</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    submitForm() {
      // Handle form submission
      console.log('Email:', this.email);
      console.log('Password:', this.password);
    }
  }
};
</script>

<style scoped>
.fill-height {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  padding: 0;
}

.login-form {
  width: 600px;
  padding: 20px;
  background-color: #222831;
  color: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.login-title {
  font-size: 20px;
  margin-left: 20px;
  margin-top: 30px;
  color: white;
}

.field-label {
  font-size: 14px;
  color: white;
  margin-bottom: 5px;
}

.v-card-text {
  margin-top: 20px;
}

.avatar-icon {
  color: #76ABAE;
  font-size: 44px;
}

.custom-avatar-icon path:first-child {
  fill: white;
}

.horizontal-line {
  border-top: 2px solid #76ABAE;
  margin: 10px 60px;
}

.helper-buttons {
  font-size: 12px;
  text-transform: none;
  text-decoration: none;
  margin: 0;
}

.forgot-password:hover,
.create-account:hover {
  color: #B5B5B5;
}

.rounded-btn {
  border-radius: 50px;
}

.black-text-btn {
  color: black !important;
}

.action-buttons {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.action-buttons .v-btn {
  margin-bottom: 0;
}

.action-buttons .v-btn:last-child {
  margin-bottom: 0;
}

.white-text {
  color: white !important;
}

.uppercase-text {
  text-transform: uppercase;
}
</style>
