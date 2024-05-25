<template>
  <v-app>
    <v-container fluid class="pa-0">
      <Header />
      <v-container fluid class="image-container pa-0">
        <v-img
          :src="imageSrc"
          alt="Main Image"
          class="background-image"
          cover
        >
          <template v-slot:placeholder>
            <v-row
              class="fill-height ma-0"
              align="center"
              justify="center"
            >
              <v-progress-circular
                indeterminate
                color="primary"
              ></v-progress-circular>
            </v-row>
          </template>
          <div class="overlay-container">
            <v-card class="white-card">
              <v-card-title class="bold-title">Build trust in your CREDITWORTHINESS</v-card-title>
              <v-card-text class="card-text">
                Retrieve your credit score without sacrificing your privacy.
              </v-card-text>
              <v-spacer></v-spacer>
              <v-card-actions class="card-actions">
                <v-btn size="x-large" class="card-button">Get your Credit Score</v-btn>
              </v-card-actions>
            </v-card>
          </div>
        </v-img>
      </v-container>
      <Footer />
    </v-container>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

const imageSrc = new URL('@/assets/images/main-wallpaper.jpg', import.meta.url).href;
</script>

<style scoped>
.image-container {
  height: 100vh;
  width: 100%;
  position: relative;
  overflow: hidden;
}

.background-image {
  height: 90vh;
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
}

.overlay-container {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  padding: 20px;
  z-index: 2;
}

.white-card {
  background-color: rgba(255, 255, 255, 0.4) !important;
  color: black !important;
  max-width: 800px;
  min-height: 300px;
  margin-bottom: 100px;
  margin-left: 40px;
  z-index: 3;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.bold-title {
  font-weight: bold;
  margin-top: 30px;
  text-transform: uppercase;
  font-size: 30px;
}

.card-text {
  font-size: 24px;
  margin: 50px 0;
  line-height: 1.5 !important; 
}

.card-actions {
  justify-content: flex-end;
}
  
.card-button {
  background-color: #76ABAE !important;
  color: black !important;
  border-radius: 10px;
}
</style>
