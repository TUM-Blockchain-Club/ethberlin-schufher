<template>
    <div class="modal" v-if="showPopOut">
        <div class="modal-content">
            <span class="close-button" @click="close" aria-label="Close">
                <i class="mdi mdi-close-circle" aria-hidden="true"></i>
            </span>
            <p class="popout-text"><b>User specific access</b>: Password Required</p>
            <div class="password-container">
                <input class="password-input" v-model="password" :type="passwordFieldType" placeholder="Enter your password"
                    @keyup.enter="submit" />
                <span class="toggle-password" @click="togglePasswordVisibility">
                    <i v-if="passwordFieldType === 'password'" class="mdi mdi-eye" aria-hidden="true"></i>
                    <i v-else class="mdi mdi-eye-off" aria-hidden="true"></i>
                </span>
            </div>
            <button class="submit-button" @click="submit">Submit</button>
            <p class="success-message" v-if="successMessage">{{ successMessage }}</p>
            <p class="error-message" v-if="errorMessage">{{ errorMessage }}</p>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    data() {
        return {
            showPopOut: true,
            password: '',
            successMessage: '',
            errorMessage: '',
            passwordFieldType: 'password'
        }
    },
    methods: {
        close() {
            this.$store.commit('hidePasswordPopOut')
        },
        async submit() {
            try {
                const response = await axios.post('http://localhost:8042/api/v1/auth', {
                    password: this.password
                });

                if (response.data.access_token) {
                    localStorage.setItem('access_token', response.data.access_token);
                    this.successMessage = 'Authentication successful';
                    this.errorMessage = '';
                    setTimeout(() => {
                        this.$emit('authenticated')
                        this.showPopOut = false
                        if (this.$store.state.intendedRoute) {
                            this.$router.push(this.$store.state.intendedRoute.path);
                            this.$store.state.intendedRoute = null;
                        } else {
                            this.$router.push({ name: 'Home' });
                        }
                        this.successMessage = '';
                    }, 1000); // delay 1 sec
                } else {
                    this.errorMessage = 'Authentication failed';
                }
            } catch (error) {
                console.error(error)
                this.errorMessage = 'Error during authentication';
            }
        },
        togglePasswordVisibility() {
            this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password';
        },
    }
}
</script>
  
<style>
.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 9999;
}

.modal-content {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.2), 0 2px 10px 0 rgba(0, 0, 0, 0.19);
    width: 50%;
    max-width: 400px;
}

.close-button {
    font-size: 32px;
    color: red;
    position: absolute;
    top: -15px;
    right: -5px;
    cursor: pointer;
}

.password-input {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: 100%;
}

.submit-button {
    padding: 10px 20px;
    background-color: var(--color-orange);
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

p.popout-text {
    margin-bottom: 10px;
    font-size: 16px;
    font-weight: 400;
}

p.success-message {
    color: green;
}

p.error-message {
    color: red;
}

.password-container {
    position: relative;
    width: 100%;
}

.toggle-password {
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
}

.password-input {
    padding-right: 40px;
}
</style>
  