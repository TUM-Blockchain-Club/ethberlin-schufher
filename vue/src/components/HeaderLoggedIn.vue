<template>
    <div class="app-bar">
        <router-link to="/" class="title">
            <img src="@/assets/logo-text.svg" alt="schufher logo" />
        </router-link>
        <div class="menu-items">
            <a href="#" class="menu-link">PRODUCTS</a>
            <a href="#" class="menu-link">CONTACT</a>
        </div>
        <div class="buttons-right" style="display: flex; align-items: center;">
            <span style="margin-right: 10px; color: white;">Mr. Alexander Semenov</span>
            <v-icon large class="avatar-icon custom-avatar-icon">mdi-account-circle</v-icon>
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

.avatar-icon {
  color: #76ABAE;
  font-size: 44px;
}

.custom-avatar-icon path:first-child {
  fill: white;
}
</style>
