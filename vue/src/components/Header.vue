<template>
  <v-app>
    <div class="app-bar">
      <a href="https://example.com/home" class="logo-link">
        <img src="@/assets/logo.svg" alt="Logo" class="logo">
      </a>
      <span class="title">
        <img src="@/assets/logo-text.svg" alt="Your SVG">
      </span>
      <div class="menu-items">
        <a href="#" class="menu-link">PRODUCTS</a>
        <a href="#" class="menu-link">CONTACT</a>
        <a href="#" class="menu-link" @click.prevent="handleApiTestClick">{{ apiTestLinkText }}</a>
      </div>
      <div class="buttons-right">
        <v-btn class="normal-button" style="border-radius: 50px;">Sign In</v-btn>
        <v-btn class="emphasize-button" style="border-radius: 50px;">Sign Up for free</v-btn>
      </div>
    </div>
  </v-app>
</template>




<script>
export default {
  data() {
    return {
      apiTestLinkText: 'API TEST',
      defaultApiTestLinkText: 'API TEST'
    }
  },
  methods: {
    async testApiCall() {
      try {
        // Make the API call
        const response = await fetch('http://localhost:8042/api/v1/')
        const data = await response.json()
        
        // Update the link text
        this.apiTestLinkText = data.response
        
        // Reset the link text after 5 seconds
        setTimeout(() => {
          this.apiTestLinkText = this.defaultApiTestLinkText
        }, 5000)
      } catch (error) {
        console.error(error)
      }
    },
    handleApiTestClick() {
      this.testApiCall()
    }
  }
}


</script>
<style scoped>
.app-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4vh;
  background-color: #31363F;
  height: 60px;
}

.emphasize-button {
  color: black;
  background-color: #76ABAE;
}
.normal-button {
  color: black;
  background-color: white;
}

.buttons-right {
  display: flex;
  gap: 10px;
  align-items: center;
}

.menu-items {
  display: flex;
  margin-left: 8em;
  gap: 20px;
  text-align: left;
  flex-grow: 1;
}

.menu-link {
  color: white;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  padding-left: 2em;
  padding-right: 2em;
}

.menu-link:hover {
  text-decoration: underline;
}

.logo {
  max-width: 40px;
  margin-right: 20px;
}

.title {
  font-size: 20px;
  font-weight: 800;
  text-transform: uppercase;
  color: #F8F9FD;
}

.navbar {
  box-shadow: 0px 2px 10px 0px rgba(0, 0, 0, 0.5);
}

.navbar-nav {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
}

.nav-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: inherit;
}

.nav-link i {
  margin-right: 8px;
}

.navbar-nav li {
  text-align: center;
  padding: 14px 16px;
  font-size: .875rem;
  font-weight: 500;
}

.navbar-nav a {
  color: var(--color-grey);
  text-transform: uppercase;
  font-size: 16px;
  font-weight: 500;
  text-decoration: none;
}

.navbar-nav a:hover {
  color: var(--color-dark-blue);
  text-decoration: underline;
  text-decoration-thickness: 3px;
  text-underline-offset: 10px;
}

.language-select .v-input__control {
  color: white;
}

.language-select .v-select__selections {
  color: white;
}

.language-select .v-select__control {
  min-height: 56px;
}

.v-select.v-input--solo.v-input--solo--flat .v-input__control {
  background-color: transparent;
}
</style>

