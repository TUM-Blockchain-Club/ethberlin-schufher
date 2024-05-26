<template>
    <v-app class="app-background">
      <v-container fluid class="pa-0 app-background">
        <HeaderLoggedIn />
        <v-container fluid class="image-container pa-0">
          <v-img :src="userImageSrc" alt="Main Image" class="background-image" cover>
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
              </v-row>
            </template>
            <div class="overlay-container">
              <v-card class="white-card">
                <v-card-title class="bold-title">Hello Mr. Alexander Semenov</v-card-title>
                <v-card-text class="card-text">
                  We prioritize keeping your personal data private and secure above all else. Using state-of-the-art cryptography, we are able to retrieve your credit score from your encrypted data.
                </v-card-text>
                <v-spacer></v-spacer>
                <v-card-actions class="card-actions">
                    <router-link to="/application">
                        <v-btn size="x-large" class="card-button">Get your Credit Score</v-btn>
                     </router-link>
                </v-card-actions>
              </v-card>
            </div>
          </v-img>
        </v-container>
        <v-container fluid class="cards-container">
          <v-row justify="center" class="custom-row-spacing">
            <v-col cols="12" md="3" class="custom-col-spacing">
              <v-card class="info-card">
                <v-card-text class="card-content">
                  <p class="card-description">Your personal data will always stay encrypted and secure.</p>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="3" class="custom-col-spacing">
              <v-card class="info-card">
                <v-card-text class="card-content">
                  <p class="card-description">Retrieve a document that proves your personal creditworthiness.</p>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="3" class="custom-col-spacing">
              <v-card class="info-card">
                <v-card-text class="card-content">
                  <p class="card-description">Obtain the most accurate credit scores from your customers by ensuring data privacy and trust.</p>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
        <Footer />
      </v-container>
    </v-app>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import HeaderLoggedIn from '@/components/HeaderLoggedIn.vue';
  import Footer from '@/components/Footer.vue';
  
  const userImageSrc = new URL('@/assets/images/user.jpg', import.meta.url).href;
  </script>
  
  <style scoped>
  .app-background {
    background-color: #222831 !important;
  }
  
  .image-container {
    height: 60vh;
    width: 100%;
    position: relative;
    overflow: hidden;
    background-color: #222831 !important;
  }
  
  .background-image {
    height: 100%;
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
    margin-bottom: 50px;
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
  
  .cards-container {
    padding: 20px;
  }
  
  .custom-row-spacing {
    margin-bottom: 20px !important;
  }
  
  .custom-col-spacing {
    margin: 0 10px;
  }
  
  .info-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 20px;
    overflow: hidden;
    background-color: #31363F;
    position: relative;
    max-width: 400px;
    min-height: 180px;
  }
  
  .card-content {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    padding: 50px;
  }
  
  .card-description {
    font-size: 18px;
    color: white;
    text-transform: uppercase;
    margin: 0;
    white-space: normal;
    word-break: break-word;
    overflow-wrap: break-word;
  }
  </style>
  
  <style>
  body {
    background-color: #222831;
  }
  </style>
  