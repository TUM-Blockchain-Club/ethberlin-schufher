<template>
  <v-app>
    <v-container fluid class="pa-0">
      <Header />
      <v-container fluid class="image-container pa-0">
        <v-img :src="mainImageSrc" alt="Main Image" class="background-image" cover>
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </v-row>
          </template>
          <div class="overlay-container">
            <v-card class="white-card">
              <v-card-title class="bold-title">Build trust in your CREDITWORTHINESS</v-card-title>
              <v-card-text class="card-text">
                We prioritize keeping your personal data private and secure above all else. Using state-of-the-art cryptography, we are able to retrieve your credit score from your encrypted data.
              </v-card-text>
              <v-spacer></v-spacer>
              <v-card-actions class="card-actions">
                <router-link to="/login">
                  <v-btn size="x-large" class="card-button">Get your Credit Score</v-btn>
                </router-link>
              </v-card-actions>
            </v-card>
          </div>
        </v-img>
      </v-container>
      <v-container fluid class="cards-container">
        <v-row justify="space-around" class="custom-row-spacing">
          <v-col cols="12" md="5" class="custom-col-spacing">
            <v-card class="info-card">
              <v-img :src="phoneImageSrc" class="card-image"></v-img>
              <v-card-text class="card-content">
                <v-card-title class="card-heading">Your personal data will always stay encrypted and secure.</v-card-title>
                <p class="card-description">Using blockchain technology, our website ensures your data is encrypted and secure. We never access your data directly. The decentralized system guarantees your privacy and control over your information.</p>
                <a href="#" class="read-more">> Read More</a>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" md="5" class="custom-col-spacing">
            <v-card class="info-card">
              <v-img :src="laptopImageSrc" class="card-image"></v-img>
              <v-card-text class="card-content">
                <v-card-title class="card-heading">Retrieve a document that proves your personal creditworthiness.</v-card-title>
                <p class="card-description">Using our secure platform, you can access and retrieve your creditworthiness document with confidence. Rest assured, all your personal information is encrypted and protected.</p>
                <a href="#" class="read-more">> Read More</a>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row justify="center" class="custom-row-spacing">
          <v-col cols="12" md="10" class="custom-col-spacing">
            <v-card class="info-card">
              <v-img :src="newImageSrc" class="card-image"></v-img>
              <v-card-text class="card-content">
                <v-card-title class="card-heading">Obtain the most accurate credit scores from your customers by ensuring data privacy and trust.</v-card-title>
                <p class="card-description">Schufher uses advanced encryption to protect all customer data, ensuring confidentiality. By prioritizing data security, we build trust and provide the most reliable credit scores. Partner with us to enhance your credit evaluation process while safeguarding your customers' information.</p>
                <a href="#" class="read-more">> Read More</a>
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
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

const mainImageSrc = new URL('@/assets/images/main.jpg', import.meta.url).href;
const phoneImageSrc = new URL('@/assets/images/phone.jpg', import.meta.url).href;
const laptopImageSrc = new URL('@/assets/images/laptop.jpg', import.meta.url).href;
const newImageSrc = new URL('@/assets/images/city.jpg', import.meta.url).href;

</script>

<style scoped>
.image-container {
  height: 100vh;
  width: 100%;
  position: relative;
  overflow: hidden;
}

.background-image {
  height: 100vh;
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

.cards-container {
  padding: 50px 20px 100px 20px;
}

.custom-row-spacing {
  margin-bottom: 20px !important;
}

.custom-col-spacing {
  padding: 0 !important;
  margin: 10px !important;
}

.info-card {
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 20px;
  overflow: hidden;
  background-color: #31363F;
  position: relative;
}

.card-image {
  width: 50%;
  height: auto;
  min-height: 250px;
  object-fit: contain;
  border-radius: 20px;
  margin: 20px;
}

.card-content {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  padding: 20px;
}

.card-heading {
  font-size: 18px;
  font-weight: bold;
  text-transform: uppercase;
  color: white;
  margin: 0 0 10px 0;
  word-break: break-word;
  overflow-wrap: break-word;
  white-space: normal;
  padding: 0 !important;
}

.card-description {
  font-size: 14px;
  color: white;
  margin: 0 0 10px 0;
  white-space: normal;
  word-break: break-word;
  overflow-wrap: break-word;
}

.read-more {
  color: white;
  text-decoration: none;
  font-size: 16px;
  text-transform: uppercase;
  position: absolute;
  bottom: 25px;
  right: 25px;
}
</style>
