<template>
    <div class="app-bar">
      <router-link to="/" class="title">
        <img src="@/assets/logo-text.svg" alt="schufher logo" />
      </router-link>
      <div class="menu-items">
        <a href="#" class="menu-link">PRODUCTS</a>
        <a href="#" class="menu-link">CONTACT</a>
      </div>
      <div class="buttons-right">
        <router-link to="/login">
          <v-btn class="normal-button" style="border-radius: 50px;">Sign In</v-btn>
        </router-link>
        <v-btn class="emphasize-button" style="border-radius: 50px;">Sign Up</v-btn>
      </div>
    </div>
</template>

<script>
</script>

<style scoped>
.app-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4vh;
  background-color: #31363F;
  height: 60px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
  margin-left: 2em;
  gap: 20px;
  text-align: left;
  flex-grow: 1;
}

.menu-link {
  color: white;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  padding: 0 1em;
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
</style>
